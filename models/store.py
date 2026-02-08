from extensions import db

class Store(db.Model):
    __table_name__='store'
    store_id=db.Column(db.Integer, primary_key=True)
    manager_staff_id=db.Column(db.Integer, nullable=False)
    adress_id=db.Column(db.Integer, nullable=False)