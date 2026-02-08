from extensions import db

# represents columns(not all) in store table in database
class Store(db.Model):
    __table_name__='store'
    store_id=db.Column(db.Integer, primary_key=True)
    manager_staff_id=db.Column(db.Integer, nullable=False)
    adress_id=db.Column(db.Integer, nullable=False)