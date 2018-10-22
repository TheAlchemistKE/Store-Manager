from flask_restful import reqparse, Resource
from flask_jwt_extended import (create_access_token, jwt_required, create_refresh_token,
                                jwt_refresh_token_required, get_raw_jwt, get_jwt_identity)
# Local Imports
from ..models.user_model import User


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

        # result = user_object.register_user(name, username, password)

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
            return {"Message": "Something's a bit off."}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        print(data)
        username = data["Username"]
        password = data["Password"]

        if user_object.login(username, password) == True:
            resp = {
                "Message": "Logged in as {}".format(username),
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
