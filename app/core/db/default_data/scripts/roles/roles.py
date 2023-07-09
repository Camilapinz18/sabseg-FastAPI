from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import func

from app.core.models.default_data_version import DefaultDataVersion
from app.core.auth.models.roles import Roles
from app.core.db.default_data.master_data.roles.roles import V_ROLES, DefaultRoles

def import_roles(db_session):

    is_firts_time = False
    tablename = Roles.__tablename__
    # Gets the current version of the stored data
    default_data_version = db_session.query(DefaultDataVersion).filter(
        DefaultDataVersion.name == tablename
    ).first()

    # Verify if not exists stored data
    if default_data_version is None:

        is_firts_time = True

        default_data_version = DefaultDataVersion(
            name=tablename,
            version=V_ROLES
        )

        # adds the new data version to DB
        db_session.add(default_data_version)

    # Verify if the data is newer
    # Verify if the data is newer
    if V_ROLES > default_data_version.version or is_firts_time:
        # Update the version
        default_data_version.version = V_ROLES

        last_id = db_session.query(func.max(Roles.id)).scalar() or 0

        items = []
        for item in DefaultRoles.list():
            code, _name = item
            last_id += 1  # Increment the last ID
            items.append(
                {
                    "id": last_id,
                    "code": code,
                    "name": _name
                }
            )

        # Generate an update or insert (UPSERT) query
        insert_stmt = insert(Roles).values(items)
        do_update_stmt = insert_stmt.on_conflict_do_update(
            # If unique constraint violation ("code") ...
            index_elements=[Roles.code],
            # ... Update the name
            set_={
                "name": insert_stmt.excluded.name,
                "code": insert_stmt.excluded.code,
            }
        )
        db_session.execute(do_update_stmt)
