from flask import jsonify, make_response
from flask_restful import reqparse, Resource
from flask_jwt_extended import create_access_token, create_refresh_token


# Local Imports
from ..models.user_model import User
from ..utils.validator import credential_checker, login_checker


# User Object.
user_object = User()

# Parsing and requesting for Data.
parser = reqparse.RequestParser()
parser.add_argument("Name", type=str, help="Name field required")
parser.add_argument("Username", type=str, help="Username field required")
parser.add_argument("Password", type=str, help="Password field required")


class UserRegistration(Resource):

    def post(self):
        data = parser.parse_args()
        name = data["Name"]
        username = data["Username"]
        password = data["Password"]

        validate = credential_checker(name,username, password)

        if  validate == True:
            try:
                result = user_object.register_user(name, username, password)
                auth_token = create_access_token(identity=username)
                renewal_token = create_refresh_token(identity=username)
                token_resp = {
                    "message": "User successfully created.",
                    "Token": auth_token,
                    "New Token": renewal_token,
                    "user": result

                }
                return token_resp
            except:
                return {"Message": "Please provide the user's name, username and password."}, 500
        else:
            return validate
        
        


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        username = data["Username"]
        password = data["Password"]

        validate = login_checker(username, password)

        if validate == True:
            resp = {
                "Message": "Successfully Logged in as {}".format(username),
                "Authorization_Token": create_access_token(identity=username),
                "New Auth Token": create_refresh_token(identity=username)
            }
            return resp
        else:
            return {"Message": "Please enter correct credentials."}


class AllUsers(Resource):
    def get(self):
        resp = {
            "Message": "Successful.",
            "Status": "Ok.",
            "Users": user_object.get_all_users()
        }
        return resp
