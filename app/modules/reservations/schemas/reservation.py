# lib
from typing import Any, List, Optional
from pydantic import BaseModel, validator
from datetime import date, datetime, time


class ReservationPost(BaseModel):
    date: date
    start_hour: time
    end_hour: time
    aditional: Optional[str]
    client_id: int
    reservation_type: str
    room_id: int
    equipments: Optional[List[Any]]
    
    class Config:
        orm_mode = True


class ReservationUpdate(BaseModel):
    name: Optional[str]
    status: Optional[str]
    category_name: Optional[str]

    class Config:
        orm_mode = True
