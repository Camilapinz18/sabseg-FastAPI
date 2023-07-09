# fastapi
from fastapi import Depends, UploadFile, File
from fastapi import HTTPException
from fastapi import Request

# route
from ..register import reservations_router

# session
from app.core.db.session import get_db
from sqlalchemy.orm import Session

# provider
from app.modules.reservations.providers.reservation import Reservation as ReservationProvider

# schemas
from app.modules.reservations.schemas.reservation import ReservationPost, ReservationUpdate
from app.core.security import auth_wrapper




@reservations_router.get("")
def get_reservations(
    _=Depends(auth_wrapper),
    db_session: Session = Depends(get_db)
):
    reservations = ReservationProvider.get_reservations(db_session)
    return reservations


@reservations_router.get("/{id}")
def get_reservation_by_id(
    id: int,
    db_session: Session = Depends(get_db)
):
    reservation = ReservationProvider.get_reservation_by_id(id, db_session)
    return reservation

 
@reservations_router.post("")
def create_reservation(
    reservation: ReservationPost,
    db_session: Session = Depends(get_db)
):
    created = ReservationProvider.create_reservation(reservation,  db_session)
    return created


@reservations_router.put("/{id}")
def update_reservation(
    id: int,
    reservation_update: ReservationUpdate,
    db_session: Session = Depends(get_db)
):
    room = ReservationProvider.update_reservation(id, reservation_update, db_session)
    return room


@reservations_router.delete("/{id}")
def delete_reservation_by_id(
    id: int,
    db_session: Session = Depends(get_db)
):
    reservation = ReservationProvider.delete_reservation_by_id(id, db_session)
    return reservation
