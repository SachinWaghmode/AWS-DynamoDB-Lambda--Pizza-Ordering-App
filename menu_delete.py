def lambda_handler(event, context):
    import boto3
    from botocore.exceptions import ClientError
    
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    
    table = dynamodb.Table('menu')
    
    try:
        response = table.delete_item(
            Key={
                'menu_id': event['menu_id']
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("DeleteItem succeeded:")
        return "200 OK"