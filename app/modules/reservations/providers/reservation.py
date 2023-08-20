from fastapi import HTTPException
from sqlalchemy import func, distinct

# models:
from app.modules.reservations.models.reservation import Reservation as ReservationModel
from app.modules.equipments.models.equipment import Equipment as EquipmentModel

from app.core.db.default_data.master_data.roles.roles import DefaultRoles


class Reservation():
    def get_reservations(current_user, db_session):
        reservations = None

        if current_user['role'] == DefaultRoles.client.code:
            reservations = db_session.query(ReservationModel).filter(
                ReservationModel.client_id == current_user['id']).all()

        if current_user['role'] == DefaultRoles.admin.code:
            reservations = db_session.query(ReservationModel).all()

        reservation_to_return = []

        for r in reservations:

            obj = {
                'id': r.id,
                'url': '',
                'title': str(r.start_hour) + ' ' + str(r.end_hour),
                'time': {
                    'start': str(r.date) + ' '+str(r.start_hour),
                    'end': str(r.date) + ' ' + str(r.end_hour),
                },
                'tags': r.reservation.name,
                'location': r.room.name,
                'client':r.client.id

            }

            reservation_to_return.append(obj)


        return reservation_to_return

    def get_reservation_by_id(id, db_session):
        reservation = db_session.query(ReservationModel).filter(
            ReservationModel.id == id).first()

        if not reservation:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado una reservación con el id proporcionado'
            )

        return reservation

    def create_reservation(reservation, db_session, current_user):
        equipments = reservation.equipments

        reservation = ReservationModel(
            **reservation.dict(exclude_unset=True, exclude={"equipments", "room"}))
        # reservation.equipments=equipments

        total_equipments = []

        for id in equipments:

            equipment_objects = db_session.query(EquipmentModel).filter(
                EquipmentModel.id == id).first()

            if not equipment_objects:
                raise HTTPException(
                    status_code=404,
                    detail='No se ha encontrado un equipo con el id proporcionado'
                )

            total_equipments.append(equipment_objects)

        reservation.equipments = total_equipments

        db_session.add(reservation)
        db_session.commit()
        
        return {"msg": f"Se han creado la reservación exitosamente"}

    def delete_reservation_by_id(id, db_session):
        reservation = db_session.query(ReservationModel).filter(
            ReservationModel.id == id).first()

        if reservation:
            db_session.delete(reservation)
            db_session.commit()
            return {"msg": "Reserva eliminada correctamente"}
        else:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado una reserva con el id proporcionado'
            )

    