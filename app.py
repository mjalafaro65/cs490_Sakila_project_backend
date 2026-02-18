from flask import Flask
from flask_restful import Api 
from flask_cors import CORS
from config import Config 
from extensions import db
from flask_restful import Resource
from resources.film_resource import TopFilms, FilmDetails, SearchedFilmsResults
from resources.actor_resource import Top5Actors, ActorWithFilms, ActorTopFilms
from resources.customer_resourse import CustomerList


app=Flask(__name__)

api=Api(app)
app.config.from_object(Config)

db.init_app(app)
CORS(app)
api.init_app(app)


class Hello(Resource):
    
    def get(self):
        return {"message": "hello"}


api.add_resource(Hello, "/")
api.add_resource(TopFilms, "/films/top")
api.add_resource(FilmDetails, "/films/<int:id>")
api.add_resource(Top5Actors, "/actors/top")
api.add_resource(ActorWithFilms, "/actors/<int:id>")
api.add_resource(ActorTopFilms, "/actors/top/<int:id>")
api.add_resource(SearchedFilmsResults, "/films/search")
api.add_resource(CustomerList, "/customers/list")


if __name__=="__main__":
    app.run(debug=True)


