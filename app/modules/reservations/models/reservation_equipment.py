# sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, Time, Table, String, Boolean, Date
from datetime import datetime
# base
from app.core.db.base import Base

from app.modules.reservations.models.reservation import Reservation
from app.modules.equipments.models.equipment import Equipment

class ReservationEquipments(Base):
    reservation_id = Column(Integer, ForeignKey('reservation.id'), nullable=False)
    reservation=relationship('Reservation', lazy='joined')

    equipment_id=Column(String, ForeignKey('equipment.id'), nullable=False)
    equipment=relationship('Equipment', lazy='joined')

