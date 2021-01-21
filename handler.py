import json


def get_joke(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "joke": 'i work 1'
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response