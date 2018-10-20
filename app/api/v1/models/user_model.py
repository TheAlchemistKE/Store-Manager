from flask_restful import reqparse
from flask import jsonify, make_response
from passlib.hash import pbkdf2_sha256 as sha256


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

    def signup(self, username, password):
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

    @staticmethod
    def generate_password_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_password_hash(password, hash):
        return sha256.verify(password, hash)

    def logout(self):
        pass
