import boto3
import json
import time
from orcomm_module.oritem import ORItem

class ORQueue():

    def __init__(self, AWS_REGION=None, AWS_ACCESS_KEY=None, AWS_SECRET_KEY=None, QUEUE_NAME=None):
        session  = boto3.Session(
            region_name=AWS_REGION,
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        sqs = session.resource('sqs')
        self.queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)

    def pushItem(self, oritem):
        return self.queue.send_message(MessageBody=oritem.MessageBody, MessageAttributes=oritem.MessageAttributes, MessageGroupId=str(int(time.time())))
        
    def pullItems(self, messageAttributeNames=[], limit=None, deleteMsgs=False):
        messages = self.queue.receive_messages(MessageAttributeNames=messageAttributeNames, MaxNumberOfMessages=limit)
        items = []
        for message in messages:
            item = ORItem()
            item.MessageAttributes = message.message_attributes
            item.Attributes = message.attributes
            item.MessageBody = message.body
            item.QueueUrl = message.queue_url
            item.MessageId = message.message_id
            item.ReceiptHandle = message.receipt_handle
            item.MessageIsActive = not deleteMsgs
            if deleteMsgs:
                message.delete()
            items.append(item)
        return items

    def getResource(self):
        return self.queue