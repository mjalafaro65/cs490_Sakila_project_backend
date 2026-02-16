from extensions import mash 
from models.customers import Customers

class BaseCustomerSchema(mash.SQLAlchemyAutoSchema):
    class Meta:
        model=Customers
        load_instance=True



customers_schema=BaseCustomerSchema()

