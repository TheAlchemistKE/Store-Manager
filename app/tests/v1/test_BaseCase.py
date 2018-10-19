import unittest
import json
from ... import create_app


class TestValidInput(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing").test_client()
        self.content_type = 'application/json'

    def tearDown(self):
        self.app = None
        self.content_type = None

    def test_post_products(self):
        payload = {
            "Product Name": "New",
            "Product Price": 200,
            "Product Category": "Category",
            "Quantity in Inventory": 50
        }
        resp = self.app.post(
            '/api/v1/products', content_type=self.content_type, data=json.dumps(payload))
        self.assertEqual(resp.status_code, 201)

    def test_post_sales(self):
        payload = {
            "Sold By": "Kevin",
            "Quantity Sold": 200,
            "Date Created": "27/8/2016",
            "Price per unit": 30
        }
        resp = self.app.post(
            '/api/v1/sales', content_type=self.content_type, data=json.dumps(payload))
        self.assertEqual(resp.status_code, 201)

    def test_get_products(self):
        resp = self.app.get(
            '/api/v1/products', content_type=self.content_type)
        self.assertEqual(resp.status_code, 200)

    def test_get_sales(self):
        resp = self.app.get(
            '/api/v1/sales', content_type=self.content_type)
        self.assertEqual(resp.status_code, 200)

    def test_get_one_sales_records(self):
        payload = {
            "Sold By": "Kelyn Paul",
            "Quantity Sold": 500,
            "Date Created": "31/09/2020",
            "Price per unit": 20
        }
        post_data = self.app.post(
            '/api/v1/sales', content_type=self.content_type, data=json.dumps(payload))
        self.assertEqual(post_data.status_code, 201)
        resp = self.app.get(
            '/api/v1/sales/{}'.format(1), content_type=self.content_type)
        self.assertEqual(resp.status_code, 200)

    def test_get_one_products(self):
        payload = {
            "Product Name": "Knife",
            "Product Price": 250,
            "Product Category": "Kitchenware",
            "Quantity in Inventory": 40
        }
        post_data = self.app.post(
            '/api/v1/products', content_type=self.content_type, data=json.dumps(payload))
        self.assertEqual(post_data.status_code, 201)
        resp = self.app.get(
            '/api/v1/products/{}'.format(1), content_type=self.content_type)
        self.assertEqual(resp.status_code, 200)


class TestEmptyInputs(TestValidInput):
    # Here the user doesn't fill in certain fields.
    def test_empty_product_post(self):
        payload = {
            "Product Name": "",
            "Product Price": 200,
            "Product Category": "Category",
            "Quantity in Inventory": 50
        }
        resp = self.app.post(
            '/api/v1/products', content_type=self.content_type, data=json.dumps(payload))
        self.assertEqual(resp.status_code, 400)

    def test_empty_sale_records_post(self):
        payload = {
            "Sold By": "Kevin",
            "Quantity Sold": 200,
            "Date Created": "",
            "Price per unit": 30
        }
        resp = self.app.post(
            '/api/v1/sales', content_type=self.content_type, data=json.dumps(payload))
        self.assertEqual(resp.status_code, 400)

    def test_multiple_empty_fields_products_post(self):
        payload = {
            "Product Name": "",
            "Product Price": "",
            "Product Category": "",
            "Quantity in Inventory": 50
        }
        resp = self.app.post(
            '/api/v1/products', content_type=self.content_type, data=json.dumps(payload))
        self.assertEqual(resp.status_code, 400)

    def test_multiple_empty_fields_sales_post(self):
        payload = {
            "Sold By": "",
            "Quantity Sold": 200,
            "Date Created": "",
            "Price per unit": ""
        }
        resp = self.app.post(
            '/api/v1/sales', content_type=self.content_type, data=json.dumps(payload))
        self.assertEqual(resp.status_code, 400)


class TestExtremeCases(TestValidInput):
    def test_missing_fields_post_product(self):
        payload = {
            "Product Category": "Category",
            "Quantity in Inventory": 50
        }
        resp = self.app.post(
            '/api/v1/products', content_type=self.content_type, data=json.dumps(payload))
        self.assertEqual(resp.status_code, 400)

    def test_missing_fields_post_sales(self):
        payload = {
            "Sold By": "",
            "Quantity Sold": 200,
            "Date Created": "",
            "Price per unit": ""
        }
        resp = self.app.post(
            '/api/v1/sales', content_type=self.content_type, data=json.dumps(payload))
        self.assertEqual(resp.status_code, 400)
