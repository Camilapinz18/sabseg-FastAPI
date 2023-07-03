from fastapi import HTTPException
from sqlalchemy import func, distinct
from sqlalchemy.orm import aliased
from sqlalchemy.sql import and_, or_, not_  # Import the necessary logical operators
from sqlalchemy.sql.expression import literal_column
from datetime import datetime

# models:
from app.modules.equipments.models.equipment import Equipment as EquipmentModel
from app.modules.reservations.models.reservation import Reservation as ReservationModel
from app.modules.reservations.models.reservation_equipment import reservation_equipments


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
    
    def get_available_equipments(available, db_session):

        reservation_ids = db_session.query(ReservationModel).filter(
                ReservationModel.date == available.date,
                ReservationModel.start_hour <= available.end_hour,
                ReservationModel.end_hour >= available.start_hour
        ).all()
                
        reserved_equipments=[]
        
        for reservation in reservation_ids:
            for equipment in reservation.equipments:
                reserved_equipments.append(equipment.id)       
        
        distinct_equipments = list(set(reserved_equipments))
        
        available_equipment = db_session.query(EquipmentModel).filter(
            ~EquipmentModel.id.in_(distinct_equipments)
        ).all()              
    
        return available_equipment
