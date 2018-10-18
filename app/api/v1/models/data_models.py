from flask import jsonify, make_response
from flask_restful import abort
product_list = []
sales_list = []


class ProductOps:
    def __init__(self):
        self.products = product_list

    def save_product(self, name, price, category, quantity):
        params = [name, category]
        for param in params:
            if bool(param) is False:
                return make_response(jsonify({"Message": "{} cannot be null.".format(param)}), 406)

        payload = {
            "Id": len(self.products)+1,
            "Product Name": name,
            "Product Price": price,
            "Product Category": category,
            "Quantity in Inventory": quantity
        }
        self.products.append(payload)
        return self.products

    def retrieve_all_items(self):
        return self.products

    def show_one(self, product_id):
        for product_item in self.products:
            if product_item["Id"] == product_id:
                return product_item
        return abort(404, message="Product {} does not exist in inventory".format(product_id))


class SalesOps():
    def __init__(self):
        self.sales = sales_list

    def save_sales_record(self, sales_by, quantity_sold, sales_date, unit_price):
        payload = {
            "Id": len(self.sales)+1,
            "Sold By": sales_by,
            "Quantity Sold": quantity_sold,
            "Date Created": sales_date,
            "Price per unit": unit_price,
            "Total": quantity_sold * unit_price
        }
        self.sales.append(payload)
        return self.sales

    def retrieve_all_items(self):
        return self.sales

    def show_one(self, sale_id):
        for sale_records in self.sales:
            if sale_records["Id"] == sale_id:
                return sale_records
        return abort(404)
