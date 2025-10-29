from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class ClientBase(BaseModel):
    Client_Id: int
    Client_Names: str
    Client_Mail: str
    Client_Phone: Optional[str] = None

class ClientCreate(BaseModel):
    Client_Id: int
    Client_Names: str
    Client_Mail: str
    Client_Phone: Optional[str] = None

class ClientUpdate(BaseModel):
    Client_Names: str
    Client_Mail: str
    Client_Phone: Optional[str] = None

