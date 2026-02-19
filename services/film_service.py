
from extensions import db
from sqlalchemy import or_
from models.film import Film
from models.rental import Rental
from models.inventory import Inventory
from models.actor import Actor
from sqlalchemy import func
from schemas import films_schema, film_schema, films_search_schema
from models.associations import film_actor
from models.category import Category

def top5_films(actor_id=None):
       #sql query gets top 5 films
       query= db.session.query(
              Film.film_id,
              Film.title,
              func.count(Rental.rental_id).label("rental_count")
       )\
       .join(Inventory, Film.film_id==Inventory.film_id)\
       .join(Rental,Inventory.inventory_id==Rental.inventory_id)
       
       if actor_id:
              query= query.join(film_actor, Film.film_id== film_actor.c.film_id)\
                     .filter(film_actor.c.actor_id== actor_id)

       result=query.group_by(Film.film_id)\
       .order_by(func.count(Rental.rental_id).desc(), Film.title.asc())\
       .limit(5)\
       .all()
      

       #dump converts to dictionary
       return films_schema.dump(result)


def one_film(id):
       #sql query gets one film

       result= Film.query.get(id)

       if not result:
              return {"message": "Film not found"}, 404

       #dump: converts to dictionary
       return film_schema.dump(result)


def search_films(srch_str,srch_by, page=1, per_page=10):

       #clean white spaces and reduce middle ones to one
       cleaned=" ".join(srch_str.split())
       search_pattern=f"%{cleaned}%"

       
       query=Film.query
              
       if srch_by =="title":
              query=query.filter(Film.title.ilike(search_pattern))

              

       elif srch_by == "actor":
              query= query.join(Film.actors).filter(
               or_(Actor.first_name.ilike(search_pattern),
                                   Actor.last_name.ilike(search_pattern),
                                   func.concat(Actor.first_name, " ", Actor.last_name).ilike(search_pattern)

                                   ))
              

       elif srch_by == "genre":
              query = query.join(Film.categories).filter(
        Category.name.ilike(search_pattern)
    )

       else:
              return {"message": "Film not found"}, 404 
       
       query = query.distinct()

       pagination = query.paginate(page=page, per_page=per_page, error_out=False)

       return {
              "items": films_search_schema.dump(pagination.items),
              "page": pagination.page,
              "pages": pagination.pages,
              "total": pagination.total
       }




#go to film_resource
