from flask import jsonify


# Checking if the fields are empty.
def product_validator(data):
    if bool(data["Product Name"]) != True:
       return jsonify({"message": "Product Name cannot be empty."})

    elif bool(data["Product Category"]) != True:
        return jsonify({"message": "Product Category cannot be empty."})
    
    else:
        return "OK"