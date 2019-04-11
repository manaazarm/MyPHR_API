import connexion
import six
from datetime import date
import datetime
from passlib.hash import sha256_crypt
import openapi_server.dal.firebase as firebase

from openapi_server.models.address import Address  # noqa: E501
from openapi_server.models.client import Client
from openapi_server.models.web_user import WebUser
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

def hash_password(passw):
    h= sha256_crypt.hash(passw)
    return h


def list_hc_os():  
    def_HCO = HCO(_DEF_HIC_ID,_DEF_HIC_NAME,_DEF_HIC_CREATION_DATE,_DEF_HIC_DEACTIVATION_DATE,_DEF_HIC_BIN,_DEF_HIC_ORGANIZATION_TYPE)
    HCO_list = [def_HCO]
    return HCO_list

def postcomment(comment):
    return "comment posted"

def get_authenticated_user(username, password):
    user = firebase.get_user(username,password)
    if user is not None:
        return user
    else:
        return 'no user found!' 

    
def get_client_from_user(username, password):
    return "Here's the client"

def get_client_basic_info(client):
    return "Basic info"

def get_client_health_profile(client, active_status=1):
    return "here's the health profile"

def get_client_contact_info(client, active_status=1):
    return "here's the contact info"

def get_client_caregiver_info(client, active_status=1):
    return "here's the caregiver status"

def get_client_physicians(client, active_status=1):
    return "here's the client's physician"

def get_client_episodes(client, start_date, end_date= datetime.datetime.now):
    return "here's the health profile"

def get_client_alerts(client, active_status =1):
    return "here are the alerts"


if __name__ == '__main__':
    print("[main] reached here")