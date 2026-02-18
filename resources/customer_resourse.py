from flask_restful import Resource, reqparse
from services.customer_service import all_customers_paginated


parser=reqparse.RequestParser()
parser.add_argument('page', type=int, location='args', default=1)
parser.add_argument('per_page', type=int, location='args', default=12)

class CustomerList(Resource):
    def get(self):

        args=parser.parse_args()
        data=all_customers_paginated(args['page'],args['per_page'])

        return data, 200

