from flask import jsonify, request, make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

# Local Imports
from ..models.data_models import SalesOps
from ..utils.validator import sales_validator

sales_obj = SalesOps()

parser = reqparse.RequestParser()
parser.add_argument("Sold By", type=str, required=True,
                    help="Sold By required.")
parser.add_argument("Quantity Sold", type=int, required=True,
                    help="Quantity Sold required.")
parser.add_argument("Price per unit", type=int,
                    required=True, help="Price per unit required.")


class SalesList(Resource, SalesOps):
    @jwt_required
    def get(self):
        resp = {
            "Message": "Successful.",
            "Status": "Ok",
            "Sale Records": sales_obj.retrieve_all_items()
        }
        return make_response(jsonify(resp), 200)

    @jwt_required
    def post(self):
        data = parser.parse_args(strict=True)
        sales_by = data['Sold By']
        quantity_sold = data['Quantity Sold']
        unit_price = data['Price per unit']

        resp = {
            "Message": "New Sales Record Created.",
            "Status": "OK",
            "Sales Records": sales_obj.save_sales_record(sales_by, quantity_sold, unit_price)
        }
        return make_response(jsonify(resp), 201)

# Get Single Product.


class SingleSaleRecords(Resource):

    @jwt_required
    def get(self, sale_id):
        resp = {
            "Message": "Request Successful.",
            "Product": sales_obj.show_one(sale_id)
        }
        return make_response(jsonify(resp), 200)
