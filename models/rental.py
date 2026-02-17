from extensions import db

#represents columns in rental table in database
class Rental(db.Model):
    __tablename__="rental"

    rental_id=db.Column(db.Integer, primary_key=True)
    rental_date=db.Column(db.DateTime, nullable=False)
    inventory_id=db.Column(db.Integer, db.ForeignKey("inventory.inventory_id") ,nullable=False)
    customer_id=db.Column(db.Integer,db.ForeignKey("customer.customer_id"),  nullable=False)
    return_date=db.Column(db.DateTime, nullable=True)
    staff_id=db.Column(db.Integer, nullable=False)

