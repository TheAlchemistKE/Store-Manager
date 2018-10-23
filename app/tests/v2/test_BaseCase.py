import unittest
import json
from ... import create_app


class TestBaseCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.content_type = 'application/json'

        # Creating Valid Payloads
        self.product_payload = {
            "Product Name": "Shoe",
            "Product Price": 200,
            "Product Category": "Clothing",
            "Quantity in Inventory": 500
        }
        self.sales_payload = {
            "Sold By": "Kelyn",
            "Quantity Sold": 20,
            "Date Created": "27/8/2016",
            "Price per unit": 650
        }
        self.user_payload = {
            "Name": "Kelyn",
            "Username": "testme",
            "Password": "Password"
        }
        self.login_credentials = {
            "Username": "testme",
            "Password": "Password"
        }
        self.invalid_login_credential = {
            "Username": "",
            "Password": "Password"
        }

    def login(self):
        self.client.post(
            'api/v2/register', data=json.dumps(self.user_payload), content_type=self.content_type)
        login = self.client.post(
            'api/v2/login', data=json.dumps(self.login_credentials), content_type=self.content_type)
        return json.loads(login.data.decode())["Authorization_Token"]

    def tearDown(self):
        self.client = None
        self.content_type = None
