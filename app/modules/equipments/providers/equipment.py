from fastapi import HTTPException
from sqlalchemy import func, distinct

# models:
from app.modules.equipments.models.equipment import Equipment as EquipmentModel


class Equipment():
    def create_equipment(equipment, db_session):
        equipment_data = equipment.dict()
        equipment_data['current_stock'] = equipment.total_stock
        
        created = EquipmentModel(**equipment_data)
        db_session.add(created)
        db_session.commit()
            
        return {"msg": "Equipo creado exitosamente"}
        

    def get_equipments(db_session):
        equipments = db_session.query(EquipmentModel).all()

        return equipments

    def get_equipment_by_id(id, db_session):
        equipment = db_session.query(EquipmentModel).filter(EquipmentModel.id == id).first()

        if not equipment:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado un equipo con el id proporcionado'
            )

        return equipment

    def delete_equipment_by_id(id, db_session):
        user = db_session.query(EquipmentModel).filter(EquipmentModel.id == id).first()

        if user:
            db_session.delete(user)
            db_session.commit()
            return {"msg": "Equipo eliminado correctamente"}
        else:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado un equipo con el id proporcionado'
            )

    def update_equipment(id, user_update, db_session):
        pass
        # user = db_session.query(UserModel).filter(UserModel.id == id).first()

        # if not user:
        #     raise HTTPException(
        #         status_code=404,
        #         detail='No se ha encontrado un usuario con el id proporcionado'
        #     )

        # user.name = user_update.name
        # user.surname = user_update.surname
        # user.phone = user_update.phone

        # db_session.add(user)
        # db_session.commit()

        # return {"msg": "Usuario actualizado correctamente"}
