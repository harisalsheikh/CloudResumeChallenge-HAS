import boto3

def lambda_handler(event, context):
    
    client = boto3.resource("dynamodb")
    table = client.Table("CloudResumeChallenge")
    
    count_id = table.scan()["Items"]
    
    count_list = []
    
    for count in count_id: 
        count_list += count_id["Counter"]
    
    return count_list