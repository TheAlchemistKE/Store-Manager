from flask import Flask, request, make_response, jsonify, Blueprint
from flask_restful import Api, Resource

# Local Imports
from ..models.data_models import ProductOps

product_obj = ProductOps()


class ProductList(Resource):

    def get(self):
        resp = {
            "Message": "Successful.",
            "Status": "Ok",
            "Products": product_obj.retrieve_all_items()
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
            "Products": product_obj.save_product(name, price, category, quantity)
        }
        return make_response(jsonify(resp), 201)


class SingleProduct(Resource):
    def get(self, product_id):
        resp = {
            "Message": "Successful.",
            "Product": product_obj.show_one(product_id)
        }
        return make_response(jsonify(resp), 200)
