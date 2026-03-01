#package 

#for mash.Nested() in schema to work, all schemas should be imported somewhere. However not all schemas are imported somewhere for use  
from .film_schema import BaseFilmSchema, FilmSearchSchema
from .actor_schema import BaseActorSchema, ActorFilmsSchema, ActorTopFilms
from .category_schema import BaseCategorySchema
from .customer_schema import BaseCustomerSchema, AddressCostumerSchema
from .rental_schema import BaseRentalSchema

#Since were importing classes, we might as well import their objects to use this this package in services
from .film_schema import film_schema, films_schema, films_search_schema
from .actor_schema import actor_schema, actors_schema, actor_top_films_schema
from .category_schema import category_schema
from .customer_schema import customer_list_schema, single_customer_schema, address_customer_schema
from .rental_schema import rental_schema
