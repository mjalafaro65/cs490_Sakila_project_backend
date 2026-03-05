from extensions import db
from sqlalchemy import func
from geoalchemy2 import Geometry
class Address(db.Model):
    __tablename__="address"

    address_id=db.Column(db.Integer, primary_key=True)
    address=db.Column(db.String(50), nullable=False)
    address2=db.Column(db.String(50), nullable=True)
    district=db.Column(db.String(20), nullable=False)
    city_id=db.Column(db.Integer, db.ForeignKey("city.city_id"), nullable=False)
    postal_code=db.Column(db.String(10), nullable=True)
    phone=db.Column(db.String(20),nullable=False)
    location=db.Column(Geometry(geometry_type='POINT',srid=0),nullable=False, default=func.ST_GeomFromText('POINT(0 0)', 0))
    last_update=db.Column(db.DateTime, default=func.now(), onupdate=func.now())

    city_country=db.relationship("City", backref="addresses", lazy="joined")
