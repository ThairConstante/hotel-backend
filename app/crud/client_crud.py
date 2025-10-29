from sqlalchemy.orm import Session
from app.models.client_model import Client
import app.schemas.client_schemas as schemas

def get_clients(db: Session):
    return db.query(Client).all()

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.Client_Id == client_id).first()

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def update_client(db: Session, client_id: int, client: schemas.ClientUpdate):
    db_client = db.query(Client).filter(Client.Client_Id == client_id).first()
    if db_client:
        db_client.Client_Names = client.Client_Names
        db_client.Client_Mail = client.Client_Mail
        db_client.Client_Phone = client.Client_Phone
        db.commit()
        db.refresh(db_client)
    return db_client

