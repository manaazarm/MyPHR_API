import connexion
import six

from openapi_server.models.address import Address  # noqa: E501
from openapi_server.models.caregiver import Caregiver  # noqa: E501
from openapi_server.models.comment import Comment  # noqa: E501
from openapi_server.models.episode import Episode  # noqa: E501
from openapi_server.models.hco import HCO  # noqa: E501
from openapi_server.models.health_profile import HealthProfile  # noqa: E501
from openapi_server.models.medication import Medication  # noqa: E501
from openapi_server.models.patient import Patient  # noqa: E501
from openapi_server.models.phone_number import PhoneNumber  # noqa: E501
from openapi_server import util

def addepisodeforaclient(episode=None):  # noqa: E501
    return "it works"