import connexion
import sys
import six
import json
import os
from job_module.models.health import Health  # noqa: E501
from job_module import util
from flask import jsonify
from orcomm_module.orcommunicator import ORCommunicator

orcomm = ORCommunicator(os.environ['AWS_REGION'], os.environ['AWS_ACCESS_KEY'], os.environ['AWS_SECRET_KEY'])

def jobs_health_get():  # noqa: E501
    """jobs_health_get

    Check health of service. # noqa: E501


    :rtype: Health
    """
    response = {
        "status" : 'Job Service Component is up!'
    }
    print('Heatlh check executed.', flush=True)
    return jsonify(response)

def topic_confirm_post(body=None, x_amz_sns_message_type=None, x_amz_sns_message_id=None, x_amz_sns_topic_arn=None):  # noqa: E501
    """topic_confirm_post

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

    if not connexion.request.is_json:
        body = json.loads(body)
        if 'Message' in body:
            try:
                body['Message'] = json.loads(body['Message'])
            except json.decoder.JSONDecodeError:
                print('Message cannot be converted into JSON')
    response = orcomm.getTopic(os.environ['JOBS_ARN_TOPIC']).tuneTopic(connexion.request.headers, body)
    if response.Type == 'SubscriptionConfirmation':
        return orcomm.getTopic(os.environ['JOBS_ARN_TOPIC']).confirmSubscription(response)
    else:
        return 'bad request!', 400