from fastapi import HTTPException
from sqlalchemy import func, distinct

# models:
from app.modules.equipments.models.equipment import Equipment as EquipmentModel


class Equipment():
    def create_equipment(equipment, db_session):
        equipment_data = equipment.dict()
        total_stock = equipment_data.pop('total_stock')
        
        for _ in range(total_stock):
            created = EquipmentModel(**equipment_data)
            db_session.add(created)
        
        db_session.commit()
        
        return {"msg": f"Se han creado {total_stock} equipos exitosamente"}

    def get_all_equipments(db_session):
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

    def update_equipment_by_id(id, equipment_update, db_session):
        
        equipment = db_session.query(EquipmentModel).filter(EquipmentModel.id == id).first()

        if not equipment:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado un equipo con el id proporcionado'
            )

        equipment.brand = equipment_update.brand
        equipment.reference = equipment_update.reference
        equipment.status = equipment_update.status
        equipment.category_name = equipment_update.category_name
        
        db_session.add(equipment)
        db_session.commit()

        return {"msg": "Equipo actualizado correctamente"}
