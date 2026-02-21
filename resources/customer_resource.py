from flask_restful import Resource, reqparse, request
from services.customer_service import all_customers_paginated, search_customers


parser=reqparse.RequestParser()
parser.add_argument('page', type=int, location='args', default=1)
parser.add_argument('per_page', type=int, location='args', default=12)

class CustomerResource(Resource):
    def get(self):

       

         #?s=...&by=... <=gets args from here
        search_for=request.args.get('s', '').strip()
        search_by=request.args.get('by', '')
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)

        if search_for:

            valid_types=['customer_id', 'first_name', 'last_name']
                    
            if search_by not in valid_types:
                return {"message": f"Invalid search type must be one of: {','.join(valid_types)}"}, 400

            return search_customers(search_for, search_by, page, per_page), 200
        

        data=all_customers_paginated(page, per_page)
        return data, 200



    # def post(self):
