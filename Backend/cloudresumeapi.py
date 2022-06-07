import boto3

def lambda_handler(event, context):

    ##Create a resource for the table
    dynamodb = boto3.resource('dynamodb')
    
    ##Variable to store the table 
    table = dynamodb.Table('CloudResumeChallenge')

    ##Get Id from table 
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

