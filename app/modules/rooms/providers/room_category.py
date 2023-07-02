from fastapi import HTTPException
from sqlalchemy import func, distinct

# models:
from app.modules.rooms.models.room_category import RoomCategory as RoomCategoryModel


class RoomCategory():

    def get_rooms_categories(db_session):
        rooms = db_session.query(RoomCategoryModel).all()

        return rooms
    