from extensions import db

class Customers(db.Model):
    __tablename__ = 'customer'

    customer_id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey("store.store_id"), nullable=False)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(50))
    address_id = db.Column(db.Integer, db.ForeignKey("address.address_id"), nullable=False)
    active = db.Column(db.Integer, nullable=False)
    # didn't include create_date and last_update columns here
