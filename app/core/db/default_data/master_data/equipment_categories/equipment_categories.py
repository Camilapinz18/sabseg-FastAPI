from app.core.helpers.extended_enums import ExtendedEnum

V_EQUIPMENT_CATEGORIES = 1


class DefaultEquipmentCategories(ExtendedEnum):
    # key = name, description

    cash = (
        "Micrófonos",
        "Micrófonos"
    )

    transfer = (
        "Amplificadores",
        "Amplificación"
    )

    credit_card = (
        "Instrumentos",
        "Instrumentos musicales"
    )

    """
     With this definition we can access internal properties of enum,
     example:
     print(DefaultAccessSources.employe.code)
     console expected: AS0003
     Note: _name with undescore because name is a Enum reserved word
    """

    def __init__(
        self,
        name,
        description
    ):
        self._name = name
        self.description = description
