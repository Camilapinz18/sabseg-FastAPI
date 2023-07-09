# lib
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

# base
from app.core.db.base import Base

class Role(Base):
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
