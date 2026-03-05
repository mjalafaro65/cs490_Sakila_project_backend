from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from geoalchemy2.shape import to_shape
from models.country import Country
from models.city import City
from models.address import Address

class BaseCountrySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Country
        load_instance = True


class BaseCitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model=City
        load_instance = True

    country=fields.Nested(BaseCountrySchema)


class BaseAddressSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=Address
        load_instance = True
        exclude = ("location",)

    city_country=fields.Nested(BaseCitySchema)

    city = fields.String(attribute="city_country.city")  
    country = fields.String(attribute="city_country.country")  


    
