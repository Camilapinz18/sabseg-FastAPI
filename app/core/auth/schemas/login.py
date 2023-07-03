# lib
from typing import Optional
from pydantic import BaseModel, validator
from datetime import date, datetime, time


class Login(BaseModel):
    email:str
    password:str
    
    class Config:
        orm_mode = True


