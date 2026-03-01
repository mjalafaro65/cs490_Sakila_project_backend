from extensions import db
from models.associations import film_category

class Category(db.Model):

    __tablename__="category"
    category_id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(25),nullable=False)
    
    films=db.relationship('Film', secondary=film_category, backref='categories')

