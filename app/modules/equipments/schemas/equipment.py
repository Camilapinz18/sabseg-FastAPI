# lib
from typing import Optional
from pydantic import BaseModel, validator
from datetime import date, datetime


class EquipmentPost(BaseModel):
    brand: str
    reference: str
    photo: Optional[str]
    total_stock: int
    status: Optional[str]
    category_name: str

    class Config:
        orm_mode = True


class EquipmentUpdate(BaseModel):
    brand: Optional[str]
    reference: Optional[str]
    photo: Optional[str]
    total_stock: Optional[int]
    status: Optional[str]
    category_name: Optional[str]

    class Config:
        orm_mode = True
