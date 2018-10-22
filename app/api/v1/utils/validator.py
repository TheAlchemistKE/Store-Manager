import re
from flask import jsonify, make_response

#Validator Functions...
def input_validator(*args):
    for (username, password, quantity) in args:
        if isinstance(username, str) and bool(username) != True:
            return make_response(jsonify({"message": "Username should be filled and a string"}))
