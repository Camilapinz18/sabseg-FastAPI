from fastapi import HTTPException
from sqlalchemy import func, distinct

#models:
from app.modules.users.models.user import User as UserModel




class Users():
    def create_user(user, db_session):

        created = (UserModel(**user.dict()))
        db_session.add(created)
        db_session.commit()

        return {"msg": "PQRS creada exitosamente"}
