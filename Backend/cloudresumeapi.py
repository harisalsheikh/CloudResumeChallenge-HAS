import boto3


##Create a resource for the table
dynamodb = boto3.resource('dynamodb')
    
##Variable to store the table 
table = dynamodb.Table('CloudResumeChallenge')

getMethod = 'GET'
patchMethod = 'PATCH'
getId = '/getid'

def lambda_handler(event, context):

    httpMethod = event['httpMethod']
    path = event['path']

    ##Get Id from table 
    if httpMethod == getMethod and path == getId:
        response = table.get_item(
            Key = {
                'Id': event['Id'],
                'Counter': event['Counter']
            }
        )
    ##starting with only getting GET response 
    return {
        'statusCode' : response['ResponseMetadata']['HTTPStatusCode'], 
        'body' : 'Record' + event['Id']
    }

    ##TODO: PUT Response to update DynamoDB

