# sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, DateTime, Table, String, Boolean, Text
from datetime import datetime

# base
from app.core.db.base import Base


class ReservationType(Base):
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    