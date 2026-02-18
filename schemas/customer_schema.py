from extensions import mash
from models.customer import Customer

#schema acts as translator between database model and json
#1-SQLAlchemyAutoSchema: maps fields from model

class BaseCustomerSchema(mash.SQLAlchemyAutoSchema):

    class Meta:
        model=Customer #we dont need to repeat all  film column names
        load_instance=True #help when json -> model(post)


customer_list_schema=BaseCustomerSchema(many=True)

