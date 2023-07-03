# fastapi
from fastapi import Depends, UploadFile, File
from fastapi import HTTPException
from fastapi import Request

# route
from ..register import auth_router

# session
from app.core.db.session import get_db
from sqlalchemy.orm import Session

# provider
from app.core.auth.providers.auth import Auth as AuthProvider
# schemas
from app.core.auth.schemas.login import Login


@auth_router.post("/login")
def login(
    login_data:Login,
    db_session: Session = Depends(get_db)
):
    login = AuthProvider.login(login_data,db_session)
    return login
