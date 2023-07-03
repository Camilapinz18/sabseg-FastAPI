# sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, Time, Table, String, Boolean, Date
from datetime import datetime

# base
from app.core.db.base import Base

#models
from app.modules.users.models.user import User
from app.modules.reservations.models.reservation_type import ReservationType
from app.modules.rooms.models.room import Room
from app.modules.reservations.models.reservation_equipment import reservation_equipments

class Reservation(Base):
    date = Column(Date, nullable=False)
    start_hour = Column(Time, nullable=False)
    end_hour = Column(Time, nullable=False)
    aditional=Column(String, nullable=True)
    
    client_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    client=relationship('User', lazy='joined')

    reservation_type=Column(Integer, ForeignKey('reservation_type.id'), nullable=False)
    reservation=relationship('ReservationType', lazy='joined')

    room_id=Column(Integer, ForeignKey('room.id'), nullable=False)
    room=relationship('Room', lazy='joined')

    equipments = relationship(
        'Equipment',
        lazy="joined",
        secondary=reservation_equipments,
        back_populates='reservations'
    )


