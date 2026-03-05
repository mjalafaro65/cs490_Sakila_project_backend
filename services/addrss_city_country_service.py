from models.country import Country
from models.city import City
from models.address import Address
from models.city import City
from models.country import Country
from sqlalchemy import select
from extensions import db


#return country object
def get_or_create_country(country_name):
    stm=select(Country)\
        .where(Country.country==country_name)

    country_obj=db.session.execute(stm).scalar()

    if not country_obj:
        country_obj=Country(country=country_name)
        db.session.add(country_obj)

        db.session.flush()#don't commit changes to database until commit but it exits
    return country_obj



#will return city object without passing id 
def get_or_create_city(city_name, country_id):
    stm=select(City)\
        .where(City.city==city_name, City.country_id==country_id)
    

    city_obj=db.session.execute(stm).scalar()

    if not city_obj:
        city_obj=City(city=city_name, country_id=country_id)

        db.session.add(city_obj)
        db.session.flush()
    return city_obj

#return address object if it exists or not, without passing id
def get_or_create_address(data, city_id):

    #find address
    stm=select(Address)\
        .where(Address.address==data.get('address'),
            Address.address2 == data.get('address2'),
            Address.district == data.get('district'),
            Address.city_id == city_id,
            Address.postal_code == data.get('postal_code'),
            Address.phone == data.get('phone')

    )

    address_obj=db.session.execute(stm).scalar()

    #if not create address
    if not address_obj:
        address_obj=Address(
            address=data.get('address'),
            address2 = data.get('address2'),
            district = data.get('district'),
            city_id = city_id,
            postal_code = data.get('postal_code'),
            phone = data.get('phone'),
        )

        db.session.add(address_obj)
        db.session.flush()
    return address_obj

def get_address_by_id(id):
    return db.session.execute(select(Address).where(Address.address_id==id)).scalar()

def get_city_by_id(id):
        return db.session.execute(select(City).where(City.city_id==id)).scalar()

def get_country_by_if(id):
        return db.session.execute(select(Country).where(Country.country_id==id)).scalar()
