import unittest
import json
from .test_BaseCase import TestBaseCase


class TestProductEndpoints(TestBaseCase):
    def test_post_sales(self):
        response = self.client.post('api/v2/sales',
                                    data=json.dumps(self.product_payload),
                                    headers={
                                        "Authorization": "Bearer " + self.login},
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_get_all_sales(self):
        response = self.client.get('api/v2/sales',
                                   headers={
                                       "Authorization": "Bearer " + self.login()},
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_one_sale(self):
        response_data = self.client.get('api/v2/sales/1',
                                        headers={
                                            "Authorization": "Bearer " + self.login()},
                                        content_type='application/json')
        self.assertEqual(response_data.status_code, 200)

    def test_update_sale_details(self):
        update_response = self.client.put('api/v2/sales/1', data=json.dumps(self.updated_payload), headers={
            "Authorization": "Bearer " + self.login()},
            content_type='application/json')
        self.assertEqual(update_response.status_code, 200)

    def test_delete_one_sale(self):
        response = self.client.delete('api/v2/sales/1', data=json.dumps(self.updated_payload), headers={
            "Authorization": "Bearer " + self.login()},
            content_type='application/json')
        self.assertEqual(response.status_code, 200)