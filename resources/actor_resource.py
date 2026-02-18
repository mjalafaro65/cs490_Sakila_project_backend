from flask_restful import Resource
from services.actor_service import top5_actors, actor_details, actor_top_films
from schemas import actor_top_films_schema



class Top5Actors(Resource):
    def get (self):
            #Flask_Restful converts returned dic from top_films into json
            return top5_actors(), 200
    
    
class ActorWithFilms(Resource):
     #id: obtained from url 
     def get(self,id):

        if not str(id).isdigit():
            return {"message": "Invalid ID: Actor ID must be positive integer"}, 400
        
        return actor_details(id), 200
     
class ActorTopFilms(Resource):
    def get(self, id):
        actor = actor_top_films(id)

        if not actor:
            return {"message": "Actor not found"}, 404

        return actor_top_films_schema.dump(actor), 200

    
#     #go to app: api.resource()
