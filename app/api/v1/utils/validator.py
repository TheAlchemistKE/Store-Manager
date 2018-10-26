import re
from flask import jsonify, make_response


def credential_checker(name, username, password):
    if (bool(name) and name.isalpha()) != True:
        msg = {
            "Message": "Name must be filled and a string"
        }
        return make_response(jsonify(msg), 400)

    elif (bool(username) and username.isalpha()) != True:
        msg = {
            "Message": "Username must be filled and a string"
        }
        return make_response(jsonify(msg), 400)

    elif bool(password) != True:
        msg = {
            "Message": "Password cannot be blank."
        }
        return make_response(jsonify(msg), 400)
    elif re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        msg = {
            "Message": "Password should contain uppercase, lowercase, special case and numbers."
        }
        return make_response(jsonify(msg), 400)
    else:
        return True


def login_checker(username, password):
    if (bool(username) and username.isalpha()) != True:
        msg = {
            "Message": "Username must be filled and a string"
        }
        return make_response(jsonify(msg), 400)

    elif bool(password) != True:
        msg = {
            "Message": "Password cannot be blank."
        }
        return make_response(jsonify(msg), 400)
    elif re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
        msg = {
            "Message": "Password should contain uppercase, lowercase, special case and numbers."
        }
        return make_response(jsonify(msg), 400)
    else:
        return True

def product_checker(product_name, product_price, category, quantity):
    if (bool(product_name) and product_name.isalpha()) != True:
        msg = {
            "Message": "Product Name must be filled and should be a string"
        }
        return make_response(jsonify(msg), 400)
    elif (bool(product_price) and product_price.isdigit()) != True:
        msg = {
            "Message": "Product Price must be filled and should be a number"
        }
        return make_response(jsonify(msg), 400)
    elif (bool(category) and category.isalpha()) != True:
        msg = {
            "Message": "Product Category must be filled and should be a string"
        }
        return make_response(jsonify(msg), 400)
    elif (bool(quantity) and quantity.isdigit()) != True:
        msg = {
            "Message": "Quantity must be filled and should be a number"
        }
        return make_response(jsonify(msg), 400)
    else:
        return True

def sales_validator(sold_by, quantity_sold, price_per_unit):
    if (bool(sold_by) and sold_by.isalpha()) != True:
        msg = {
            "Message": "Product Name must be filled and should be a string"
        }
        return make_response(jsonify(msg), 400)
    elif bool(quantity_sold) != True:
        msg = {
            "Message": "Product Price must be filled and should be a number"
        }
        return make_response(jsonify(msg), 400)
    elif bool(price_per_unit) != True:
        msg = {
            "Message": "Price per unit must be filled and must be a number."
        }
        return make_response(jsonify(msg), 400)
    else:
        return True

