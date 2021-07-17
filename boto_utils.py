import boto3 as b3
from botocore.exceptions import ProfileNotFound
from constants import TABLE_NAME
from datetime import datetime
from local_constants import AWS_PROFILE_NAME
from moto import mock_dynamodb2

# locally lambda will find a config file, but once deployed it will use cloud context
try:
    dynamodb = b3.session.Session(profile_name=AWS_PROFILE_NAME).resource('dynamodb')
except ProfileNotFound:
    dynamodb = b3.resource('dynamodb')


# This method will check if a table exists with the given table name.
# @:param t_name -> the name of the table to be checked
# @:returns -> response indicating whether or not table exist
def table_exists(t_name):
    return t_name in map(lambda t: t.name, dynamodb.tables.all())


# This method will run a one time DB migration. This method will provision our DynamoDB table.
# This method will be used to create a table of urls of the proper schema required for CLUrkel
# @:param t_name -> the name of the table to be created
# @:returns -> response indicating success or of table creation
def migration(t_name=TABLE_NAME, force_create=False):
    if table_exists(t_name):
        print('found pre-existing table')
        if force_create:
            print('deleting existing, and recreating')
            table = dynamodb.Table(t_name)
            table.delete()
            table.wait_until_not_exists()
        else:
            print('table found')
            return dynamodb.Table(TABLE_NAME)

    created_table = dynamodb.create_table(
        TableName=t_name,
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

    return created_table


# This method will execute put requests to dynamo URL table.
# @:param original_url -> string of original url
# @:param redirect_hash -> string of new hash
# @:param expiration_date -> string of the expiration date of the redirect url
# @:param user -> string of user id
# @:param table_name -> string of name of table to be queried (defaults to TABLE_NAME in constants.py)
# @:returns -> response of put request if table exists; returns False otherwise
def put(original_url: str, redirect_hash: str, expiration_date: str, user: str, t_name=TABLE_NAME):
    if not table_exists(t_name):
        print("That table does not exist!")
        return False

    table = dynamodb.Table(t_name)
    response = table.put_item(
        Item={
            'redirect_url': redirect_hash,
            'original_url': original_url,
            'creation_date': datetime.now().strftime('%S'),
            'expiration_date': expiration_date,
            'user': user
        }
    )

    return response


# simple utility to get base URL from hash
def get(redirect_url, t_name=TABLE_NAME):
    if not table_exists(t_name):
        print("That table does not exist!")
        return False
    table = dynamodb.Table(t_name)
    return table.get_item(Key={
        'redirect_url': redirect_url
    }, ProjectionExpression='original_url')


@mock_dynamodb2
def fetch_mock_table():
    migration()


# method to check whether layers have been loaded in properly
def library_loaded():
    return 'congrats! layers have worked properly. Now you can use any home-built boto utils'
