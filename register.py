from fastapi import APIRouter

from modules.users.register import users_router

api_router = APIRouter()

api_router.include_router(users_router)
