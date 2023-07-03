from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import func
from app.modules.rooms.models.room_category import RoomCategory
from app.core.models.default_data_version import DefaultDataVersion

from app.core.db.default_data.master_data.room_categories.room_categories import V_ROOM_CATEGORIES, DefaultRoomCategories

def import_room_categories(db_session):

    is_firts_time = False
    tablename = RoomCategory.__tablename__
    # Gets the current version of the stored data
    default_data_version = db_session.query(DefaultDataVersion).filter(
        DefaultDataVersion.name == tablename
    ).first()

    # Verify if not exists stored data
    if default_data_version is None:

        is_firts_time = True

        default_data_version = DefaultDataVersion(
            name=tablename,
            version=V_ROOM_CATEGORIES
        )

        # adds the new data version to DB
        db_session.add(default_data_version)

    # Verify if the data is newer
    # Verify if the data is newer
    if V_ROOM_CATEGORIES > default_data_version.version or is_firts_time:
        # Update the version
        default_data_version.version = V_ROOM_CATEGORIES

        last_id = db_session.query(func.max(RoomCategory.id)).scalar() or 0

        items = []
        for item in DefaultRoomCategories.list():
            _name, description = item
            last_id += 1  # Increment the last ID
            items.append(
                {
                    "id": last_id,
                    "name": _name,
                    "description": description
                }
            )

        # Generate an update or insert (UPSERT) query
        insert_stmt = insert(RoomCategory).values(items)
        do_update_stmt = insert_stmt.on_conflict_do_update(
            # If unique constraint violation ("code") ...
            index_elements=[RoomCategory.id],
            # ... Update the name
            set_={
                "name": insert_stmt.excluded.name,
                "description": insert_stmt.excluded.description,
            }
        )
        db_session.execute(do_update_stmt)
