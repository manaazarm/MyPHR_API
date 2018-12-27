import connexion
import six
from datetime import date

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
from openapi_server.models.organization_type import OrganizationType

_DEF_HIC_ID = '000000001'
_DEF_HIC_NAME = 'MANA DEFAULT HIC'
_DEF_HIC_CREATION_DATE = date(2018,12,17)
_DEF_HIC_DEACTIVATION_DATE = None
_DEF_HIC_BIN = 'HELLO123456'
_DEF_HIC_ORGANIZATION_TYPE = OrganizationType.HOSPITAL


def list_hc_os():  
    def_HCO = HCO(_DEF_HIC_ID,_DEF_HIC_NAME,_DEF_HIC_CREATION_DATE,_DEF_HIC_DEACTIVATION_DATE,_DEF_HIC_BIN,_DEF_HIC_ORGANIZATION_TYPE)
    HCO_list = [def_HCO]
    return HCO_list