from fastapi import HTTPException
from sqlalchemy import func, distinct

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
            if user.password == login_data.password:
                return {'msg':'Inicio de sesión exitoso'}
            else:
                raise HTTPException(
                    status_code=400,
                    detail='Contraseña incorrecta'
                )
        