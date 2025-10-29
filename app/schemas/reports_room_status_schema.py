from pydantic import BaseModel
from datetime import date
from decimal import Decimal

class ReservationReportItem(BaseModel):
    reservation_id: int
    client_name: str
    room_id: int
    check_in: date
    check_out: date
    total: Decimal
    status_id: int

    class Config:
        orm_mode = True
