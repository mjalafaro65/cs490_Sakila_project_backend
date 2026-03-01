from extensions import db
from sqlalchemy import func

class City(db.Model):
    __tablename__="city"

    city_id=db.Column(db.Integer, primary_key=True)
    city=db.Column(db.String(50), nullable=False)
    country_id=db.Column(db.Integer, db.ForeignKey("country.country_id"),nullable=False)
    last_update=db.Column(db.DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    
    addresses=db.relationship("Address",backref="city_info", lazy=True)