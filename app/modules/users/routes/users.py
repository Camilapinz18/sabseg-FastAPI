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
from app.modules.users.schemas.user import UserPost, UserUpdate, UserGet


@users_router.get("")
def get_users(
    db_session: Session = Depends(get_db)
):
    users = UsersProvider.get_users(db_session)
    return users


@users_router.get("/{id}", response_model=UserGet)
def get_user_by_id(
    id: int,
    db_session: Session = Depends(get_db)
)-> UserGet:
    user = UsersProvider.get_user_by_id(id, db_session)
    return user


@users_router.post("")
def create_user(
    user: UserPost,
    db_session: Session = Depends(get_db)
):
    created = UsersProvider.create_user(user,  db_session)
    return created


@users_router.put("/{id}")
def update_user(
    id: int,
    user_update: UserUpdate,
    db_session: Session = Depends(get_db)
):
    user = UsersProvider.update_user(id, user_update, db_session)
    return user


@users_router.delete("/{id}")
def delete_user_by_id(
    id: int,
    db_session: Session = Depends(get_db)
):
    user = UsersProvider.delete_user_by_id(id, db_session)
    return user
