from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import func

from app.core.models.default_data_version import DefaultDataVersion
from app.modules.users.models.user import User
from app.core.db.default_data.master_data.users.users import V_USERS, DefaultUsers

def import_users(db_session):

    is_firts_time = False
    tablename = User.__tablename__
    # Gets the current version of the stored data
    default_data_version = db_session.query(DefaultDataVersion).filter(
        DefaultDataVersion.name == tablename
    ).first()

    # Verify if not exists stored data
    if default_data_version is None:

        is_firts_time = True

        default_data_version = DefaultDataVersion(
            name=tablename,
            version=V_USERS
        )

        # adds the new data version to DB
        db_session.add(default_data_version)

    # Verify if the data is newer
    # Verify if the data is newer
    if V_USERS > default_data_version.version or is_firts_time:
        # Update the version
        default_data_version.version = V_USERS

        last_id = db_session.query(func.max(User.id)).scalar() or 0

        items = []
        for item in DefaultUsers.list():
            email,password,attendance, _name,surname,phone,role = item
            last_id += 1  # Increment the last ID
            items.append(
                {
                    "id": last_id,
                    "email": email,
                    "password":password,
                    "attendance":attendance,
                    "name": _name,
                    "surname":surname,
                    "phone":phone,
                    "role":role
                }
            )

        # Generate an update or insert (UPSERT) query
        insert_stmt = insert(User).values(items)
        do_update_stmt = insert_stmt.on_conflict_do_update(
            # If unique constraint violation ("code") ...
            index_elements=[User.id],
            # ... Update the name
            set_={
                "email": insert_stmt.excluded.email,
                "password": insert_stmt.excluded.password,
                "attendance": insert_stmt.excluded.attendance,
                "name": insert_stmt.excluded.name,
                "surname": insert_stmt.excluded.surname,
                "phone": insert_stmt.excluded.phone,
                "role": insert_stmt.excluded.role,
            }
        )
        db_session.execute(do_update_stmt)
