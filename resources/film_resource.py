from flask_restful import Resource

from services.movie_service import get_top_movies
class TopMovies(Resource):
    def get (self):
            return get_top_movies(), 200
