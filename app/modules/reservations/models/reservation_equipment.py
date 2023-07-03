# sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, Time, Table, String, Boolean, Date
from datetime import datetime
# base
from app.core.db.base import Base


reservation_equipments = Table(
    'reservation_equipments',
    Base.metadata,
    Column(
        'reservation_id',
        Integer,
        ForeignKey('reservation.id')
    ),
    Column(
        'equipment_id',
        String,
        ForeignKey('equipment.id')
    ),
)
