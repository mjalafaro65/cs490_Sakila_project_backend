from extensions import mash
from models.customer import Customer
from marshmallow import fields, EXCLUDE
from schemas.addresses_schema import BaseAddressSchema

#schema acts as translator between database model and json
#1-SQLAlchemyAutoSchema: maps fields from model

class BaseCustomerSchema(mash.SQLAlchemyAutoSchema):

    class Meta:
        model=Customer #we dont need to repeat all  film column names
        load_instance=True #help when json -> model/object
    
    address = fields.Nested(BaseAddressSchema)
    country_name = fields.String(attribute="country.country")

class AddressCostumerSchema(BaseCustomerSchema):
    #so extra address dont get mapped to Customer attributes
    #check json matches with fields and  returns a dictionary
    class Meta(BaseCustomerSchema.Meta):
        load_instance=False

    address_id = fields.Int(attribute="address.address_id")
    address1 = fields.Str(attribute="address.address")
    address2 = fields.Str(attribute="address.address2", allow_none=True)
    district = fields.Str(attribute="address.district")
    postal_code = fields.Str(attribute="address.postal_code")
    phone = fields.Str(attribute="address.phone")
    city = fields.Str(attribute="address.city_country.city")
    country = fields.Str(attribute="address.city_country.country")

class UpdateCustomerSchema(BaseCustomerSchema):
    class Meta(BaseCustomerSchema.Meta):
        unknown=EXCLUDE
    
class RentalsCustomerSchema(BaseCustomerSchema):
    active_count=fields.Int(dump_only=True) 
    returned_count=fields.Int(dump_only=True) 


single_customer_schema=BaseCustomerSchema()
update_one_customer=UpdateCustomerSchema()
customer_list_schema=BaseCustomerSchema(many=True)
address_customer_schema=AddressCostumerSchema()
rentals_customer_schema=RentalsCustomerSchema()


