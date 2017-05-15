import boto3
import json

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table('menu')

    response = table.update_item(
        Key={
            'menu_id': event['menu_id']
            },
    UpdateExpression="set selection = :s",
    ExpressionAttributeValues={
        ':s': event['selection']
    },
    ReturnValues="UPDATED_NEW"
    )

    print("UpdateItem succeeded:")
    print(json.dumps(response, indent=4))
    return "200 Ok"