from pydantic import BaseModel
from datetime import date, time
from typing import Optional

# --- Submodelos (para relaciones) ---
class ClientBase(BaseModel):
    Client_Id: int
    Client_Names: str

    class Config:
        orm_mode = True

class RoomBase(BaseModel):
    Room_Id: int
    Room_Number: str
    Status: str

    class Config:
        orm_mode = True

class ReservationStatusBase(BaseModel):
    Reservationstatus_Id: int
    Reservationstatus_Description: str

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    User_Id: int
    User_Names: str

    class Config:
        orm_mode = True

# --- Modelos principales ---
class ReservationBase(BaseModel):
    Res_Id: int
    User_Id: Optional[int] = None
    Reservationstatus_Id: int
    Client_Id: int
    Room_Id: int
    Check_in_date: Optional[date] = None
    Check_out_date: Optional[date] = None
    Note: Optional[str] = None
    Total: float

    cliente: Optional[str] = None
    habitacion: Optional[str] = None
    usuario: Optional[str] = None
    estado: Optional[str] = None

    class Config:
        orm_mode = True


# --- Crear reserva ---
class ReservationCreate(BaseModel):
    User_Id: int
    Reservationstatus_Id: int
    Client_Id: int
    Room_Id: int
    Check_in_date: date
    Check_out_date: date
    Note: Optional[str] = None
    Total: float

# --- Actualizar reserva ---
class ReservationUpdate(BaseModel):
    Res_Id: Optional[int] = None
    User_Id: Optional[int] = None
    Client_Id: Optional[int] = None
    Room_Id: Optional[int] = None
    User_Id: Optional[int] = None
    Reservationstatus_Id: Optional[int] = None
    Check_in_date: Optional[date] = None
    Check_out_date: Optional[date] = None
    Note: Optional[str] = None
    Total: Optional[float] = None

    class Config:
        orm_mode = True


# --- Respuesta con relaciones ---
class ReservationResponse(ReservationBase):
    id: int
    usuario: Optional["UserBase"] = None
    estado: Optional["ReservationStatusBase"] = None
    cliente: Optional["ClientBase"] = None
    habitacion: Optional["RoomBase"] = None

    class Config:
        from_attributes = True