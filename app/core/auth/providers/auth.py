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

from fastapi.security import OAuth2PasswordRequestForm


import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta


# models:
from app.modules.users.models.user import User as UserModel


class Auth():

    security= HTTPBearer()
    pwd_context= CryptContext(schemes=['bcrypt'], deprecated='auto')
    secret='SECRET'

    def get_password_hash(password):
        return Auth.pwd_context.hash(password)
    
    def verify_password(plain_password, hashed_password):

        return Auth.pwd_context.verify(plain_password, hashed_password)


    
    def encode_token(user_id):
        payload={
            'exp':datetime.utcnow()+ timedelta(days=0, minutes=5),
            'iat':datetime.utcnow(),
            'sub':user_id

        }
        return jwt.encode(
            payload,
            Auth.secret,
            algorithm='HS256'
        )
    
    def decode_token(token):
        try:
            payload=jwt.decode(token, Auth.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='SU sesión ha finalzado')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Token inválido')

    def auth_wrapper(auth: HTTPAuthorizationCredentials= Security(security)):
        return Auth.decode_token(auth.credentials)

    
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
            if not Auth.verify_password(plain_password, hashed_password):
                print("INCORRECT____", plain_password, hashed_password)
                raise HTTPException(
                    status_code=401,
                    detail='Contraseña incorrecta'
                )
            else:
                token=Auth.encode_token(login_data.email)
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
            hashed_password=Auth.get_password_hash(password)
            register_data.password=hashed_password
            print("EGISTER",register_data)

            user_data = register_data.dict(exclude={"confirm_password"})


            created = UserModel(**user_data)
            db_session.add(created)
            db_session.commit()

            return {"msg": "Registro de usuario exitoso"}
        
        


