from flask_restful import Resource, request
from marshmallow import ValidationError
from services.rental_service import create_rent_record
from schemas import rental_schema


class RentalRecords(Resource):
    def post(self):

        data=request.get_json()
        try:
            rental_obj=rental_schema.load(data)
            saved_rental=create_rent_record(rental_obj)
           
            return rental_schema.dump(saved_rental), 201
        
        except ValidationError as e:
            return e.messages, 400
        

       

        


    

