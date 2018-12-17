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


def addepisodeforaclient(client_id, episode=None):  # noqa: E501
    """add an episode

     # noqa: E501

    :param client_id: 
    :type client_id: str
    :param episode: 
    :type episode: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        episode = Episode.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def createcaregiver(caregiver):  # noqa: E501
    """creates a new caregiver object

     # noqa: E501

    :param caregiver: 
    :type caregiver: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        caregiver = Caregiver.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def createpatient(patient):  # noqa: E501
    """creates a new patient object

     # noqa: E501

    :param patient: 
    :type patient: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        patient = Patient.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def editaddressesforaclient(client_id, address):  # noqa: E501
    """add/modify addresses

     # noqa: E501

    :param client_id: 
    :type client_id: str
    :param address: 
    :type address: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        address = Address.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def editpatientinfo(client_id, patient=None):  # noqa: E501
    """add/modify patient info

     # noqa: E501

    :param client_id: 
    :type client_id: str
    :param patient: 
    :type patient: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        patient = Patient.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def editphonenumbersforaclient(client_id, phone_number=None):  # noqa: E501
    """add/modify phonenumbers

     # noqa: E501

    :param client_id: 
    :type client_id: str
    :param phone_number: 
    :type phone_number: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        phone_number = PhoneNumber.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def getaddressesforaclient(client_id):  # noqa: E501
    """gets the active addresses for a client

     # noqa: E501

    :param client_id: 
    :type client_id: str

    :rtype: List[Address]
    """
    return 'do some magic!'


def getcaregiverinfo(client_id):  # noqa: E501
    """gets a caregiver by ID

     # noqa: E501

    :param client_id: 
    :type client_id: str

    :rtype: Caregiver
    """
    return 'do some magic!'


def getcommentforhco(subject_healthcare_provider_id):  # noqa: E501
    """gets the comments for a healthcare provider by ID

     # noqa: E501

    :param subject_healthcare_provider_id: 
    :type subject_healthcare_provider_id: str

    :rtype: List[Comment]
    """
    return 'do some magic!'


def getepisodesforaclient(client_id):  # noqa: E501
    """gets the episodes for a client

     # noqa: E501

    :param client_id: 
    :type client_id: str

    :rtype: List[Episode]
    """
    return 'do some magic!'


def gethealthprofilesforaclient(client_id):  # noqa: E501
    """gets the health profiles for a client

     # noqa: E501

    :param client_id: 
    :type client_id: str

    :rtype: List[HealthProfile]
    """
    return 'do some magic!'


def getmedicationsforaclient(client_id):  # noqa: E501
    """gets the medications for a client

     # noqa: E501

    :param client_id: 
    :type client_id: str

    :rtype: List[Medication]
    """
    return 'do some magic!'


def getpatientinfo(client_id):  # noqa: E501
    """gets a patient by ID

     # noqa: E501

    :param client_id: 
    :type client_id: str

    :rtype: Patient
    """
    return 'do some magic!'


def getphonenumbersforaclient(client_id):  # noqa: E501
    """gets the active phonenumbers for a client

     # noqa: E501

    :param client_id: 
    :type client_id: str

    :rtype: List[PhoneNumber]
    """
    return 'do some magic!'


def list_hc_os():  # noqa: E501
    """List all HCOs

     # noqa: E501


    :rtype: List[HCO]
    """
    return 'do some magic!'


def postcomment(comment):  # noqa: E501
    """creates a new comment

     # noqa: E501

    :param comment: 
    :type comment: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        comment = Comment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def posthealthprofile(client_id, health_profile):  # noqa: E501
    """creates a new healthprofile

     # noqa: E501

    :param client_id: 
    :type client_id: str
    :param health_profile: 
    :type health_profile: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        health_profile = HealthProfile.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def postmedication(client_id, medication):  # noqa: E501
    """creates a new medication

     # noqa: E501

    :param client_id: 
    :type client_id: str
    :param medication: 
    :type medication: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        medication = Medication.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
