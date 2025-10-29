from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from app.core.auth_token import decode_token, Annotated
from app.core.config import SessionLocal, engine, get_db
from typing import Optional

from app.models.reservation_model import Reservation
from app.models.reservation_status_model import ReservationStatus
from app.models.client_model import Client
from app.models.room_model import Room
from app.models.room_type_model import RoomType


app = APIRouter()

@app.get("/reservations", dependencies=[Depends(decode_token)])
def get_reservation_report(
    tipo: Optional[int] = Query(None),
    estado: Optional[int] = Query(None),
    desde: Optional[str] = Query(None),
    hasta: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = (
        db.query(
            Client.Client_Names.label("Cliente"),
            Room.Room_Id.label("Habitacion"),
            RoomType.Roomtype_Description.label("Tipo"),
            Reservation.Check_in_date.label("CheckIn"),
            Reservation.Check_out_date.label("CheckOut"),
            ReservationStatus.Reservationstatus_Description.label("Estado"),
            Reservation.Total.label("Total"),
        )
        .outerjoin(Room, Room.Room_Id == Reservation.Room_Id)
        .outerjoin(RoomType, RoomType.Roomtype_Id == Room.Roomtype_Id)
        .outerjoin(Client, Client.Client_Id == Reservation.Client_Id)
        .outerjoin(ReservationStatus, ReservationStatus.Reservationstatus_Id == Reservation.Reservationstatus_Id)  # ✅ corregido
    )

    if tipo:
        query = query.filter(RoomType.Roomtype_Id == tipo)
    if estado:
        query = query.filter(ReservationStatus.Reservationstatus_Id == estado)
    if desde and hasta:
        query = query.filter(Reservation.Check_in_date.between(desde, hasta))

    results = query.all()
    return [dict(r._mapping) for r in results]


@app.get("/reservation_status", dependencies=[Depends(decode_token)])
def get_status(db: Session = Depends(get_db)):
    return db.query(ReservationStatus).all()


@app.get("/room_type", dependencies=[Depends(decode_token)])
def obtener_tipos(db: Session = Depends(get_db)):
    return db.query(RoomType).all()

