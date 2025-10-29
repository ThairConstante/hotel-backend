from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from app.core.config import Base

class Reservation(Base):
    __tablename__ = "reservation"

    Res_Id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    User_Id = Column(Integer, ForeignKey("user.User_Id"))
    Reservationstatus_Id = Column(Integer, ForeignKey("reservation_status.Reservationstatus_Id"))
    Client_Id = Column(Integer, ForeignKey("client.Client_Id"))
    Room_Id = Column(Integer, ForeignKey("room.Room_Id"))
    Check_in_date = Column(Date, nullable=False)
    Check_out_date = Column(Date, nullable=False)
    Note = Column(String(100), nullable=True)
    Total = Column(DECIMAL(10,2), nullable=True)

