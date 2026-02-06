from flask import Flask
from flask_restful import Api 
from config import Config 
from extensions import db
from flask_restful import Resource


app=Flask(__name__)

api=Api(app)
app.config.from_object(Config)

db.init_app(app)
api.init_app(app)


class FilmResource(Resource):
    def get(self):
        return {"message": "List of films"}


api.add_resource(FilmResource, "/")
if __name__=="__main__":
    app.run(debug=True)


