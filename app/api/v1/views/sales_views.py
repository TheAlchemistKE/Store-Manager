from flask import jsonify, request, make_response
from flask_restful import Resource

# Local Imports
from ..models.data_models import SalesOps
sales_obj = SalesOps()


class SalesList(Resource, SalesOps):

    def get(self):
        resp = {
            "Message": "Successful.",
            "Status": "Ok",
            "Sale Records": sales_obj.retrieve_all_items()
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
            "Sales Records": sales_obj.save_sales_record(sales_by, quantity_sold, sales_date, unit_price)
        }
        return make_response(jsonify(resp), 201)

# Get Single Product.


class SingleSaleRecords(Resource):
    def get(self, sale_id):
        resp = {
            "Message": "Successful.",
            "Product": sales_obj.show_one(sale_id)
        }
        return make_response(jsonify(resp), 200)
