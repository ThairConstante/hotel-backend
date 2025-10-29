from pydantic import BaseModel
from typing import Optional


# --- Submodelos (para relaciones) ---
class RoomTypeBase(BaseModel):
    Roomtype_Id: int
    Roomtype_Description: str

    class Config:
        orm_mode = True


class RoomStatusBase(BaseModel):
    Roomstatus_Id: int
    Roomstatus_Description: str

    class Config:
        orm_mode = True


# --- Modelos principales ---
class RoomBase(BaseModel):

    Room_Id: int
    Room_night_price: float
    Room_day_price: float
    Room_Capacity: int
    Roomstatus_Id: int
    Roomtype_Id: int

    tipo: Optional[RoomTypeBase] = None
    estado: Optional[RoomStatusBase] = None

    class Config:
        orm_mode = True


class RoomCreate(BaseModel):
    Room_Id: int
    Room_night_price: float
    Room_day_price: float
    Room_Capacity: int
    Roomstatus_Id: int
    Roomtype_Id: int

class RoomUpdate(BaseModel):
    Room_Id: int
    Room_night_price: Optional[float] = None
    Room_day_price: Optional[float] = None
    Room_Capacity: Optional[int] = None
    Roomstatus_Id: Optional[int] = None
    Roomtype_Id: Optional[int] = None

    class Config:
        orm_mode = True

