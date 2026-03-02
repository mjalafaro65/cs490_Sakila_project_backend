from extensions import db
from sqlalchemy import func

#customer table
class Customer(db.Model):

    __tablename__="customer"
    customer_id=db.Column(db.Integer, primary_key=True)
    store_id=db.Column(db.Integer, default=1, nullable=False)
    last_name=db.Column(db.String(45),nullable=False)
    first_name=db.Column(db.String(45),nullable=False)
    email=db.Column(db.String(50),nullable=True)
    address_id=db.Column(db.Integer,db.ForeignKey("address.address_id"),nullable=False)
    active=db.Column(db.Integer, default=1,nullable=False)
    create_date=db.Column(db.DateTime,default=func.now(), nullable=False)
    last_update=db.Column(db.DateTime,default=func.now(), onupdate=func.now(), nullable=True )


    rentals=db.relationship('Rental', backref='customer', cascade="all, delete-orphan")
    # payments=db.relationship('Payment', backref='customer', cascade="all, delete-orphan")


