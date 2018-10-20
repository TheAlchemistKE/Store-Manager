from flask_restful import reqparse
from flask import jsonify, make_response
import passlib






parser = reqparse.RequestParser()
parser.add_argument("username", type=str,
                    help="Username cannot be left blank.")
parser.add_argument("password", type=str,
                    help="Password cannot be left blank.")
parser.add_argument("role", type=str, help="Role cannot be left blank.")

users = []


def authenticate():
    pass


class Users():
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def signup(self):
        user_data = parser.parse_args()
        username = user_data["username"]
        password = user_data["password"]

        user_payload = {
            "Id": len(users)+1,
            "Username": username,
            "Password": password
        }
        users.append(user_payload)

    def login(self, username, password):
        for user in users:
            if user["Username"] == username:
                return user
            else:
                return make_response(jsonify({"message": "User not found."}), 404)

    def logout(self):
        pass
