import unittest
import json
from .test_BaseCase import TestBaseCase


class TestProductEndpoints(TestBaseCase):
    def test_post_products(self):
        response = self.client.post('api/v2/products',
                                    data=json.dumps(self.product_payload),
                                    headers={
                                        "Authorization": "Bearer " + self.login},
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_get_all_products(self):
        response = self.client.get('api/v2/products',
                                    headers={
                                        "Authorization": "Bearer " + self.login()},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_one_product(self):
        response = self.client.post('api/v1/products',
                                    data=json.dumps(self.product_payload),
                                    headers={
                                        "Authorization": "Bearer " + self.login()},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        response_data = self.client.get('api/v1/products',
                                    headers={
                                        "Authorization": "Bearer " + self.login()},
                                    content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_update_product_details(self):
        pass

    def test_delete_one_product(self):
        pass


class TestProductDetails(TestBaseCase):
    def test_correct_input_type(self):
        pass

    def test_incorrect_input_types(self):
        pass

    def test_extra_input_fields(self):
        pass