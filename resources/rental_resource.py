from flask_restful import Resource, request
from flask import request, jsonify
from marshmallow import ValidationError
from services.rental_service import create_rent_record

class RentalRecords(Resource):
    def post(self):
        data = request.get_json()
        #print("POST /rentals payload:", data)
        film_id = data.get("film_id")
        customer_id = data.get("customer_id")

        if not film_id or not customer_id:
            return {"error": "film_id and customer_id are required"}, 400

        try:
            rental = create_rent_record(film_id, customer_id)
            return {"message": "Rental created", "rental_id": rental.rental_id}, 200
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": "Server error"}, 500
        

       

        


    

