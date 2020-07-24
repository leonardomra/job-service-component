# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from job_module.models.job import Job  # noqa: E501
from job_module.test import BaseTestCase


class TestJobsController(BaseTestCase):
    """JobsController integration test stubs"""

    def test_jobs_get(self):
        """Test case for jobs_get

        
        """
        query_string = [('limit', 100)]
        response = self.client.open(
            '/openresearch/job-ai/1.0.0/jobs',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_id_delete(self):
        """Test case for jobs_id_delete

        
        """
        response = self.client.open(
            '/openresearch/job-ai/1.0.0/jobs/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_id_get(self):
        """Test case for jobs_id_get

        
        """
        response = self.client.open(
            '/openresearch/job-ai/1.0.0/jobs/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_id_put(self):
        """Test case for jobs_id_put

        
        """
        headers = [('label', 'label_example'),
                   ('description', 'description_example'),
                   ('status', 'status_example'),
                   ('output', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/openresearch/job-ai/1.0.0/jobs/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jobs_post(self):
        """Test case for jobs_post

        
        """
        headers = [('label', 'label_example'),
                   ('description', 'description_example'),
                   ('kind', 'kind_example'),
                   ('model', '38400000-8cf0-11bd-b23e-10b96e4ef00d'),
                   ('data_source', '38400000-8cf0-11bd-b23e-10b96e4ef00d'),
                   ('data_sample', '38400000-8cf0-11bd-b23e-10b96e4ef00d'),
                   ('task', 'task_example'),
                   ('user', '38400000-8cf0-11bd-b23e-10b96e4ef00d'),
                   ('status', 'waiting')]
        response = self.client.open(
            '/openresearch/job-ai/1.0.0/jobs',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
