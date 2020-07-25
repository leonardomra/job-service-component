import connexion
import six

from flask import jsonify

from job_module.models.job import Job  # noqa: E501
from job_module import util
from job_module.dbhandler.mysql_handler import MySQLHandler
from job_module.communication.topic import Topic

import uuid
import time  


topicSNS = Topic()

def jobs_get(limit=None):  # noqa: E501
    """jobs_get

    Obtain information about jobs. # noqa: E501

    :param limit: The amount of jobs to be returned.
    :type limit: int

    :rtype: List[Job]
    """
    return 'jobs'


def jobs_id_delete(id):  # noqa: E501
    """jobs_id_delete

    Delete a job. # noqa: E501

    :param id: Id of job.
    :type id: 

    :rtype: Job
    """
    return 'do some magic!'


def jobs_id_get(id):  # noqa: E501
    """jobs_id_get

    Obtain information about a specific job. # noqa: E501

    :param id: Id of job.
    :type id: 

    :rtype: Job
    """
    return 'do some magic!'


def jobs_id_put(id, label=None, description=None, status=None, output=None):  # noqa: E501
    """jobs_id_put

    Modify a new job. # noqa: E501

    :param id: Id of job.
    :type id: 
    :param label: Label of job.
    :type label: str
    :param description: Description of job.
    :type description: str
    :param status: Status of job.
    :type status: str
    :param output: Results of job.
    :type output: 

    :rtype: Job
    """
    return 'do some magic!'


def jobs_post(label=None, kind=None, task=None, user=None, description=None, model=None, data_source=None, data_sample=None, status=None, date_created=None, date_modified=None):
    """jobs_post

    Create a new job. # noqa: E501

    :param label: Label of job.
    :type label: str
    :param kind: Type of job.
    :type kind: str
    :param task: Type of AI Task.
    :type task: str
    :param user: Id of user.
    :type user: 
    :param description: Description of job.
    :type description: str
    :param model: Model of AI Task.
    :type model: 
    :param data_source: Data source for training AI model.
    :type data_source: 
    :param data_sample: Data sample to be analysed with AI model.
    :type data_sample: 
    :param status: Status of task.
    :type status: str

    :rtype: Job
    """
    job = Job()
    job.id = str(uuid.uuid4())
    label = connexion.request.headers['label']
    job.label = label
    kind = connexion.request.headers['kind']
    job.kind = kind
    user = connexion.request.headers['user']
    job.user = user
    task = connexion.request.headers['task']
    job.task = task
    try:
        description = connexion.request.headers['description']
        job.description = description
    except Exception:
        pass
    try:
        model = connexion.request.headers['model']
        job.model = model
    except Exception:
        pass
    try:
        data_source = connexion.request.headers['dataSource']
        job.data_source = data_source
    except Exception:
        pass
    try:
        data_sample = connexion.request.headers['dataSample']
        job.data_sample = data_sample
    except Exception:
        pass
    try:
        status = connexion.request.headers['status']
    except Exception:
        status = 'waiting'
    job.status = status
    
    # validate job task
    if job.task == 'train':
        # requires job.data_source
        if job.data_source is None:
            return 'For analysis jobs, a data source should be passed.', 406
        if not isValidUUID(job.data_source):
            return 'For analysis jobs, a data source should be passed with correct UUID.', 406 
    elif job.task == 'analyse':
        # requires job.model & job.data_sample
        if job.model is None or job.data_sample is None:
            return 'For training jobs, a model and sample should be passed.', 406 
        if not isValidUUID(job.model) or not isValidUUID(job.data_sample):
            return 'For training jobs, a model and sample should be passed with correct UUID.', 406 

    # store persistent data
    db = MySQLHandler(os.environ['MYSQL_USER'], os.environ['MYSQL_PASSWORD'], os.environ['MYSQL_HOST'], os.environ['MYSQL_DATABASE'])
    add_job = ("INSERT INTO Job "
               "(description, kind, label, status, user, id, task, model, dataSample, dataSource) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    data_job = (job.description, job.kind, job.label, job.status, job.user, job.id, job.task, job.model, job.data_sample, job.data_source)
    db.add(add_job, data_job)
    
    
    topicSNS.broadcastEvent({ "msg": "hello world!" })

    # response
    return jsonify(job)


def isValidUUID(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False
