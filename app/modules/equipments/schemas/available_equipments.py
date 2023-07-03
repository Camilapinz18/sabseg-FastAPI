# lib
from typing import Optional
from pydantic import BaseModel, validator
from datetime import date, datetime, time


class AvailableEquipmentPost(BaseModel):
    date: date
    start_hour: time
    end_hour: time
    
    class Config:
        orm_mode = True


