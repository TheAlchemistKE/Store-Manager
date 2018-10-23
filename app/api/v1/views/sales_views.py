from flask import Flask, jsonify, Blueprint, request, make_response
from flask_restful import Api, Resource

# Local Imports
from ..models.data_models import SalesOps

class SalesList(Resource, SalesOps):
    def __init__(self):
        self.sales_obj = SalesOps()

    def get(self):
        resp = {
            "Message": "Successful.",
            "Status": "Ok",
            "Sale Records": self.sales_obj.retrieve_all_items()
        }
        return make_response(jsonify(resp), 200)