
from schemas import customer_list_schema
from models.customer import Customer

def all_customers_paginated(page=1,per_page=15):
    pagination=Customer.query.order_by(Customer.first_name.asc()).paginate(
            page=page,
            per_page=per_page,
            error_out=False
    ) 
 

    
    return {
        "items":customer_list_schema.dump(pagination.items),
        "total":pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page,
        "has_prev":pagination.has_prev,
        "has_next": pagination.has_next
    }



def search_customers(srch_str,srch_by, page=1, per_page=10):

       #clean white spaces and reduce middle ones to one
       cleaned=" ".join(srch_str.split())
       search_pattern=f"%{cleaned}%"

       
       query=Customer.query
              
       if srch_by =="customer_id":
              query=query.filter(Customer.customer_id.ilike(search_pattern))

       elif srch_by == "first_name":
              query= query.filter(Customer.first_name.ilike(search_pattern))
              

       elif srch_by == "last_name":
              query = query.filter(Customer.last_name.ilike(search_pattern))

       else:
              return {"message": "Film not found"}, 404 
       
       query = query.distinct()

       pagination = query.paginate(page=page, per_page=per_page, error_out=False)

       return {
              "items": customer_list_schema.dump(pagination.items),
              "page": pagination.page,
              "pages": pagination.pages,
              "total": pagination.total
       }
