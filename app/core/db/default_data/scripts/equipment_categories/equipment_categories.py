from sqlalchemy.dialects.postgresql import insert

from app.modules.equipments.models.equipment_category import EquipmentCategory
from app.core.models.default_data_version import DefaultDataVersion

from app.core.db.default_data.master_data.equipment_categories.equipment_categories import V_EQUIPMENT_CATEGORIES, DefaultEquipmentCategories

def import_equipment_categories(db_session):

    is_firts_time = False
    tablename = EquipmentCategory.__tablename__
    # Gets the current version of the stored data
    default_data_version = db_session.query(DefaultDataVersion).filter(
        DefaultDataVersion.name == tablename
    ).first()

    # Verify if not exists stored data
    if default_data_version is None:

        is_firts_time = True

        default_data_version = DefaultDataVersion(
            name=tablename,
            version=V_EQUIPMENT_CATEGORIES
        )

        # adds the new data version to DB
        db_session.add(default_data_version)

    # Verify if the data is newer
    if V_EQUIPMENT_CATEGORIES > default_data_version.version or is_firts_time:
    # Update the version
        default_data_version.version = V_EQUIPMENT_CATEGORIES

        items = []
        for item in DefaultEquipmentCategories.list():
            _name, description = item
            items.append(
                {
                    "id":1,
                    "name": _name,
                    "description": description            
                }
            )

        # Generate an update or insert (UPSERT) query
        insert_stmt = insert(EquipmentCategory).values(items)
        do_update_stmt = insert_stmt.on_conflict_do_update(
            # If unique constraint violation ("code") ...
            index_elements=[EquipmentCategory.name],
            # ... Update the name
            set_={
                "name": insert_stmt.excluded.name,
                "description": insert_stmt.excluded.description,
            }
        )
        db_session.execute(do_update_stmt)