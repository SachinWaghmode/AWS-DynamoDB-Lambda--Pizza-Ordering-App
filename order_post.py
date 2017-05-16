def lambda_handler(event, context):
    import boto3
    import uuid
    
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    
    orderTable = dynamodb.Table('order')
    menuTable = dynamodb.Table('menu')
    
    menu_id=event.get('menu_id')
    customer_name=event.get('customer_name')
    customer_email=event.get('customer_email')
    
    response = orderTable.put_item(
       Item={
            'order_id': str(uuid.uuid1()),
            'menu_id': menu_id,
            'customer_name': customer_name,
            'customer_email': customer_email,
            'order_status': 'Processing'
        }
    )
    
    menutableResponse = menuTable.get_item(
        Key = {
            "menu_id": menu_id
        }
    )
    menuitem = menutableResponse['Item']

    menuselectionOption = ''         
    for index, value in enumerate(menuitem['selection']):
        menuselectionOption += str(index+1) + ". " + value + "  " 

    returnmessageselection = "Hi {" + event.get('customer_name') + "}, please choose one of these selection: " + menuselectionOption
    
    return {
        "message" : returnmessageselection
    }