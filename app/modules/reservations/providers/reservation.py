from fastapi import HTTPException
from sqlalchemy import func, distinct

# models:
from app.modules.reservations.models.reservation import Reservation as ReservationModel


class Reservation():
    def get_reservations(db_session):
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
        
        reservation = ReservationModel(**reservation.dict(exclude_unset=True,
                                 exclude={"equipments"}))

        db_session.add(reservation)
        

        
        db_session.commit()
        
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
