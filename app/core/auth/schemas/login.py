# lib
from typing import Optional
from pydantic import BaseModel, validator
from datetime import date, datetime, time


class Login(BaseModel):
    email:str
    password:str
    
    class Config:
        orm_mode = True


class Register(BaseModel):
    email:str
    password:str
    confirm_password: str
    name: str
    surname: str
    phone: str
    attendance: int    
    
    class Config:
        orm_mode = True


