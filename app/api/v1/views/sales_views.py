from flask import jsonify, request, make_response
from flask_restful import Resource, reqparse

# Local Imports
from ..models.data_models import SalesOps
from ..utils.validator import sales_validator

sales_obj = SalesOps()

parser = reqparse.RequestParser()
parser.add_argument("Sold By", type=str, required=True, help="Sold By required.")
parser.add_argument("Quantity Sold", type=int, required=True, help="Quantity Sold required.")
parser.add_argument("Date Created", type=str, required=True, help="Date Created required.")
parser.add_argument("Price per unit", type=int, required=True, help="Price per unit required.")


class SalesList(Resource, SalesOps):

    def get(self):
        resp = {
            "Message": "Successful.",
            "Status": "Ok",
            "Sale Records": sales_obj.retrieve_all_items()
        }
        return make_response(jsonify(resp), 200)

    def post(self):
        data = parser.parse_args(strict=True)
        sales_by = data['Sold By']
        quantity_sold = data['Quantity Sold']
        sales_date = data['Date Created']
        unit_price = data['Price per unit']

        validate = sales_validator(data)
        
        if validate == "OK":
            resp = {
                "Message": "Created.",
                "Status": "OK",
                "Sales Records": sales_obj.save_sales_record(sales_by, quantity_sold, sales_date, unit_price)
            }
            return make_response(jsonify(resp), 201)
        else:
            return validate
        
# Get Single Product.


class SingleSaleRecords(Resource):
    def get(self, sale_id):
        resp = {
            "Message": "Successful.",
            "Product": sales_obj.show_one(sale_id)
        }
        return make_response(jsonify(resp), 200)
