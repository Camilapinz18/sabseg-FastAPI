# fastapi
from fastapi import Depends, UploadFile, File
from fastapi import HTTPException
from fastapi import Request

# route
from ..register import rooms_router

# session
from app.core.db.session import get_db
from sqlalchemy.orm import Session

# provider
from app.modules.rooms.providers.room import Room as RoomProvider

# schemas
from app.modules.rooms.schemas.room import RoomPost, RoomUpdate


@rooms_router.get("")
def get_rooms(
    db_session: Session = Depends(get_db)
):
    users = RoomProvider.get_rooms(db_session)
    return users


@rooms_router.get("/{id}")
def get_room_by_id(
    id: int,
    db_session: Session = Depends(get_db)
):
    room = RoomProvider.get_room_by_id(id, db_session)
    return room


@rooms_router.post("")
def create_room(
    room: RoomPost,
    db_session: Session = Depends(get_db)
):
    created = RoomProvider.create_room(room,  db_session)
    return created


@rooms_router.put("/{id}")
def update_room(
    id: int,
    room_update: RoomUpdate,
    db_session: Session = Depends(get_db)
):
    room = RoomProvider.update_room(id, room_update, db_session)
    return room


@rooms_router.delete("/{id}")
def delete_room_by_id(
    id: int,
    db_session: Session = Depends(get_db)
):
    room = RoomProvider.delete_room_by_id(id, db_session)
    return room
