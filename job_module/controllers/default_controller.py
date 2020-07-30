import connexion
import sys
import six
import json

from job_module.models.health import Health  # noqa: E501
from job_module import util
from job_module.communication.topic import Topic
from flask import jsonify

topicSNS = Topic()

def health_get():  # noqa: E501
    """health_get

    Check health of service. # noqa: E501


    :rtype: Health
    """
    response = {
        "status" : 'Job Service Component is up!'
    }
    print('Heatlh check executed.', flush=True)
    return jsonify(response)

def health_post(body=None, x_amz_sns_message_type=None, x_amz_sns_message_id=None, x_amz_sns_topic_arn=None):  # noqa: E501
    """health_post

    Check health of subscription. # noqa: E501

    :param body: The subscription confirmation message is a POST message with a message body that contains a JSON document with name-value pairs.
    :type body: dict | bytes
    :param x_amz_sns_message_type: The type of message. The possible values are SubscriptionConfirmation, Notification, and UnsubscribeConfirmation.
    :type x_amz_sns_message_type: str
    :param x_amz_sns_message_id: A Universally Unique Identifier, unique for each message published. For a notification that Amazon SNS resends during a retry, the message ID of the original message is used.
    :type x_amz_sns_message_id: str
    :param x_amz_sns_topic_arn: The Amazon Resource Name (ARN) for the topic that this message was published to.
    :type x_amz_sns_topic_arn: str

    :rtype: Health
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    else:
        body =  json.loads(body)
    response = {
        "status" : body
    }
    print(response, flush=True)
    x_amz_sns_message_id = connexion.request.headers['x_amz_sns_message_id']
    x_amz_sns_topic_arn = connexion.request.headers['x_amz_sns_topic_arn']
    return topicSNS.confirmSubscription(x_amz_sns_topic_arn, x_amz_sns_message_id)