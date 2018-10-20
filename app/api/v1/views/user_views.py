from flask import jsonify, request, make_response
from flask_restful import Resource, reqparse

#Local Imports
from ..models.user_model import Users

user_object = Users()


parser = reqparse.RequestParser()
parser.add_argument("username", type=str,
                    help="Username cannot be left blank.")
parser.add_argument("password", type=str,
                    help="Password cannot be left blank.")
parser.add_argument("role", type=str, help="Role cannot be left blank.")

class UserRegistration(Resource):
    def post(self):
        user_data = parser.parse_args()
        username = user_data["username"]
        password = user_data["password"]

        password = user_object.generate_password_hash(password)
        resp = {
            "message": "Register successful.",
            "User": user_object.signup(username, password)
        }
        return jsonify(resp)


