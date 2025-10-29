from sqlalchemy import Column, Integer, String
from app.core.config import Base

class ReservationStatus(Base):
    __tablename__ = "reservation_status"

    Reservationstatus_Id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Reservationstatus_Description = Column(String(25), nullable=False)