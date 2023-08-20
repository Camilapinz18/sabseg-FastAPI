from app.core.helpers.extended_enums import ExtendedEnum

V_USERS = 1


class DefaultUsers(ExtendedEnum):
    # key =code, name

    admin = (
        "admin_oldskull@gmail.com",
        "$2b$12$Cpd4htIT3z5Kx4ZTCnJsEe0wQ51IFsIB4Qrl8kveRvY7koKV5Txy.",
        0,
        "Administrador",
        "OldSkull",
        "3015106397",
        "admin"
    )

   
    def __init__(
        self,
        email,
        password,
        attendance,
        name,
        surname,
        phone,
        role
    ):
        self.email = email
        self.password=password
        self.attendance=attendance
        self._name = name
        self.surname=surname
        self.phone=phone
        self.role=role
