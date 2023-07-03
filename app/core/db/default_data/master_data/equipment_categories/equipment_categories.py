from app.core.helpers.extended_enums import ExtendedEnum

V_EQUIPMENT_CATEGORIES = 2


class DefaultEquipmentCategories(ExtendedEnum):
    # key = name, description

    mics = (
        "Micrófonos",
        "Micrófonos"
    )

    amps = (
        "Amplificadores",
        "Amplificación"
    )

    instruments = (
        "Instrumentos",
        "Instrumentos musicales"
    )
    
    headsets = (
        "Auriculares",
        "Auriculares"
    )
    
    cabins = (
        "Cabinas",
        "Cabinas"
    )
    
    cables = (
        "Cables",
        "Cables"
    )



    def __init__(
        self,
        name,
        description
    ):
        self._name = name
        self.description = description
