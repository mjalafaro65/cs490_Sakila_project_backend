from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.country import Country
from models.city import City
from models.address import Address

class BaseCountrySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Country

class BaseCitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model=City

    country=fields.Nested(BaseCountrySchema)


class BaseAddressSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Address

    city_country=fields.Nested(BaseCitySchema)

    
