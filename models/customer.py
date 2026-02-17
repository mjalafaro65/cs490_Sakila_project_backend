from extensions import db

class Customer(db.Model):

    __table_name__="customer"
    customer_id=db.Column(db.Integer, primary_key=True)
    store_id=db.Column(db.Integer, nullable=False)
    last_name=db.Column(db.String(45),nullable=False)
    first_name=db.Column(db.String(45),nullable=False)
    email=db.Column(db.String(45),nullable=True)
    address_id=db.Column(db.Integer,nullable=False)
    active=db.Column(db.Integer, nullable=False)

    



