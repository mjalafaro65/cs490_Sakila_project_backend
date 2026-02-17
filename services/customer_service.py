
from schemas import costumer_list_schema
from models.customer import Customer

def all_customers_paginated(page=1,per_page=15):
    pagination=Customer.query.order_by(Customer.first_name.asc()).paginate(
            page=page,
            per_page=per_page,
            error_out=False
    ) 


    
    return {
        "items":costumer_list_schema.dump(pagination.items),
        "total":pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.per_page,
        "has_prev":pagination.has_prev,
        "has_next": pagination.has_next
    }

