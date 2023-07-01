from fastapi import HTTPException
from sqlalchemy import func, distinct

# models:
from app.modules.equipments.models.equipment_category import EquipmentCategory as EquipmentCategoryModel


class EquipmentCategory():
    
    def get_all_equipments_categories(db_session):
        equipments = db_session.query(EquipmentCategoryModel).all()

        return equipments