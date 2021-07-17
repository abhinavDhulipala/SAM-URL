from unittest import TestCase
import requests as req

"""
Integration tests for AWS SAM. Requires that you run sam with "sam local start-api" and activate the virtualenv
"""
api_endpoint = 'http://127.0.0.1:3000'
class TestApiGateway(TestCase):

    def test_api_gateway(self):
        """
        Call the API Gateway endpoint and check the response
        """
        response = req.get(api_endpoint)
        self.assertDictEqual(response.json(), {'message': 'Missing Authentication Token'})

