from extensions import db
from sqlalchemy import func

class Country(db.Model):
    __tablename__="country"

    country_id=db.Column(db.Integer, primary_key=True)
    country=db.Column(db.String(50), nullable=False)
    last_update=db.Column(db.DateTime,default=func.now(), onupdate=func.now(), nullable=False)
    
    #cities=db.relationship("City", backref="country_info", lazy=True)