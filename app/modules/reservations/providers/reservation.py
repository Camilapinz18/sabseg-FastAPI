from fastapi import HTTPException
from sqlalchemy import func, distinct

# models:
from app.modules.reservations.models.reservation import Reservation as ReservationModel
from app.modules.equipments.models.equipment import Equipment as EquipmentModel

from app.core.db.default_data.master_data.roles.roles import DefaultRoles


class Reservation():
    def get_reservations(current_user, db_session):
        reservations=None

        if current_user['role'] == DefaultRoles.client.code:
            reservations = db_session.query(ReservationModel).filter(
                ReservationModel.client_id==current_user['id']).all()
            
        if current_user['role'] == DefaultRoles.admin.code:
            reservations = db_session.query(ReservationModel).all()

        return reservations
    

    def get_reservation_by_id(id, db_session):
        reservation = db_session.query(ReservationModel).filter(ReservationModel.id == id).first()

        if not reservation:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado una reservación con el id proporcionado'
            )

        return reservation
    
    def create_reservation(reservation, db_session):
        equipments=reservation.equipments
        
        
        reservation = ReservationModel(**reservation.dict(exclude_unset=True, exclude={"equipments","room"}))
        #reservation.equipments=equipments

        total_equipments=[]

        for id in equipments:
            print("id",id)

            equipment_objects = db_session.query(EquipmentModel).filter(
                EquipmentModel.id==id).first()
            
            if not equipment_objects:
                raise HTTPException(
                    status_code=404,
                    detail='No se ha encontrado un equipo con el id proporcionado'
                )
            
            total_equipments.append(equipment_objects)
        
        print("equipment_objects",equipment_objects)
        reservation.equipments=total_equipments

        db_session.add(reservation)
        db_session.commit()
        #db_session.refresh(reservation)
        
        # equipments_to_save=[]
        
        # for data in equipments:
        #     reservation_equipments=ReservationEquipmentsModel(
        #         equipment_id = data,
        #         reservation_id = reservation.id
        #     )
            
        #     equipments_to_save.append(reservation_equipments)
            
        # db_session.add_all(equipments_to_save)
        # db_session.commit()
        
        return {"msg": f"Se han creado la reservación exitosamente"}



    def delete_room_by_id(id, db_session):
        room = db_session.query(RoomModel).filter(RoomModel.id == id).first()

        if room:
            db_session.delete(room)
            db_session.commit()
            return {"msg": "Sala eliminada correctamente"}
        else:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado una sala con el id proporcionado'
            )

    def update_room(id, room_update, db_session):
        
        room = db_session.query(RoomModel).filter(RoomModel.id == id).first()

        if not room:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado una sala con el id proporcionado'
            )

        room.name = room_update.name
        room.status = room_update.status
        room.category_name = room_update.category_name
        
        db_session.add(room)
        db_session.commit()

        return {"msg": "Sala actualizada correctamente"}
