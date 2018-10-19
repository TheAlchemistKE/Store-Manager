from flask import request, make_response, jsonify
from flask_restful import Resource, reqparse

# Local Imports
from ..models.data_models import ProductOps
from ..utils.validator import product_validator

product_obj = ProductOps()

#Creating a parser for adding data.
parser = reqparse.RequestParser()
parser.add_argument("Product Name", type=str, required=True, help="Check your Product Name.")
parser.add_argument("Product Price", type=int, required=True, help="Check your Product Price.")
parser.add_argument("Product Category", type=str, required=True, help="Check your Product Category.")
parser.add_argument("Quantity in Inventory", type=int, required=True, help="Check your 'Quantity in Inventory'")

class ProductList(Resource):

    def get(self):
        resp = {
            "Message": "Successful.",
            "Status": "Ok",
            "Products": product_obj.retrieve_all_items()
        }
        return make_response(jsonify(resp), 200)

    def post(self):
        data = parser.parse_args()
        name = data["Product Name"]
        price = data["Product Price"]
        category = data["Product Category"]
        quantity = data["Quantity in Inventory"]

        #Validating User's input.
        validate = product_validator(data)

        if validate == "OK":
            resp = {
                "Message": "Created.",
                "Status": "Ok.",
                "Products": product_obj.save_product(name, price, category, quantity)
            }
            return make_response(jsonify(resp), 201)
        else:
            return validate


class SingleProduct(Resource):
    def get(self, product_id):
        resp = {
            "Message": "Successful.",
            "Product": product_obj.show_one(product_id)
        }
        return make_response(jsonify(resp), 200)
