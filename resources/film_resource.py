from flask_restful import Resource
from services.film_service import top_films, one_film


class TopMovies(Resource):
    def get (self):
            
            #Flask_Restful  converts returned dic from top_films into json
            return top_films(), 200
    
class FilmDetails(Resource):
    def get(self,id):
          return one_film(id), 200
    
    #go to app: api.resource()
