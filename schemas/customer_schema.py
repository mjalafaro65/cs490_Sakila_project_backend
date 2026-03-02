from extensions import mash
from models.customer import Customer
from marshmallow import fields, EXCLUDE

#schema acts as translator between database model and json
#1-SQLAlchemyAutoSchema: maps fields from model

class BaseCustomerSchema(mash.SQLAlchemyAutoSchema):

    class Meta:
        model=Customer #we dont need to repeat all  film column names
        load_instance=True #help when json -> model/object
    
class AddressCostumerSchema(BaseCustomerSchema):
    #so extra address dont get mapped to Customer attributes
    #check json matches with fields and  returns a dictionary
    class Meta(BaseCustomerSchema.Meta):
        load_instance=False

    address=fields.Str(required=True)
    address2=fields.Str(allow_none=True)
    district=fields.Str(required=True)
    city=fields.Str(required=True)
    country=fields.Str(required=True)
    postal_code=fields.Str(required=True)
    phone=fields.Str(required=True)

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


