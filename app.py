from flask import Flask
from flask_restful import Api 
from flask_cors import CORS
from config import Config 
from extensions import db
from flask_restful import Resource
from resources.film_resource import TopFilms, FilmDetails, SearchedFilmsResults
from resources.actor_resource import Top5Actors, ActorWithFilms, ActorTopFilms
from resources.customer_resource import CustomerResource, OneCustomerResource
from resources.rental_resource import RentalRecords


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
#gets top 5 films
api.add_resource(TopFilms, "/films/top")

#gets details of each film
api.add_resource(FilmDetails, "/films/<int:id>")
 
# get top 5 actors
api.add_resource(Top5Actors, "/actors/top")

#gets all films of one actor
api.add_resource(ActorWithFilms, "/actors/<int:id>") #check

#gets the top films of once actor
api.add_resource(ActorTopFilms, "/actors/top/<int:id>")#check

#searches films search?s=..&by=..
api.add_resource(SearchedFilmsResults, "/films/search")


#####after learning more about end points##########

#get list of all costumers
#search customers
#post customer
api.add_resource(CustomerResource, "/customers")

api.add_resource(OneCustomerResource, "/customers/<int:id>")




#create a rental record
api.add_resource(RentalRecords, "/rentals")





if __name__=="__main__":
    app.run(debug=True)


