from extensions import db

film_actor=db.Table('film_actor',
    db.Column('actor_id',db.Integer,db.ForeignKey('actor.actor_id'),primary_key=True),
    db.Column('film_id',db.Integer,db.ForeignKey('film.film_id'), primary_key=True)
)