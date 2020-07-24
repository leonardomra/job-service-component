import boto3
import json
from decouple import config as env

class Topic():

    def __init__(self, topic=None):
        print(env('AWS_ACCESS_KEY'))
        print(env('AWS_SECRET_KEY'))
        print(env('JOBS_ARN_TOPIC'))
        self.client = boto3.client(
            'sns',
            region_name=env('AWS_REGION'),
            aws_access_key_id=env('AWS_ACCESS_KEY'),
            aws_secret_access_key=env('AWS_SECRET_KEY')
        )

    
    def broadcastEvent(self, message):
        print('Broadcasting event...', message)
        response = self.client.publish(
            TopicArn=env('JOBS_ARN_TOPIC'),
            Subject='a short subject for your message',
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'
        )
        # Print out the response
        print(response)

