from extensions import db
from models.rental import Rental

def create_rent_record(rental_obj):
    #unpacking->inserts items into model object

    db.session.add(rental_obj)
    db.session.commit()

    return rental_obj