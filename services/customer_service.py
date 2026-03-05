
from schemas import customer_list_schema
from models.customer import Customer
from models.rental import Rental
from models.inventory import Inventory
from models.film import Film
from models.address import Address
from models.country import Country
from models.city import City
from extensions import db
from sqlalchemy import select, func
from services.addrss_city_country_service import get_or_create_country, get_or_create_city, get_or_create_address, get_address_by_id, get_city_by_id, get_country_by_if





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


def get_customer_by_email(email):
       return db.session.execute(select(Customer).where(Customer.email==email)).scalar()

def get_customer_by_id(id):
    stmt = (
        select(Customer)
        
        .where(Customer.customer_id == id)
    )
    return db.session.execute(stmt).scalar()



def create_customer_record(data):

       country=get_or_create_country(data.get('country'))
       city=get_or_create_city(data.get('city'), country.country_id)
       address=get_or_create_address(data, city.city_id)

       customer_obj=Customer(
              last_name=data.get('last_name'),
              first_name=data.get('first_name'),
              email=data.get('email'),
              address_id=address.address_id      
       )

       db.session.add(customer_obj)
       db.session.commit()
       return customer_obj

#check for customer address changes
def save_customer(data, customer_obj):

       #get or create address if
       country_obj=get_or_create_country(data.get('country'))
       city_obj=get_or_create_city(data.get('city'), country_obj.country_id)
       address_obj=get_or_create_address(data, city_obj.city_id)

       #change to new created address id and replace it in object
       if customer_obj != address_obj.address_id :
                customer_obj.address_id=address_obj.address_id


       db.session.commit()
       
       #return updated customer object
       return customer_obj
       
def delete_customer(customer_obj):
       #delete customer locally
       db.session.delete(customer_obj)
       #commit deletion
       db.session.commit()
       
       return

def get_rental_details_customer(customer_obj):

       id=customer_obj.customer_id

       #get address id and obj
       addr_id=customer_obj.address_id
       addr_obj=get_address_by_id(addr_id)

       #get city id and obj
       city_id=addr_obj.city_id
       city_obj=get_city_by_id(city_id)

       #get country id and obj
       country_id=city_obj.country_id
       country_obj=get_country_by_if(country_id)

       #insert addr info in customer obj
       customer_obj.address_val = addr_obj.address
       customer_obj.address2 = addr_obj.address2
       customer_obj.district = addr_obj.district
       customer_obj.postal_code = addr_obj.postal_code
       customer_obj.phone = addr_obj.phone
       customer_obj.city = city_obj.city
       customer_obj.country = country_obj.country
       
       #get total rentals
       total_count=db.session.execute(select(func.count(Rental.rental_id))\
                                .where(Rental.customer_id==id)).scalar() or 0
       
       #get active rentals
       active_count=db.session.execute(select(func.count(Rental.rental_id))\
                                 .where(Rental.customer_id==id, Rental.return_date==None)).scalar() or 0
       
       #insert active rentals to objects
       customer_obj.active_count=active_count
       customer_obj.returned_count=total_count-active_count

       stmt = (
              select(Film.title, Film.film_id)
              .join(Inventory, Film.film_id == Inventory.film_id)
              .join(Rental, Inventory.inventory_id == Rental.inventory_id)
              .where(Rental.customer_id == id)
       )
       results = db.session.execute(stmt).mappings().all()
       
       #attach to customer obj
       customer_obj.rented_films = results



       return customer_obj


def return_film_by_id(customer_id, film_id):
       stmt=select(Rental)\
       .join(Inventory, Rental.inventory_id==Inventory.inventory_id)\
       .where(Rental.customer_id==customer_id,
              Inventory.film_id==film_id,
              Rental.return_date==None)
       
       rental=db.session.execute(stmt).scalar_one_or_none()

       if not rental:
              return None
       
       rental.return_date=func.now()
       
       db.session.commit()

       return rental



