
from extensions import db
from models.film import Film
from models.rental import Rental
from models.inventory import Inventory
from sqlalchemy import func
from schemas.film_schema import films_schema

def top_films():

       result= db.session.query(
              Film.title,
              func.count(Rental.rental_id).label("rental_count")
       )\
       .join(Inventory, Film.film_id==Inventory.film_id)\
       .join(Rental,Inventory.inventory_id==Rental.inventory_id)\
       .group_by(Film.film_id)\
       .order_by(func.count(Rental.rental_id).desc())\
       .limit(5)\
       .all()
       print(result)
       print(films_schema.dump(result))
       return films_schema.dump(result)
