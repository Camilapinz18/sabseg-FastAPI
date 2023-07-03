from app.core.helpers.extended_enums import ExtendedEnum

V_RESERVATION_TYPE = 1


class DefaultReservationType(ExtendedEnum):
    # key = name, description

    recording = (
        "Grabación",
        "Grabación"
    )

    rehersal = (
        "Ensayo",
        "Ensayo"
    )

    rental = (
        "Alquiler",
        "Alquiler musicales"
    )
    
    

    def __init__(
        self,
        name,
        description
    ):
        self._name = name
        self.description = description
