from app.core.db.session import SessionLocal

from app.core.db.default_data.scripts.equipment_categories.equipment_categories import import_equipment_categories
from app.core.db.default_data.scripts.room_categories.room_categories import import_room_categories


def import_bulk_default_data():
    print("Importing bulk default data")
    try:
        db_session = SessionLocal()
        import_equipment_categories(db_session)
        import_room_categories(db_session)

        db_session.commit()
    except Exception as e:
        raise e
    finally:
        db_session.close()