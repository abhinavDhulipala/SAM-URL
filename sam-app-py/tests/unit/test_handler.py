import sys
import os

sys.path.append(os.path.abspath('../..'))
print(os.getcwd())
import json
import pytest
from hello_world import app



@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    with open('sam-app-py/events/redirect_simple_event.json') as fp:
        return json.load(fp)

def test_lambda_handler(apigw_event, mocker):
    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in data
    assert data["message"] == "hello world"
    assert data['resource_id'] == '123456'
