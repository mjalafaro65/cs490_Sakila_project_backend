from extensions import db

class Address(db.Model):
    __tablename__ = 'address'

    address_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50), nullable=False)
    address2 = db.Column(db.String(50))
    district = db.Column(db.String(20), nullable=False)
    city_id = db.Column(db.Integer, nullable=False)
    postal_code = db.Column(db.String(10))
    phone = db.Column(db.String(20), nullable=False)
    # didn't include location (geometry) and last_update columns here
