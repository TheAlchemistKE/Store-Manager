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

def product_checker(product_name, )