import os
from unittest import TestCase
import requests as req
import boto3
import requests

"""
Integration tests for AWS SAM. Requires that you run sam with 
"""
api_endpoint = 'http://localhost:3000'
class TestApiGateway(TestCase):

    def setUpClass(cls) -> None:
        # check if port is open
        req.get(api_endpoint)

    def test_api_gateway(self):
        """
        Call the API Gateway endpoint and check the response
        """
        response = requests.get(api_endpoint)
        self.assertDictEqual(response.json(), {"message": "hello world"})
