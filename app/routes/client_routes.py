from fastapi import APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from app.core.auth_token import decode_token, Annotated
from app.core.config import SessionLocal, engine, get_db

from app.models.client_model import Base

import app.crud.client_crud as crud
import app.schemas.client_schemas as schemas


app = APIRouter()

@app.get("/list", dependencies=[Depends(decode_token)], response_model=list[schemas.ClientBase])
def list_clients(db: Session = Depends(get_db)):
    clients = crud.get_clients(db=db)
    return clients

@app.get("/clientId/{client_id}", dependencies=[Depends(decode_token)], response_model=schemas.ClientBase)
def id_client(client_id: int, db: Session = Depends(get_db)):
    client = crud.get_client(db=db, client_id=client_id)
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return client

@app.post("/create", dependencies=[Depends(decode_token)], response_model=schemas.ClientBase)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db=db, client=client)

@app.put("/update/{client_id}", dependencies=[Depends(decode_token)], response_model=schemas.ClientBase)
def update_client(client_id: int, client: schemas.ClientUpdate, db: Session = Depends(get_db)):
    client_updated = crud.update_client(db=db, client_id=client_id, client=client)
    if client_updated is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return client_updated

