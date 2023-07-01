from fastapi import APIRouter

from .modules.users.register import users_router
from .modules.equipments.register import equipments_router
from .modules.rooms.register import rooms_router

api_router = APIRouter()

api_router.include_router(users_router)
api_router.include_router(equipments_router)
api_router.include_router(rooms_router)
