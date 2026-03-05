from extensions import db
from models.rental import Rental
from models.inventory import Inventory

def create_rent_record(film_id, customer_id):
    #unpacking->inserts items into model object
    inventory = Inventory.query.filter_by(film_id=film_id).first()
    if not inventory:
        print("No inventory found for this film!")
        raise ValueError("No inventory available for this film")

    print(f"Using inventory_id={inventory.inventory_id}")

    rental = Rental(
        inventory_id=inventory.inventory_id,
        customer_id=customer_id,
        staff_id=1
    )

    db.session.add(rental)
    try:
        db.session.commit()
    except Exception as e:
        print("DB commit error:", e)
        raise
        #print(f"Rental created: rental_id={rental.rental_id}")

    return rental