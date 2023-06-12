import re
from sqlalchemy.ext.declarative import declarative_base, as_declarative, declared_attr
from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean
from sqlalchemy import func
from sqlalchemy import cast
from sqlalchemy import extract
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    __name__: str
    __models__ = []
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    @hybrid_property
    def created_at_year(self):
        return func.extract('year', self.created_at)

    @hybrid_property
    def created_at_month(self):
        return func.extract('month',  self.created_at)

    @hybrid_property
    def created_at_day(self):
        return func.extract('day',  self.created_at)

    @hybrid_property
    def updated_at_year(self):
        return func.extract('year', self.updated_at)

    @hybrid_property
    def updated_at_month(self):
        return func.extract('month',  self.updated_at)

    @hybrid_property
    def updated_at_day(self):
        return func.extract('day',  self.updated_at)

    def __init_subclass__(cls, **kwargs):

        child_class = cls
        child_class_name = child_class().__class__.__name__.lower()

        if child_class_name != 'base':
            cls.__models__.append(child_class)

        # Iterate through the columns of the class

        attrs_copy = child_class.__dict__.copy()
        for attr_name, attr_value in attrs_copy.items():

            # If the attribute is a DateTime column, generate a function for it
            if isinstance(attr_value, Column) and (
                isinstance(attr_value.type, Date) or isinstance(
                    attr_value.type, DateTime)
            ):
                cls.add_datetime_functions(attr_name)

            super().__init_subclass__(**kwargs)

    @classmethod
    def add_datetime_functions(cls, attr_name):

        def get_year(self):
            return func.extract('year', getattr(self, attr_name))

        def get_month(self):
            return func.extract('month', getattr(self, attr_name))

        def get_day(self):
            return func.extract('day', getattr(self, attr_name))

        # Add the functions to the class
        function_name_year = f"{attr_name}_year"
        setattr(cls, function_name_year, hybrid_property(get_year))
        function_name_month = f"{attr_name}_month"
        setattr(cls, function_name_month, hybrid_property(get_month))
        function_name_day = f"{attr_name}_day"
        setattr(cls, function_name_day, hybrid_property(get_day))
