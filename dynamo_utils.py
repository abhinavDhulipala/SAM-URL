import boto3 as b3
import boto_utils
from local_constants import AWS_PROFILE
from constants import TABLE_NAME
from datetime import datetime

flask_profile = b3.session.Session(profile_name=AWS_PROFILE)
dynamodb = flask_profile.resource('dynamodb')

"""
This method will execute put requests to dynamo URL table.
@:param original_url -> string of original url
@:param redirect_url -> string of the new url
@:param expiration_date -> string of the expiration date of the redirect url
@:param user -> string of user id
@:param table_name -> string of name of table to be queried (defaults to TABLE_NAME in constants.py)
@:returns -> response of put request if table exists; returns False otherwise
"""
def put(original_url, redirect_url, expiration_date, user, table_name=TABLE_NAME):
    if not boto_utils.table_exists(table_name):
        print("That table does not exist!")
        return False

    table = dynamodb.Table(table_name)
    response = table.put_item(
        Item={
            'redirect_url': redirect_url,
            'original_url': original_url,
            'creation_date': datetime.now().strftime('%s'),
            'expiration_date': expiration_date,
            'user': user
        }
    )

    return response

