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