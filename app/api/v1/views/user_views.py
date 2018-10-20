from flask_restful import reqparse, Resource
#Local Imports
from ..models.user_model import User

#User Object.
user_object = User()

#Parsing and requesting for Data.
parser = reqparse.RequestParser()
parser.add_argument("Name", type=str, help="Name field required")
parser.add_argument("Username", type=str, help="Username field required")
parser.add_argument("Password", type=str, help="Password field required")


class UserActions(Resource):
    def post(self):
        data = parser.parse_args()
        name = data["Name"]
        username = data["Username"]
        password = data["Password"]

        resp = {
            "message": "Successful registration!",
            "User Details": user_object.register_user(name, username, password)
        }
        return resp
    

class AllUsers(Resource):
    def get(self):
        resp = {
            "Message": "Successful.",
            "Status": "Ok.",
            "Users": user_object.get_all_users()
        }
        return resp