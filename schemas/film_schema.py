from extensions import mash
from models.film import Film

#schema acts as translator between database model and json
#1-SQLAlchemyAutoSchema: maps fields from model
#2-rental_count: custom field added for top films query

class BaseFilmSchema(mash.SQLAlchemyAutoSchema):

    class Meta:
        model=Film #we dont need to repeat all  film column names
        load_instance=True #help when json -> model(post)
    rental_count=mash.Integer(dump_only=True) #dump_only: ont with get?


class FilmSearchSchema(BaseFilmSchema):
    actors=mash.Nested('BaseActorSchema', many=True, only=("first_name", "last_name"))
    categories=mash.Nested('BaseCategorySchema', many=True, only=("name",))


#Used in service:
#worker obj for one film
film_schema=BaseFilmSchema()

#worker obj for multiple films
films_schema=BaseFilmSchema(many=True)


films_search_schema=FilmSearchSchema(many=True)

