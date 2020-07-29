import connexion
import six

from job_module.models.health import Health  # noqa: E501
from job_module import util


def health_get():  # noqa: E501
    """health_get

    Check health of service. # noqa: E501


    :rtype: Health
    """
    print('Got health request!')
    return 'Job Service Component is up!'