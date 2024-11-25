import json

def lambda_handler(event, context):
    if event.get("queryStringParameters") and "message" in event["queryStringParameters"]:
        return {
            "statusCode": 200,
            "body": event["queryStringParameters"]["message"]
        }
    elif event.get("body"):
        body = json.loads(event["body"])
        if "message" in body:
            return {
                "statusCode": 200,
                "body": body["message"]
            }
    return {
        "statusCode": 200,
        "body": "Hello World!"
    }
