# lib
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

# base
from app.core.db.base import Base

class DefaultDataVersion(Base):
    __tablename__ = 'default_data_version'

    name = Column(String, nullable=False)
    version = Column(Integer, nullable=True)
