from flask_restful import Resource, request
from services.film_service import top_films, one_film, search_films


class TopFilms(Resource):
    def get (self):
            
            #Flask_Restful converts returned dic from top_films into json
            return top_films(), 200
    
class FilmDetails(Resource):
    #id: obtained from url 
    def get(self,id):
          return one_film(id), 200
    

class SearchedFilmsResults(Resource):
    def get(self):

        search_for=request.args.get('s', '').strip()
        search_by=request.args.get('by', '')


        if not search_for:
            return {'message', "provide a search input"}

        return search_films(search_for, search_by), 200
    

         

#go to app: api.resource()
