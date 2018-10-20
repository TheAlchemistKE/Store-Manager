from flask_restful import reqparse
from passlib.hash import pbkdf2_sha256 as sha256

user_list = []


class User():
    def __init__(self):
        self.users = user_list

    def register_user(self, name, username, password):
        user_payload = {
            "Id": len(self.users)+1,
            "Name": name,
            "Username": username,
            "Password": User.generate_password_hash(password)
        }

        self.users.append(user_payload)

        return user_payload

    @staticmethod
    def generate_password_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_password_hash(password, hash):
        return sha256.verify(password, hash)

    def get_all_users(self):
        return self.users

    def login(self, username, password):
        for user in self.users:
            if user["Username"] == username and User.verify_password_hash(password, user["Password"]):
                resp = {
                    "message": "Successful login."
                }
                return resp
            else:
                respnse = {
                    "message": "Failed to login."
                }
                return respnse
