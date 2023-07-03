# fastapi
from fastapi import Depends, UploadFile, File
from fastapi import HTTPException
from fastapi import Request

# route
from ..register import equipments_router

# session
from app.core.db.session import get_db
from sqlalchemy.orm import Session

# provider
from app.modules.equipments.providers.equipment import Equipment as EquipmentProvider

# schemas
from app.modules.equipments.schemas.equipment import EquipmentPost, EquipmentUpdate
from app.modules.equipments.schemas.available_equipments import AvailableEquipmentPost


@equipments_router.get("")
def get_all_equipments(
    db_session: Session = Depends(get_db)
):
    equipments = EquipmentProvider.get_all_equipments(db_session)
    return equipments


@equipments_router.get("/{id}")
def get_equipment_by_id(
    id: int,
    db_session: Session = Depends(get_db)
):
    equipment = EquipmentProvider.get_equipment_by_id(id, db_session)
    return equipment


@equipments_router.post("")
def create_equipment(
    equipment: EquipmentPost,
    db_session: Session = Depends(get_db)
):
    created = EquipmentProvider.create_equipment(equipment,  db_session)
    return created


@equipments_router.put("/{id}")
def update_equipment_by_id(
    id: int,
    equipment_update: EquipmentUpdate,
    db_session: Session = Depends(get_db)
):
    equipment = EquipmentProvider.update_equipment_by_id(id, equipment_update, db_session)
    return equipment


@equipments_router.delete("/{id}")
def delete_equipment_by_id(
    id: int,
    db_session: Session = Depends(get_db)
):
    equipment = EquipmentProvider.delete_equipment_by_id(id, db_session)
    return equipment

@equipments_router.post("/available/")
def get_available_equipments(
    available: AvailableEquipmentPost,
    db_session: Session = Depends(get_db)
):
    room = EquipmentProvider.get_available_equipments(available, db_session)
    return room