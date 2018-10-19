from flask import jsonify, make_response


# Checking if the fields are empty.
def product_validator(data):
    if bool(data["Product Name"]) != True:
        return make_response(jsonify({"message": "Product Name cannot be empty."}), 400)

    elif bool(data["Product Category"]) != True:
        return make_response(jsonify({"message": "Product Category cannot be empty."}), 400)

    else:
        return "OK"


def sales_validator(data):
    if bool(data['Sold By']) != True:
        return make_response(jsonify({"message": "Product Name cannot be empty."}), 400)

    elif bool(data['Date Created']) != True:
        return make_response(jsonify({"message": "Product Category cannot be empty."}), 400)

    else:
        return "OK"
