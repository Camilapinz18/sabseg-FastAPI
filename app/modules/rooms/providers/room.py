from fastapi import HTTPException
from sqlalchemy import func, distinct

# models:
from app.modules.rooms.models.room import Room as RoomModel


class Room():
    def create_room(room, db_session):
        created = RoomModel(**room.dict())
        db_session.add(created)
        
        db_session.commit()
        
        return {"msg": f"Se han creado la sala exitosamente"}

    def get_rooms(db_session):
        rooms = db_session.query(RoomModel).all()

        return rooms
    

    def get_room_by_id(id, db_session):
        room = db_session.query(RoomModel).filter(RoomModel.id == id).first()

        if not room:
            raise HTTPException(
                status_code=404,
                detail='No se ha encontrado una sala con el id proporcionado'
            )

        return room

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