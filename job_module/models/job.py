# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from job_module.models.base_model_ import Model
from job_module import util


class Job(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, user: str=None, label: str=None, description: str=None, kind: str=None, model: str=None, data_source: str=None, data_sample: str=None, status: str=None, output: str=None, task_params: str=None, date_created: datetime=None, date_modified: datetime=None):  # noqa: E501
        """Job - a model defined in Swagger

        :param id: The id of this Job.  # noqa: E501
        :type id: str
        :param user: The user of this Job.  # noqa: E501
        :type user: str
        :param label: The label of this Job.  # noqa: E501
        :type label: str
        :param description: The description of this Job.  # noqa: E501
        :type description: str
        :param kind: The kind of this Job.  # noqa: E501
        :type kind: str
        :param model: The model of this Job.  # noqa: E501
        :type model: str
        :param data_source: The data_source of this Job.  # noqa: E501
        :type data_source: str
        :param data_sample: The data_sample of this Job.  # noqa: E501
        :type data_sample: str
        :param status: The status of this Job.  # noqa: E501
        :type status: str
        :param output: The output of this Job.  # noqa: E501
        :type output: str
        :param date_created: The date_created of this Job.  # noqa: E501
        :type date_created: datetime
        :param date_modified: The date_modified of this Job.  # noqa: E501
        :type date_modified: datetime
        """
        self.swagger_types = {
            'id': str,
            'user': str,
            'label': str,
            'description': str,
            'kind': str,
            'model': str,
            'data_source': str,
            'data_sample': str,
            'status': str,
            'output': str,
            'task_params': str, 
            'date_created': datetime,
            'date_modified': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'user': 'user',
            'label': 'label',
            'description': 'description',
            'kind': 'kind',
            'model': 'model',
            'data_source': 'dataSource',
            'data_sample': 'dataSample',
            'status': 'status',
            'output': 'output',
            'task_params': 'taskParams',  
            'date_created': 'dateCreated',
            'date_modified': 'dateModified'
        }
        self._id = id
        self._user = user
        self._label = label
        self._description = description
        self._kind = kind
        self._model = model
        self._data_source = data_source
        self._data_sample = data_sample
        self._status = status
        self._output = output
        self._task_params = task_params
        self._date_created = date_created
        self._date_modified = date_modified

    @classmethod
    def from_dict(cls, dikt) -> 'Job':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Job of this Job.  # noqa: E501
        :rtype: Job
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Job.


        :return: The id of this Job.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Job.


        :param id: The id of this Job.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user(self) -> str:
        """Gets the user of this Job.


        :return: The user of this Job.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user: str):
        """Sets the user of this Job.


        :param user: The user of this Job.
        :type user: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def label(self) -> str:
        """Gets the label of this Job.


        :return: The label of this Job.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label: str):
        """Sets the label of this Job.


        :param label: The label of this Job.
        :type label: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def description(self) -> str:
        """Gets the description of this Job.


        :return: The description of this Job.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Job.


        :param description: The description of this Job.
        :type description: str
        """

        self._description = description

    @property
    def kind(self) -> str:
        """Gets the kind of this Job.


        :return: The kind of this Job.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        """Sets the kind of this Job.


        :param kind: The kind of this Job.
        :type kind: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501

        self._kind = kind

    @property
    def model(self) -> str:
        """Gets the model of this Job.


        :return: The model of this Job.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this Job.


        :param model: The model of this Job.
        :type model: str
        """

        self._model = model

    @property
    def data_source(self) -> str:
        """Gets the data_source of this Job.


        :return: The data_source of this Job.
        :rtype: str
        """
        return self._data_source

    @data_source.setter
    def data_source(self, data_source: str):
        """Sets the data_source of this Job.


        :param data_source: The data_source of this Job.
        :type data_source: str
        """

        self._data_source = data_source

    @property
    def data_sample(self) -> str:
        """Gets the data_sample of this Job.


        :return: The data_sample of this Job.
        :rtype: str
        """
        return self._data_sample

    @data_sample.setter
    def data_sample(self, data_sample: str):
        """Sets the data_sample of this Job.


        :param data_sample: The data_sample of this Job.
        :type data_sample: str
        """

        self._data_sample = data_sample

    @property
    def status(self) -> str:
        """Gets the status of this Job.


        :return: The status of this Job.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """Sets the status of this Job.


        :param status: The status of this Job.
        :type status: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def output(self) -> str:
        """Gets the output of this Job.


        :return: The output of this Job.
        :rtype: str
        """
        return self._output

    @output.setter
    def output(self, output: str):
        """Sets the output of this Job.


        :param output: The output of this Job.
        :type output: str
        """

        self._output = output

    @property
    def task_params(self) -> str:
        """Gets the output of this Job.


        :return: The output of this Job.
        :rtype: str
        """
        return self._task_params

    @task_params.setter
    def task_params(self, task_params: str):
        """Sets the output of this Job.


        :param output: The output of this Job.
        :type output: str
        """

        self._task_params = task_params

    @property
    def date_created(self) -> datetime:
        """Gets the date_created of this Job.


        :return: The date_created of this Job.
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created: datetime):
        """Sets the date_created of this Job.


        :param date_created: The date_created of this Job.
        :type date_created: datetime
        """
        if date_created is None:
            raise ValueError("Invalid value for `date_created`, must not be `None`")  # noqa: E501

        self._date_created = date_created

    @property
    def date_modified(self) -> datetime:
        """Gets the date_modified of this Job.


        :return: The date_modified of this Job.
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: datetime):
        """Sets the date_modified of this Job.


        :param date_modified: The date_modified of this Job.
        :type date_modified: datetime
        """
        if date_modified is None:
            raise ValueError("Invalid value for `date_modified`, must not be `None`")  # noqa: E501

        self._date_modified = date_modified
