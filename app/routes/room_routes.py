from fastapi import APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from app.core.auth_token import decode_token, Annotated
from app.core.config import SessionLocal, engine, get_db

from app.models.room_model import Base

import app.crud.room_crud as crud
import app.schemas.room_schemas as schemas

app = APIRouter()


@app.get("/list", dependencies=[Depends(decode_token)], response_model=list[schemas.RoomBase])
def list_rooms(db: Session = Depends(get_db)):
    habitaciones = crud.get_rooms(db=db)
    return habitaciones


@app.get("/roomId/{room_id}", dependencies=[Depends(decode_token)], response_model=schemas.RoomBase)
def id_room(room_id: int, db: Session = Depends(get_db)):
    habitacion = crud.get_room_por_id(db=db, room_id=room_id)
    if habitacion is None:
        raise HTTPException(status_code=404, detail="Habitacion no encontrada")
    return habitacion

@app.post("/create", dependencies=[Depends(decode_token)], response_model=schemas.RoomCreate)
def room_create(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    return crud.room_create(db=db, room=room)


@app.put("/update/{room_id}", dependencies=[Depends(decode_token)], response_model=schemas.RoomBase)
def room_update(room_id: int, room: schemas.RoomUpdate, db: Session = Depends(get_db)):
    updated_room = crud.room_update(db=db, room_id=room_id, room=room)
    if updated_room is None:
        raise HTTPException(status_code=404, detail="Habitación no encontrada")
    return updated_room



@app.get("/types", dependencies=[Depends(decode_token)])
def list_room_types(db: Session = Depends(get_db)):
    tipos = crud.get_tipos(db)
    return tipos


@app.get("/statuses", dependencies=[Depends(decode_token)])
def list_room_statuses(db: Session = Depends(get_db)):
    estados = crud.get_estados(db)
    return estados


