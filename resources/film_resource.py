from flask_restful import Resource
from services.film_service import top_films

class TopMovies(Resource):
    def get (self):
            return top_films(), 200
