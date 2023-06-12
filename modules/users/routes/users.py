# fastapi
from fastapi import Depends, UploadFile, File
from fastapi import HTTPException
from fastapi import Request

# route
from ..register import users_router, module_name


@users_router.get("/me")
def get_user_me():
    """
    Get own user.
    """
    return 'current_user'
