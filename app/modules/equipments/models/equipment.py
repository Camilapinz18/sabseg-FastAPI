# sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, DateTime, Table, String, Boolean, Text
from datetime import datetime

# base
from app.core.db.base import Base


class Equipment(Base):
    brand = Column(String, nullable=False)
    reference = Column(String, nullable=False)
    photo = Column(String, nullable=True)
    total_stock = Column(Integer, nullable=False)
    current_stock = Column(Integer, nullable=False)
    status = Column(String, nullable=True)