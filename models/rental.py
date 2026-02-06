
from datetime import datetime
from extensions import db
from sqlalchemy_serializer import SerializerMixin

#represents columns in rental table in database
class Rental(db.model, SerializerMixin):
    __tablename__="rental"

    rental_id=db.Column(db.Integer, primary_key=True)
    rental_date=db.Column(db.DateTime, nullable=False)
    inventory_id=db.Column(db.Integer, nullable=False)
    customer_id=db.Column(db.Integer, nullable=False)
    return_date=db.Column(db.DateTime, nullable=True)
    staff_id=db.Column(db.Integer, nullable=False)

