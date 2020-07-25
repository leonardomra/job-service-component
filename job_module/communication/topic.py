import boto3
import json
import os

class Topic():

    def __init__(self, topic=None):
        self.client = boto3.client(
            'sns',
            region_name=os.environ['AWS_REGION'],
            aws_access_key_id=os.environ['AWS_ACCESS_KEY'],
            aws_secret_access_key=os.environ['AWS_SECRET_KEY']
        )

    
    def broadcastEvent(self, message):
        print('Broadcasting event...', message)
        response = self.client.publish(
            TopicArn=os.environ['JOBS_ARN_TOPIC'],
            Subject='a short subject for your message',
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'
        )
        # Print out the response
        print(response)

