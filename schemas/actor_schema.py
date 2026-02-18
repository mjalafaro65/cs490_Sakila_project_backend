from extensions import mash 
from models.actor import Actor

class BaseActorSchema(mash.SQLAlchemyAutoSchema):
    class Meta:
        model=Actor
        load_instance=True

    film_count=mash.Integer(dump_only=True)

class ActorFilmsSchema(BaseActorSchema):

    films=mash.Nested('BaseFilmSchema', many=True,only=("title",) )

class ActorTopFilms(BaseActorSchema):
    films = mash.Nested(
        'BaseFilmSchema',
        many=True,
        only=("film_id", "title")
    )

actors_schema=BaseActorSchema(many=True)
actor_schema=ActorFilmsSchema()
actor_top_films_schema = ActorTopFilms()

