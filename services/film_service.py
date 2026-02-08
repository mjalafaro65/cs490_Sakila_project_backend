
from extensions import db
from models.film import Film
from models.rental import Rental
from models.inventory import Inventory
from sqlalchemy import func
from schemas.film_schema import films_schema, film_schema

def top_films():
       #sql query which gets top 5 films
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
      
       #dump converts to dictionary
       return films_schema.dump(result)

def one_film(id):
       #sql query which gets one film
       result= Film.query.get(id)

       if not result:
              return {"message": "Film not found"}, 404

       #dump: converts to dictionary
       return film_schema.dump(result)

       


#go to film_resource
