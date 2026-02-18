
from extensions import db
from models.film import Film
from models.actor import Actor
from sqlalchemy import func
from schemas.actor_schema import actors_schema, actor_schema, actor_top_films_schema
from services.film_service import top5_films
from app import db

def top5_actors():
    #sql query gets top 5 films
    result= db.session.query(
        Actor.actor_id,
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

#gets films of one actor
def actor_details(id):
        
       #sql query gets one actor
       result= Actor.query.get(id)


       if not result:
              return {"message": "Actor not found"}, 404
       
       #dump: converts to dictionary
       data = actor_schema.dump(result)
       data["top_5_films"]=top5_films(actor_id=id)
       
       # possible fix: remove list of all films

       return data


def actor_top_films(actor_id, limit=5):
    actor = db.session.get(Actor, actor_id)
    if not actor:
        return None 

    top_film = (
        db.session.query(Film)
        .join(Film.actors) 
        .filter(Actor.actor_id == actor_id)
        #.order_by(Film.rental_count.desc()) 
        .limit(limit)
        .all()
    )

    actor.films = top_film

    return actor


#go to film_resource
