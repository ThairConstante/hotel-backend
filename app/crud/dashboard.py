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
    month_expr = func.date_format(Reservation.Check_in_date, "%m")
    month_name_expr = func.date_format(Reservation.Check_in_date, "%M")

    results = (
        db.query(
            month_expr.label("month"),
            month_name_expr.label("month_name"),
            func.sum(Reservation.Total).label("total_sales")
        )
        .group_by(month_expr, month_name_expr)
        .order_by(month_expr)
        .all()
    )

    return [
        {"month": r.month_name, "total_sales": float(r.total_sales)}
        for r in results
    ]
