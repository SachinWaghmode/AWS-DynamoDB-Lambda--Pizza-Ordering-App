def lambda_handler(event, context):
    import boto3
    import datetime
    
    from botocore.exceptions import ClientError
    
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    
    orderTable = dynamodb.Table('order')
    menuTable = dynamodb.Table('menu')
    
    order_id=event.get('order_id')
    
    try:
       ordersResponse = orderTable.get_item(
            Key = {
                "order_id": order_id
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        order = ordersResponse['Item']
        return order