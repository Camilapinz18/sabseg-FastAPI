from fastapi import HTTPException
from sqlalchemy import func, distinct

from app.core.db.default_data.master_data.users.users import DefaultUsers

# models:
from app.modules.users.models.user import User as UserModel


class Users():
    def create_user(user, db_session):

        if user.password == user.confirm_password:

            email_exists = db_session.query(UserModel).filter(
                UserModel.email == user.email).first()

            if email_exists:
                raise HTTPException(
                    status_code=400,
                    detail="El email ya se encuentra registrado. Inicia sesión o prueba con otro email"
                )
            
            
            user_data = user.dict(exclude={"confirm_password"})

            created = UserModel(**user_data)
            db_session.add(created)
            db_session.commit()

            return {"msg": "Usuario creado exitosamente"}
        else:
            raise HTTPException(
                status_code=400,
                detail='Las contraseñas deben coincidir'
            )

    def get_users(db_session):
        users = db_session.query(UserModel).all()

        return users

    def get_user_by_id(id, db_session):
        user = db_session.query(UserModel).filter(UserModel.id == id).first()

        if not user:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado un usuario con el id proporcionado'
            )

        return user

    def delete_user_by_id(id, db_session):
        user = db_session.query(UserModel).filter(UserModel.id == id).first()

        if user.email == DefaultUsers.admin.value[0]:
            raise HTTPException(
                status_code=400,
                detail="No se puede eliminar al usuario Administrador"
            )

        if user:
            db_session.delete(user)
            db_session.commit()
            return {"msg": "Usuario eliminado correctamente"}
        else:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado un usuario con el id proporcionado'
            )

    def update_user(id, user_update, db_session):

        user = db_session.query(UserModel).filter(UserModel.id == id).first()

        if not user:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado un usuario con el id proporcionado'
            )

        user.name = user_update.name
        user.surname = user_update.surname
        user.phone = user_update.phone

        db_session.add(user)
        db_session.commit()

        return {"msg": "Usuario actualizado correctamente"}
