from extensions import mash
from models.rental import Rental
from marshmallow import fields
class BaseRentalSchema(mash.SQLAlchemyAutoSchema):
    class Meta:
        model=Rental
        load_instance=True #used for post: returns model object ready to send to database
        include_fk=True # it will provide(also needed when post) foreign key instead of the whole foreign model object

    ##this will only work with get, prevents user from sending/posting these
    dump_only=("rental_id", "rental_date", "return_date", "last_update", "staff_id")

    inventory_id=fields.Int(required=True)
    customer_id=fields.Int(required=True)


rental_schema=BaseRentalSchema()