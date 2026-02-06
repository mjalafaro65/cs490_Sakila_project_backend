from extensions import db
from sqlalchemy_serializer import SerializerMixin

class Film(db.Model, SerializerMixin):
    __tablename__ = 'film'

    film_id = db.Column(db.SMALLINT(unsigned=True), primary_key=True)
    title = db.Column(db.VARCHAR(128), nullable=False)
    description = db.Column(db.Text)
    release_year = db.Column(db.YEAR)
    language_id = db.Column(db.TINYINT(unsigned=True), nullable=False)
    original_language_id = db.Column(db.TINYINT(unsigned=True))
    rental_duration = db.Column(db.TINYINT(unsigned=True), nullable=False)
    rental_rate = db.Column(db.DECIMAL(4,2), nullable=False)
    length = db.Column(db.SMALLINT(unsigned=True), nullable=False)
    replacement_cost = db.Column(db.DECIMAL(5,2), nullable=False)
    rating = db.Column(db.ENUM('G','PG','PG-13','R','NC-17'))

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
 