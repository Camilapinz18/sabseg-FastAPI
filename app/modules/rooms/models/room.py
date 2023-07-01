# sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, DateTime, Table, String, Boolean, Text
from datetime import datetime

# base
from app.core.db.base import Base
from .room_category import RoomCategory

class Room(Base):
    name = Column(String, nullable=False)
    status=Column(String, nullable=False)
    category_name = Column(String, ForeignKey('room_category.name'), nullable=False)
    
    category= relationship('RoomCategory', lazy='joined')