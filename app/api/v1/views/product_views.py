from flask import Flask, request, make_response, jsonify, Blueprint
from flask_restful import Api, Resource

# Local Imports
from ..models.data_models import ProductOps

class ProductList(Resource, ProductOps):
    def __init__(self):
        self.product_obj = ProductOps()

    def get(self):
        resp = {
            "Message": "Successful.",
            "Status": "Ok",
            "Products": self.product_obj.retrieve_all_items()
        }
        return make_response(jsonify(resp), 200)

    def post(self):
        data = request.get_json()
        name = data["Product Name"]
        price = data["Product Price"]
        category = data["Product Category"]
        quantity = data["Quantity in Inventory"]
        resp = {
            "Message": "Created.",
            "Status": "Ok.",
            "Products": self.product_obj.save_product(name, price, category, quantity)
        }
        return make_response(jsonify(resp), 201)