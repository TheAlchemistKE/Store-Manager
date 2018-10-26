import unittest
import json
from ... import create_app


class TestValidInput(unittest.TestCase):
    def setUp(self):
        self.content_type = 'application/json'
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.product = {
            "Product Name": "New",
            "Product Price": 200,
            "Product Category": "Category",
            "Quantity in Inventory": 50
        }
        self.credentials = {
            "Name": "Kelyn",
            "Username": "new",
            "Password": "Kelyn1@"
        }
        self.login = {
            "Username": "new",
            "Password": "Kelyn1@"
        }

    def tearDown(self):
        self.client = None
        self.content_type = None
        
    def user_login(self):
        x = self.client.post(
            'api/v1/register', data=json.dumps(self.credentials), content_type=self.content_type)
        print(json.loads(x.data.decode()))
        login = self.client.post(
            'api/v1/login', data=json.dumps(self.login), content_type=self.content_type)
        return json.loads(login.data.decode())['Authorization_Token']

    def test_post_products(self):
        payload = {
            "Product Name": "New",
            "Product Price": 200,
            "Product Category": "Category",
            "Quantity in Inventory": 50
        }
        response = self.client.post('api/v1/products',
                                    data=json.dumps(payload),
                                    headers={
                                        "Authorization": "Bearer " + self.user_login()},
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_post_sales(self):
        payload = {
            "Sold By": "Kevin",
            "Quantity Sold": 200,
            "Price per unit": 30
        }
        response = self.client.post('api/v1/sales',
                                    data=json.dumps(payload),
                                    headers={
                                        "Authorization": "Bearer " + self.user_login()},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_products(self):
        response = self.client.get('api/v1/products',
                                   headers={
                                       "Authorization": "Bearer " + self.user_login()},
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_sales(self):
        response = self.client.get('api/v1/products',
                                   headers={
                                       "Authorization": "Bearer " + self.user_login()},
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_one_sales_records(self):
        payload = {
            "Sold By": "Kelyn Paul",
            "Quantity Sold": 500,
            "Price per unit": 20
        }
        response = self.client.post('api/v1/sales',
                                    data=json.dumps(payload),
                                    headers={
                                        "Authorization": "Bearer " + self.user_login()},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response_data = self.client.get('api/v1/sales',
                                        headers={
                                            "Authorization": "Bearer " + self.user_login()},
                                        content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_get_one_products(self):
        payload = {
            "Product Name": "Knife",
            "Product Price": 250,
            "Product Category": "Kitchenware",
            "Quantity in Inventory": 40
        }
        response = self.client.post('api/v1/products',
                                    data=json.dumps(payload),
                                    headers={
                                        "Authorization": "Bearer " + self.user_login()},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response_data = self.client.get('api/v1/products',
                                        headers={
                                            "Authorization": "Bearer " + self.user_login()},
                                        content_type='application/json')
        self.assertEqual(response_data.status_code, 200)


class TestEmptyInputs(TestValidInput):
    # Here the user doesn't fill in certain fields.

    def test_empty_product_post(self):
        payload = {
            "Product Price": 200,
            "Product Category": "Category",
            "Quantity in Inventory": 50
        }
        response = self.client.post('api/v1/products',
                                    data=json.dumps(payload),
                                    headers={
                                        "Authorization": "Bearer " + self.user_login()},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_empty_sale_records_post(self):
        payload = {
            "Sold By": "Kevin",
            "Quantity Sold": 200,
            "Date Created": "",
            "Price per unit": 30
        }
        response = self.client.post('api/v1/sales',
                                    data=json.dumps(payload),
                                    headers={
                                        "Authorization": "Bearer " + self.user_login()},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_multiple_empty_fields_products_post(self):
        payload = {
            "Product Name": "",
            "Product Price": "",
            "Product Category": "",
            "Quantity in Inventory": 50
        }
        response = self.client.post('api/v1/products',
                                    data=json.dumps(payload),
                                    headers={
                                        "Authorization": "Bearer " + self.user_login()},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_multiple_empty_fields_sales_post(self):
        payload = {
            "Quantity Sold": 200,
            "Price per unit": ""
        }
        response = self.client.post('api/v1/sales',
                                    data=json.dumps(payload),
                                    headers={
                                        "Authorization": "Bearer " + self.user_login()},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)


