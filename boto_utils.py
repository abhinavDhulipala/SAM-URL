import boto3 as b3
from local_constants import AWS_PROFILE
from constants import TABLE_NAME

flask_profile = b3.session.Session(profile_name=AWS_PROFILE)
dynamodb = flask_profile.resource('dynamodb')

table_name = TABLE_NAME


"""
This method will run a one time DB migration. This method will provision our DynamoDB table.
This method will be used to create a table of urls of the proper schema required for CLUrkel
@:param t_name -> the name of the table to be created 
@:returns -> response indicating success or of table creation
"""
def migration(t_name=table_name):
    if t_name in map(lambda t: t.name, dynamodb.tables.all()):
        print('found prexisting table')
        table = dynamodb.Table(t_name)
        table.delete()
        table.wait_until_not_exists()

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


if __name__ == '__main__':
    response = migration()
    print(response)
    print(type(response) == dynamodb.Table)
    print(response.name == table_name)
