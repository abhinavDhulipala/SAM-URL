import boto_utils
import json


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    entry_to_fetch = event.get('pathParameters', {}).get('hash')
    entry = boto_utils.get(entry_to_fetch)
    if not entry:
        return {
            'statusCode': 204,
            'body': json.dumps('Fail: entry does not exist')
        }

    if 'Item' not in entry:
        return {
            'statusCode': 206,
            'body': json.dumps('Fail: incomplete or incorrect hash')
        }
    return {
        'statusCode': 302,
        'headers': {'location': entry['Item']['original_url']},
        'body': 'Success: fetched item'
    }
