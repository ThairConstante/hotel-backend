from sqlalchemy import Column, Integer, String
from app.core.config import Base

class Client(Base):
    __tablename__ = "client"

    Client_Id = Column(Integer, primary_key=True, index=True)
    Client_Names = Column(String(50), nullable=False)
    Client_Mail = Column(String(50), nullable=False)
    Client_Phone = Column(String(50), nullable=True)
