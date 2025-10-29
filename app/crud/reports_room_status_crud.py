from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.reservation_model import Reservation
from app.models.client_model import Client
from app.models.room_model import Room

def get_reservation_report(db: Session):
    """
    Retorna una lista con la información combinada de las reservas, clientes y habitaciones.
    """
    query = (
        db.query(
            Reservation.Res_Id.label("reservation_id"),
            Client.Client_Names.label("client_name"),
            Room.Room_Id.label("room_id"),
            Reservation.Check_in_date.label("check_in"),
            Reservation.Check_out_date.label("check_out"),
            Reservation.Total.label("total"),
            Reservation.Reservationstatus_Id.label("status_id"),
        )
        .join(Client, Reservation.Client_Id == Client.Client_Id)
        .join(Room, Reservation.Room_Id == Room.Room_Id)
        .all()
    )
    return query
