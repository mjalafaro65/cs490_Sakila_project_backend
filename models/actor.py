from extensions import db 
from models.associations import film_actor


class Actor(db.Model):
    __tablename__="actor"

    actor_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)

    #goes to film_actor table and look for film_ids with this actor id and  returns list of films                                       
    films=db.relationship('Film',secondary=film_actor, backref='actors') #backref: Film model will also keep track of actors

    