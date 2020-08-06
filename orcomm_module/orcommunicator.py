from orcomm_module.ortopic import ORTopic 
from orcomm_module.orchannel import ORChannel
from orcomm_module.orqueue import ORQueue

import boto3

class ORCommunicator():
    
    def __init__(self, AWS_REGION, AWS_ACCESS_KEY, AWS_SECRET_KEY):
        client = boto3.client(
            'sns',
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        self.topic = ORTopic(client)
        self.channel = ORChannel(client)
        self.queue = ORQueue(client)
