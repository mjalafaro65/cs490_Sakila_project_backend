
from extensions import db
from models.film import Film
from models.actor import Actor
from sqlalchemy import func
from schemas.actor_schema import actors_schema, actor_schema

def top_actors():
    #sql query gets top 5 films
    result= db.session.query(
        Actor.first_name,
        Actor.last_name,
        func.count(Film.film_id).label("films")
       )\
       .join(Actor.films)\
       .group_by(Actor.actor_id)\
       .order_by(func.count(Film.film_id).desc())\
       .limit(5)\
       .all()
      
       #dump converts to dictionary
    return actors_schema.dump(result)

def actor_films(id):
        
       #sql query gets one film
       result= Actor.query.get(id)

       if not result:
              return {"message": "Film not found"}, 404

       #dump: converts to dictionary
       return actor_schema.dump(result)

# group by fc.film_id , fc.name
# order by COUNT(i.inventory_id) desc  
# limit 5;

#go to film_resource
