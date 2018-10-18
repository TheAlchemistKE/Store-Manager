from flask import Flask, jsonify, Blueprint, request, make_response
from flask_restful import Api, Resource

# Local Imports
from ..models.data_models import SalesOps

sales_blueprint = Blueprint('sales_blueprint', __name__, url_prefix='/api/v1')
sales_api = Api(sales_blueprint)


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

    def post(self):
        data = request.get_json()
        sales_by = data['Sold By']
        quantity_sold = data['Quantity Sold']
        sales_date = data['Date Created']
        unit_price = data['Price per unit']

        resp = {
            "Message": "Created.",
            "Status": "OK",
            "Sales Records": self.sales_obj.save_sales_record(sales_by, quantity_sold, sales_date, unit_price)
        }
        return make_response(jsonify(resp), 201)


class SingleSaleRecords(Resource):
    def __init__(self):
        self.records_obj = SalesOps()

    def get(self, sale_id):
        resp = {
            "Message": "Successful.",
            "Product": self.records_obj.show_one(sale_id)
        }
        return make_response(jsonify(resp), 200)
