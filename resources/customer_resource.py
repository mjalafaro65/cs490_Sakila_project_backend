from flask_restful import Resource, reqparse, request
from services.customer_service import all_customers_paginated, search_customers, create_customer_record, get_customer_by_email, get_customer_by_id, save_customer, delete_customer, get_rentals_customer, return_film_by_id
from schemas import address_customer_schema, single_customer_schema, update_one_customer, rentals_customer_schema
from marshmallow import ValidationError


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

        #continue if it for searching
        if search_for:

            valid_types=['customer_id', 'first_name', 'last_name']
                    
            if search_by not in valid_types:
                return {"message": f"Invalid search type must be one of: {','.join(valid_types)}"}, 400

            return search_customers(search_for, search_by, page, per_page), 200
        
        #all customers
        data=all_customers_paginated(page, per_page)
        return data, 200



#create customer record
    def post(self):
        data=request.get_json()

        # make sure inputs are valid
        required_fields=["first_name", "last_name", "email", "address","district","postal_code","city", "country","phone"]
        if not all(data.get(field) for field in required_fields):
            return {"message":"Error Fields Invalid"}, 400
        

        #email exits?
        if get_customer_by_email(data.get('email')):
            return {"message":"User with this email exists"}, 400
            
        try:
            #returns dict
            data_as_dict=address_customer_schema.load(data)
            #passes dict
            saved_customer=create_customer_record(data_as_dict)
           
            return single_customer_schema.dump(saved_customer), 201
        except ValidationError as e:
            return e.messages, 400
        


class OneCustomerResource(Resource):
    def put(self,id):
        data=request.get_json()

        # make sure inputs are valid
        required_fields=["first_name", "last_name", "email", "address","district","postal_code","city", "country","phone"]
        if not all(data.get(field) for field in required_fields):
            return {"message":"Error Fields Invalid"}, 400
        
        #find customer
        customer_obj=get_customer_by_id(id)

        if not customer_obj:
            return {'message':"Customer not found"}, 404

        try: 
            #makes changes in base fields in customer obj 
            update_one_customer.load(data, instance=customer_obj)

            #check for updates in address and update
            updated_customer=save_customer(data, customer_obj)
            
            #return updated object
            return single_customer_schema.dump(updated_customer), 201
        
        except ValidationError as e:
            return e.messages, 400
        
    def delete(self,id):

        customer_obj=get_customer_by_id(id)

        if not customer_obj:
            {"message":"Customer not found"},404
        try:
            delete_customer(customer_obj)
            return {"message": "Customer deleted"}
        
        except Exception as e:
            return {"message": str(e)},500
        

    def get(self,id):

        customer_obj=get_customer_by_id(id)

        if not customer_obj:
            {"message":"Customer not found"},404

        rental_customer_obj=get_rentals_customer(customer_obj)

        try:
            return rentals_customer_schema.dump(rental_customer_obj), 200
        
        except Exception as e:
            return {"message": str(e)},500
    
class ReturnCustomerRental(Resource):
    def patch(self, customer_id, film_id):

        rental_record=return_film_by_id(customer_id, film_id)

        if  rental_record == None:
            return {'message':"Already Returned"}, 404
        else:
             return {'message':"Successful return"},200
            



        

