from app.core.helpers.extended_enums import ExtendedEnum

V_ROLES = 1


class DefaultRoles(ExtendedEnum):
    # key =code, name

    admin = (
        "admin",
        "Administrador"
    )

    engineer = (
        "engineer",
        "Ingeniero de sonido"
    )

    client = (
        "client",
        "Cliente"
    )

    sales = (
        "sales",
        "Cajero"
    )

    def __init__(
        self,
        code,
        name
    ):
        self.code = code
        self._name = name
