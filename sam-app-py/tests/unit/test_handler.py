import sys
from os.path import abspath

sys.path.append(abspath('..'))

print(sys.path)

import json
import pytest
import boto_utils
from redirect_handler import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""
    with open('./events/redirect_simple_event.json') as fp:
        return json.load(fp)


def test_lambda_handler(apigw_event):
    # Note put must work. You should have a test entry in your DB under the entry '1234567' for you to pass this test
    ret = app.lambda_handler(apigw_event, '')
    data = ret['body']

    assert ret['statusCode'] == 302
    assert 'location' in ret['headers']

    apigw_event['pathParameters']['hash'] = apigw_event['pathParameters']['hash'][:-1]
    ret = app.lambda_handler(apigw_event, '')
    assert ret['statusCode'] in {206, 204}

    apigw_event['pathParameters']['hash'] = 'garbage'
    ret = app.lambda_handler(apigw_event, '')
    assert ret['statusCode'] in {206, 204}

