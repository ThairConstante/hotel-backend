from sqlalchemy import Column, Integer, String
from app.core.config import Base

class RoomStatus(Base):
    __tablename__ = "room_status"

    Roomstatus_Id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Roomstatus_Description = Column(String(25), nullable=False)
