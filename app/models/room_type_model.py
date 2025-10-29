from sqlalchemy import Column, Integer, String
from app.core.config import Base

class RoomType(Base):
    __tablename__ = "room_type"

    Roomtype_Id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Roomtype_Description = Column(String(25), nullable=False)
