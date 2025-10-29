from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.auth_token import decode_token
from app.core.config import get_db

from app.models.room_model import Room
from app.models.room_type_model import RoomType

import app.crud.reservation_crud as crud
import app.schemas.reservation_schemas as schemas

app = APIRouter()


@app.get("/list", dependencies=[Depends(decode_token)], response_model=list[schemas.ReservationBase])
def list_reservas(db: Session = Depends(get_db)):
    reservas = crud.get_reservas(db=db)
    return reservas


@app.get("/reservaId/{reserva_id}", dependencies=[Depends(decode_token)], response_model=schemas.ReservationBase)
def id_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = crud.get_reserva(db=db, reserva_id=reserva_id)
    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return reserva


@app.post("/create", dependencies=[Depends(decode_token)], response_model=schemas.ReservationCreate)
def reserva_create(reserva: schemas.ReservationCreate, db: Session = Depends(get_db)):
    crud.crear_reserva(db=db, reserva=reserva)
    return reserva  


@app.put("/update/{reserva_id}", dependencies=[Depends(decode_token)], response_model=schemas.ReservationBase)
def reserva_update(reserva_id: int, reserva: schemas.ReservationUpdate, db: Session = Depends(get_db)):
    return crud.actualizar_reserva(db=db, reserva_id=reserva_id, reserva=reserva)


@app.get("/estados", dependencies=[Depends(decode_token)])
def list_estados(db: Session = Depends(get_db)):
    return crud.get_estados(db=db)


@app.get("/habitaciones", dependencies=[Depends(decode_token)])
def list_habitaciones(db: Session = Depends(get_db)):
    habitaciones = db.query(Room).filter(Room.Roomstatus_Id == 1).all()
    resultado = []

    for h in habitaciones:
        room_type = db.query(RoomType).filter(RoomType.Roomtype_Id == h.Roomtype_Id).first()
        tipo_desc = room_type.Roomtype_Description if room_type else "Desconocido"

        resultado.append({
            "id": h.Room_Id,
            "label": f"{h.Room_Id} - {tipo_desc}"  
        })

    return resultado

@app.get("/habitaciones/todas", dependencies=[Depends(decode_token)])
def list_todas_habitaciones(db: Session = Depends(get_db)):
    habitaciones = db.query(Room).all()
    resultado = []

    for h in habitaciones:
        room_type = db.query(RoomType).filter(RoomType.Roomtype_Id == h.Roomtype_Id).first()
        tipo_desc = room_type.Roomtype_Description if room_type else "Desconocido"

        resultado.append({
            "id": h.Room_Id,
            "label": f"{h.Room_Id} - {tipo_desc}",
            "status": h.Roomstatus_Id
        })

    return resultado



@app.get("/clientes", dependencies=[Depends(decode_token)])
def list_clientes(db: Session = Depends(get_db)):
    from app.models.client_model import Client
    clientes = db.query(Client).all()
    return [{"id": c.Client_Id, "label": c.Client_Names} for c in clientes]
