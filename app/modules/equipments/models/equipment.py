# sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, DateTime, Table, String, Boolean, Text
from datetime import datetime

# base
from app.core.db.base import Base
from .equipment_category import EquipmentCategory
from app.modules.reservations.models.reservation_equipment import reservation_equipments


class Equipment(Base):
    brand = Column(String, nullable=False)
    reference = Column(String, nullable=False)
    photo = Column(String, nullable=True)
    status = Column(String, nullable=True)
    category_name = Column(String, ForeignKey('equipment_category.name'))
    
    category= relationship('EquipmentCategory', lazy='joined')

    reservations = relationship(
        'Reservation',
        secondary=reservation_equipments,
        back_populates='equipments'
    )

    
