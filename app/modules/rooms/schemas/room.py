# lib
from typing import Optional
from pydantic import BaseModel, validator
from datetime import date, datetime


class RoomPost(BaseModel):
    name: str
    status: str
    category_name: str
    
    class Config:
        orm_mode = True


class RoomUpdate(BaseModel):
    name: Optional[str]
    status: Optional[str]
    category_name: Optional[str]

    class Config:
        orm_mode = True
