from extensions import db
from sqlalchemy import func

#represents columns in rental table in database
class Rental(db.Model):
    __tablename__="rental"

    rental_id=db.Column(db.Integer, primary_key=True)
    inventory_id=db.Column(db.Integer, db.ForeignKey("inventory.inventory_id") ,nullable=False)
    customer_id=db.Column(db.Integer,db.ForeignKey("customer.customer_id"),  nullable=False)

    rental_date=db.Column(db.DateTime , default=func.now(), nullable=False)
    return_date=db.Column(db.DateTime, nullable=True)
    staff_id=db.Column(db.Integer, default=1, nullable=False)
    last_update=db.Column(db.DateTime, default=func.now, onupdate=func.now(), nullable=False)


   

