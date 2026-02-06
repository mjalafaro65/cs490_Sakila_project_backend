from flask import  jsonify
from models.film import Film

def get_top_movies(limit=5):
 
       films = Film.query.limit(5).all()
       return [film.to_dict() for film in films]