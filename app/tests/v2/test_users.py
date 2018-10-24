import unittest
import json
from .test_BaseCase import TestBaseCase


class TestProductEndpoints(TestBaseCase):
    def test_signup_user(self):
        response = self.client.post('api/v2/auth/signup',
                                    data=json.dumps(self.user_payload),
                                    headers={
                                        "Authorization": "Bearer " + self.login},
                                    content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        response = self.client.post('api/v2//auth/login',
                                    data=json.dumps(self.login_credentials),
                                    content_type=self.content_type)
        self.assertEqual(response.status_code, 200)
