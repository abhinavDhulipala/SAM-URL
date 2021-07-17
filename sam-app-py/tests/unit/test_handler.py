import json
import pytest
import os
import sys
abs_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f'{abs_path}/../..')
sys.path.append(f'{abs_path}/../../..')
print(sys.path[-1])
from moto import mock_dynamodb2
from redirect_handler import app
import boto_utils
from constants import TABLE_NAME
import boto3


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""
    with open('./events/redirect_simple_event.json') as fp:
        return json.load(fp)

def test_lambda_handler(apigw_event):
    # Note put must work. You should have a test entry in your DB under the entry '1234567' for you to pass this test
    @mock_dynamodb2
    def mock_events():
        dynamodb = boto3.resource('dynamodb')
        created_table = dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {
                    'AttributeName': 'redirect_url',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'redirect_url',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        boto_utils.put('https://example.com', '1234567', '', '')

    mock_events()

    ret = app.lambda_handler(apigw_event, '')

    assert ret['statusCode'] == 302
    assert 'location' in ret['headers']

    failed_codes = {206, 204}
    apigw_event['pathParameters']['hash'] = apigw_event['pathParameters']['hash'][:-1]
    ret = app.lambda_handler(apigw_event, '')
    assert ret['statusCode'] in failed_codes

    apigw_event['pathParameters']['hash'] = 'garbage'
    ret = app.lambda_handler(apigw_event, '')
    assert ret['statusCode'] in failed_codes
