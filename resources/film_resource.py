from flask_restful import Resource, request
from services.film_service import top5_films, one_film, search_films


class TopFilms(Resource):
    def get (self):
            
            #Flask_Restful converts returned dic from top_films into json
            return top5_films(), 200
    
class FilmDetails(Resource):
    #id: obtained from url 
    def get(self,id):
          
        if not str(id).isdigit():
            return {"message": "Invalid ID: Film ID must be positive integer"}, 400
           
        return one_film(id), 200
    

class SearchedFilmsResults(Resource):
    def get(self):

        #?s=...&by=... <=gets args from here
        search_for=request.args.get('s', '').strip()
        search_by=request.args.get('by', '')

        if not search_for:
            return {"message":"Please provide input"}
                
        valid_types=['title', 'actor', 'genre']
                
        if search_by not in valid_types:
            return {"message": f"Invalid search type must be one of: {','.join(valid_types)}"}, 400

        return search_films(search_for, search_by), 200
    

         

#go to app: api.resource()
