# lib
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

# base
from app.core.db.base import Base

class Roles(Base):
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    
