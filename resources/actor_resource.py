from flask_restful import Resource
from services.actor_service import top_actors, actor_films


class TopActors(Resource):
    def get (self):
            #Flask_Restful converts returned dic from top_films into json
            return top_actors(), 200
    
    
class ActorWithFilms(Resource):
     #id: obtained from url 
     def get(self,id):
        return actor_films(id), 200
    
#     #go to app: api.resource()
