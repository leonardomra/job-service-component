from orcomm_module.orevent import OREvent 
from flask import jsonify

class ORTopic():

    def __init__(self, _client = None):
        self.client = _client

    def broadcastEvent(self, response):
        self.client.publish(
            TopicArn=response.TopicArn,
            Subject=response.Subject,
            Message=json.dumps(response.Message),
            MessageStructure=response.MessageStructure
        )
        return jsonify(response.summarize())

    def tuneTopic(self, headers, body):        
        e = OREvent()
        if 'x-amz-sns-message-type' in headers:
            e.Type = headers['x-amz-sns-message-type']
        if 'x-amz-sns-message-id' in headers:
            e.MessageId = headers['x-amz-sns-message-id']
        if 'x-amz-sns-topic-arn' in headers:
            e.TopicArn = headers['x-amz-sns-topic-arn']
        if 'x-amz-sns-subscription-arn' in headers:
            e.SubscriptionArn = headers['x-amz-sns-subscription-arn']
        if 'Timestamp' in body:
            e.Timestamp = body['Timestamp']
        if 'SignatureVersion' in body:
            e.SignatureVersion = body['SignatureVersion']
        if 'Signature' in body:
            e.Signature = body['Signature']
        if 'SigningCertURL' in body:
            e.SigningCertURL = body['SigningCertURL']
        if 'UnsubscribeURL' in body:
            e.UnsubscribeURL = body['UnsubscribeURL']  
        if 'Token' in body:
            e.Token = body['Token']
        if 'Subject' in body:
            e.Subject = body['Subject']
        if 'Message' in body:
            e.Message = body['Message']
        return e

    def confirmSubscription(self, response):
        return self.client.confirm_subscription(
            TopicArn = response.TopicArn,
            Token = response.Token,
        )

    def unsubscribe(self, response):
        return self.client.unsubscribe(
            SubscriptionArn = response.SubscriptionArn,
        )