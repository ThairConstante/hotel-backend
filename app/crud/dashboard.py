from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.reservation_model import Reservation
from app.models.room_model import Room
from app.models.room_type_model import RoomType
from app.models.client_model import Client


def get_dashboard_counts(db: Session):
    total_reservations = db.query(Reservation).count()
    total_rooms = db.query(Room).count()
    total_categories = db.query(RoomType).count()
    total_clients = db.query(Client).count()

    return {
        "total_reservations": total_reservations,
        "total_rooms": total_rooms,
        "total_categories": total_categories,
        "total_clients": total_clients
    }

def get_sales_by_month(db: Session):
    results = (
        db.query(
            func.date_format(Reservation.Check_in_date, "%m").label("month"),
            func.sum(Reservation.Total).label("total_sales")
        )
        .group_by(func.date_format(Reservation.Check_in_date, "%M"))
        .order_by(func.min(Reservation.Check_in_date))  # asegura orden cronológico
        .all()
    )

    return [{"month": r.month, "total_sales": float(r.total_sales)} for r in results]
