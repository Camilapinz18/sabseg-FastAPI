# fastapi
from fastapi import Depends, UploadFile, File
from fastapi import HTTPException
from fastapi import Request

# route
from ..register import users_router, module_name

# session
from app.core.db.session import get_db
from sqlalchemy.orm import Session

# provider
from app.modules.users.providers.user import Users as UsersProvider

# schemas
from app.modules.users.schemas.user import UserPost


@users_router.get("")
def get_user_me():
    """
    Get own user.
    """
    return 'current_user'


@users_router.post("")
def create_user(
    user: UserPost,
    db_session: Session = Depends(get_db)
):
    created = UsersProvider.create_user(user, db_session)
    return created
 