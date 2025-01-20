import json
import math

import boto3
from time import gmtime, strftime

dynamoDB = boto3.resource('dynamodb')

tb = dynamoDB.Table('PowerOfMathDB')

now = strftime("%a, %d %b %Y %H:%M:%S", gmtime())


def lambda_handler(event, context):
    
    mathResult = math.pow(int(event['base']), int(event['exponent']))
    
    response = tb.put_item()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Your result is ' + str(mathResult))
    }
