# lib
from typing import Optional
from pydantic import BaseModel, validator
from datetime import date, datetime


class UserPost(BaseModel):
    name: str
    surname: str
    phone: str
    email: str
    password: str
    attendance: int
    confirm_password: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    phone: Optional[str]

    class Config:
        orm_mode = True

class UserGet(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    phone: Optional[str]
    email: Optional[str]

    class Config:
        orm_mode = True

