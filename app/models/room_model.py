from sqlalchemy import Column, Integer, DECIMAL, ForeignKey
from app.core.config import Base

class Room(Base):
    __tablename__ = "room"

    Room_Id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Room_night_price = Column(DECIMAL(10,2), nullable=False)
    Room_day_price = Column(DECIMAL(10,2), nullable=False)
    Room_Capacity = Column(Integer, nullable=False)
    Roomstatus_Id = Column(Integer, ForeignKey("room_status.Roomstatus_Id"))
    Roomtype_Id = Column(Integer, ForeignKey("room_type.Roomtype_Id"))
