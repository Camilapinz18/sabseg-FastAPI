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
from app.modules.rooms.providers.room_category import RoomCategory as RoomCategoryProvider

# schemas
from app.modules.rooms.schemas.room import RoomPost, RoomUpdate


@rooms_router.get("/categories/")
def get_rooms(
    db_session: Session = Depends(get_db)
):
    rooms = RoomCategoryProvider.get_rooms_categories(db_session)
    return rooms

