from extensions import mash 
from models.category import Category

class BaseCategorySchema(mash.SQLAlchemyAutoSchema):
    class Meta:
        model=Category
        load_instance=True



category_schema=BaseCategorySchema()

