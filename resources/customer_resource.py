from flask_restful import Resource, request
from services.customer_service import list_cust


class ListCustomers(Resource):
    def get (self):
            page = request.args.get("page", 1, type=int)
            per_page = request.args.get("per_page", 12, type=int)
            return list_cust(page, per_page), 200
    
    
