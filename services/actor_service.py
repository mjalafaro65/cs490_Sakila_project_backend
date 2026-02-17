
from extensions import db
from models.film import Film
from models.actor import Actor
from sqlalchemy import func
from schemas.actor_schema import actors_schema, actor_schema
from services.film_service import top5_films

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
   

       return data



#go to film_resource
