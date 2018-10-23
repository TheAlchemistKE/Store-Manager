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
        response_data = self.client.get('api/v1/products/1',
                                    headers={
                                        "Authorization": "Bearer " + self.login()},
                                    content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_update_product_details(self):
        update_response = self.client.put('api/v1/products/1', data=json.dumps(self.updated_payload), headers={
                                        "Authorization": "Bearer " + self.login()},
                                    content_type='application/json' )
        self.assertEqual(update_response.status_code, 200)  

    def test_delete_one_product(self):
        response = self.client.delete('api/v1/products/1', data=json.dumps(self.updated_payload), headers={
                                        "Authorization": "Bearer " + self.login()},
                                    content_type='application/json' )
        self.assertEqual(response.status_code, 200)  
