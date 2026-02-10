from flask import Flask
from flask_restful import Api 
from config import Config 
from extensions import db
from flask_restful import Resource
from resources.film_resource import TopFilms, FilmDetails, SearchedFilmsResults
from resources.actor_resource import TopActors, ActorWithFilms


app=Flask(__name__)

api=Api(app)
app.config.from_object(Config)

db.init_app(app)
api.init_app(app)


class Hello(Resource):
    
    def get(self):
        return {"message": "hello"}


api.add_resource(Hello, "/")
api.add_resource(TopFilms, "/films/top")
api.add_resource(FilmDetails, "/films/<int:id>")
api.add_resource(TopActors, "/actors/top")
api.add_resource(ActorWithFilms, "/actors/<int:id>")
api.add_resource(SearchedFilmsResults, "/films/search")


if __name__=="__main__":
    app.run(debug=True)


