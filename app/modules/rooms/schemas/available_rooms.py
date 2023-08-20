# lib
from typing import Optional
from pydantic import BaseModel, validator
from datetime import date, datetime, time


class AvailableRoomPost(BaseModel):
    room_type: str
    date: date
    start_hour: time
    end_hour: time
    
    class Config:
        orm_mode = True


