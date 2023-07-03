from app.core.helpers.extended_enums import ExtendedEnum

V_ROOM_CATEGORIES = 1


class DefaultRoomCategories(ExtendedEnum):
    # key = name, description

    recording = (
        "Estudio de grabación",
        "Salas especializadas para la grabación de solistas y/o bandas musicales"
    )

    rehersal = (
        "Sala de ensayo",
        "Salas especializadas para el ensayo musical de solistas y/o bandas musicales "
    )

    def __init__(
        self,
        name,
        description
    ):
        self._name = name
        self.description = description
