# fastapi
from fastapi import Depends, UploadFile, File
from fastapi import HTTPException
from fastapi import Request


# providers
from ..providers.users import Users

# route
from ..register import users_router


@users_router.get("/me")
def get_user_me():
    return 'get user'
