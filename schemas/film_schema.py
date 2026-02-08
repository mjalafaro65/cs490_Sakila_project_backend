from extensions import mash
from models.film import Film

class BaseFilmSchema(mash.SQLAlchemyAutoSchema):
    class Meta:
        model=Film
        load_instance=True #help when json to model(post)
    rental_count=mash.Integer(dump_only=True)


film_schema=BaseFilmSchema()
films_schema=BaseFilmSchema(many=True)

