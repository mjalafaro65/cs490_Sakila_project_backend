from extensions import db
from models.customers import Customers
from schemas.customer_schema import customers_schema

def list_cust(page=1, per_page=12):
    pagination = Customers.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    customers = pagination.items

    data = [
        {
            "customer_id": c.customer_id,
            "first_name": c.first_name,
            "last_name": c.last_name,
            "email": c.email,
            "active": c.active
        }
        for c in customers
    ]
    
    return {
        "items": data,
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page
    }

    return list_cust(page, per_page), 200



       # gets all customers
       #result= db.session.query(
              #Customers.customer_id,
              #Customers.first_name,
              #Customers.last_name, 
              #Customers.email
       #)\
       #.join(Address, Customers.customer_id==Address.address_id)\
       #.join(Store,Customers.customer_id==Store.store_id)\
       #.all()
      
       #dump converts to dictionary
       #return customers_schema.dump(result)

