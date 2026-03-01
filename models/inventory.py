from extensions import db

#represents inventory table in database
class Inventory(db.Model):
    __tablename__="inventory"
    inventory_id=db.Column(db.Integer, primary_key=True)
    film_id=db.Column(db.Integer, db.ForeignKey("film.film_id"), nullable=False)
    store_id=db.Column(db.Integer,db.ForeignKey("store.store_id"), nullable=False)


    