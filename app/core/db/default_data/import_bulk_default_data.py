from app.core.db.session import SessionLocal

from app.core.db.default_data.scripts.equipment_categories.equipment_categories import import_equipment_categories
from app.core.db.default_data.scripts.room_categories.room_categories import import_room_categories
from app.core.db.default_data.scripts.reservation_type.reservation_type import import_reservation_types
from app.core.db.default_data.scripts.roles.roles import import_roles
from app.core.db.default_data.scripts.users.users import import_users


def import_bulk_default_data():
    print("Importing bulk default data")
    try:
        db_session = SessionLocal()
        import_equipment_categories(db_session)
        import_room_categories(db_session)
        import_reservation_types(db_session)
        import_roles(db_session)
        import_users(db_session)

        db_session.commit()
    except Exception as e:
        raise e
    finally:
        db_session.close()