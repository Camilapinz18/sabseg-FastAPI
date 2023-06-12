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
    confirm_password: str

    class Config:
        orm_mode = True
