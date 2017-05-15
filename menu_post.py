import boto3
import json
def lambda_handler(event, context):
    

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    
    table = dynamodb.Table('menu')
    selection = event.get('selection')
    size = event.get('size')
    price = event.get('price')
    store_hours = event.get('store_hours')
    
    response = table.put_item(
        Item = {
            'menu_id': event.get('menu_id'),
            'store_name': event.get('store_name'),
            'selection': selection,
            'size': size,
            'price': price,
            'store_hours': store_hours
    
            }
    )

    print("PutItem succeeded:")
    print(json.dumps(response, indent=4))
    return "200 Ok"
