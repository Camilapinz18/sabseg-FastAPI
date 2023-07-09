from fastapi import HTTPException
from sqlalchemy import func, distinct
# fastapi
from fastapi import Depends, UploadFile, File
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Request

# route
from ..register import auth_router

# session
from app.core.db.session import get_db
from sqlalchemy.orm import Session

# provider

# schemas
from app.core.auth.schemas.login import Login

from app.core.security import *


# models:
from app.modules.users.models.user import User as UserModel


class Auth():
    def login(login_data,db_session):
        user=db_session.query(UserModel).filter(UserModel.email==login_data.email).first()
        
        if not user:
            raise HTTPException(
                status_code=404,
                detail="El email proporcionado no se encuentra registrado"
            )
        else:
            plain_password= login_data.password
            hashed_password = user.password
            if not verify_password(plain_password, hashed_password):
                print("INCORRECT____", plain_password, hashed_password)
                raise HTTPException(
                    status_code=401,
                    detail='Contraseña incorrecta'
                )
            else:
                token=encode_token(login_data.email)
                return {'token':token}


        
    def register(register_data, db_session):
        email_exists = db_session.query(UserModel).filter(
                UserModel.email == register_data.email).first()

        if email_exists:
            raise HTTPException(
                status_code=400,
                detail="El email ya se encuentra registrado. Inicia sesión o prueba con otro email"
            )

        if register_data.password == register_data.confirm_password:
            
            password=register_data.password
            hashed_password=get_password_hash(password)
            register_data.password=hashed_password
            print("EGISTER",register_data)

            user_data = register_data.dict(exclude={"confirm_password"})


            created = UserModel(**user_data)
            db_session.add(created)
            db_session.commit()

            return {"msg": "Registro de usuario exitoso"}
        
        


