from extensions import db

# represents columns(not all) in film table in database
#using se
class Film(db.Model):
    __tablename__ = 'film'

    #not for all columns
    film_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    release_year = db.Column(db.Integer)
    language_id = db.Column(db.Integer,nullable=False)
    original_language_id = db.Column(db.Integer)
    rental_duration = db.Column(db.Integer, nullable=False)
    rental_rate = db.Column(db.Float, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    replacement_cost = db.Column(db.Float, nullable=False)
    rating = db.Column(db.String(10))

    inventories = db.relationship("Inventory", backref="film")

    # def to_dict(self):
    #     return{

    #         "film_id": self.film_id,
    #         "title":self.title,
    #         "description":self.description,
    #         "release_year": self.release_year,
    #         "language_id" : self.language_id,
    #         "original_language_id" : self.original_language_id,
    #         "rental_duration" : self.rental_duration,
    #         "rental_rate" : self.rental_rate,
    #         "length" : self.length,
    #         "replacement_cost" : self.replacement_cost,
    #         "rating" : self.rating
            
    #     }
 