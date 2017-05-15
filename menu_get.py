import boto3
import json
import decimal
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb", region_name='us-west-2')

    table = dynamodb.Table('menu')

    try:
        response = table.get_item(
            Key={
                'menu_id': event['menu_id'],
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Item']
        print("GetItem succeeded:")
        print(json.dumps(item, indent=4))
        return "200 Ok", item