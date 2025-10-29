from pydantic import BaseModel
from typing import Optional

class DashboardCounts(BaseModel):
    total_reservations: int
    total_rooms: int
    total_categories: int
    total_clients: int