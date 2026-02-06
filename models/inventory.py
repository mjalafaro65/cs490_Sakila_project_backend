from extensions import db
from sqlalchemy_serializer import SerializerMixin

#represents inventory table in database
class Inventory(db.Model, SerializerMixin):
    __tablename__="inventory"
    inventory_id=db.Column(db.Integer, primary=True)
    film_id=db.Column(db.Integer, nullable=False)
    store_id=db.Column(db.Integer, nullable=False)


    