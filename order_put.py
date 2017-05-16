def lambda_handler(event, context):
    import boto3
    import datetime
    
    from botocore.exceptions import ClientError
    
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    
    orderTable = dynamodb.Table('order')
    menuTable = dynamodb.Table('menu')
    
    order_id=event.get('order_id')
    input=event.get('input')
    
    orderResponse = orderTable.get_item(
        Key = {
            "order_id": event.get('order_id')
        }
    )
    order = orderResponse['Item']
   
    menu_id=order['menu_id']
    menutableResponse = menuTable.get_item(
        Key = {
            "menu_id": menu_id
        }
    )
    menuitem = menutableResponse['Item']
    if 'orderdetails' in order:
        if 'selection' in order['orderdetails']:
            sizeOptions = menuitem['size']
            sizeSelected = sizeOptions[int(input)-1]
            costOptions = menuitem['price']
            ordercost = costOptions[int(input)-1]
            orderTable.update_item(
            Key = {
                "order_id": order_id
            },
            UpdateExpression = 'set order_status = :val1, orderdetails= :val2',
            ExpressionAttributeValues = {
                ':val1': "Processing",
                ':val2':  {'selection' : order['orderdetails']['selection'],'size' : sizeSelected, 'costs' : ordercost,
                 'order_time' : datetime.datetime.now().strftime("%m-%d-%y@%I:%M:%S")}
            }
        )

        returnmessageCost =  "Your order costs $%s. We will email you when the order is ready. Thank you!" % ordercost
    
    else:
        selectionOptions = menuitem['selection']
        selectionSelected = selectionOptions[int(input)-1] 
        
    
        orderTable.update_item(
            Key = {
                "order_id": order_id
            },
            UpdateExpression = 'set orderdetail = :val1',
            ExpressionAttributeValues = {
                ':val1': {'selection' : selectionSelected}
            }
        )    
    
        sizeOption = ''         
        for index, value in enumerate(menuitem['size']):
            sizeOption += str(index+1) + ". " + value + "  " 
    
        returnmessageCost = "Which size do you want? "  + sizeOption
        
    return returnmessageCost