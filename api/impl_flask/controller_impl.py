import connexion
import six
from datetime import date
import datetime
import hashlib
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

_USER = WebUser()

_HMACKEY = 'hiwuehf983'

def hash_password(passw):
    h= sha256_crypt.hash(passw)
    return h


def list_hc_os():  
    def_HCO = HCO(_DEF_HIC_ID,_DEF_HIC_NAME,_DEF_HIC_CREATION_DATE,_DEF_HIC_DEACTIVATION_DATE,_DEF_HIC_BIN,_DEF_HIC_ORGANIZATION_TYPE)
    HCO_list = [def_HCO]
    return HCO_list

def postcomment(comment):
    return "comment posted"

def generate_ticket(client_id):
    h_input = client_id + _HMACKEY
    return hashlib.sha256(h_input.encode()).hexdigest()

def verify_ticket(claimed_client_id, hash_client_id):
    return generate_ticket(claimed_client_id) == hash_client_id


def get_authenticated(username, password):
    user = firebase.get_user(username,password)
    client_id = user.client_id
    user_id = user.user_id
    user_type = user.type
    if user is not None:
        client_hash = generate_ticket(client_id)
        return {'client_id':client_id, 'user_id':user_id , 'user_type': user_type,'token':client_hash}
    else:
        return 'no user found!' 

    
def get_client_from_user(username, password):
    user = get_authenticated(username,password)
    clnt = firebase.get_client(user)
    return clnt

def get_client_basic_info(client_id,user_id,token):
    bi = []
    if verify_ticket(client_id, token):
        bi = firebase.get_client_basic_info(client_id, user_id)
    return bi

def update_service_language(client_id, service_language,token):
    if verify_ticket(client_id, token):
        message = firebase.update_service_language(client_id, service_language)
    return message

def get_client_health_profile(client_id,token):
    if verify_ticket(client_id, token):
        hplist_dto = firebase.get_client_health_profile(client_id)
        return hplist_dto
        #return [H.to_dict() for H in hplist_dto]
    else:
        raise Exception('invalid token')

def get_client_contact_info(client_id,is_active,token):
    if verify_ticket(client_id, token):
        addresses = firebase.get_address(is_active,client_id)
        phone_numbers = firebase.get_phone_number(is_active,client_id)
        # addresses = [a.to_dict() for a in firebase.get_address(is_active,client_id)]
        # phone_numbers = [p.to_dict() for p in firebase.get_phone_number(is_active,client_id)]
        emails = firebase.get_email_address(is_active,client_id)
        contact_info = [('addresses',addresses),('phone_numbers',phone_numbers),('emails',emails)]
        return contact_info
    else:
        raise Exception('invalid token')


def get_client_caregiver_info(client_id,is_active,token):
    if verify_ticket(client_id, token):
        # caregivers = [c.to_dict() for c in firebase.get_care_givers(client_id, is_active)]
        caregivers = firebase.get_care_givers(client_id, is_active)
        return caregivers
    else:
        raise Exception('invalid token')

def get_client_caregiver_contact_info(client_id, is_active, token, caregiver_client_id):
    if verify_ticket(client_id, token):
        addresses = firebase.get_address(is_active,caregiver_client_id)
        phone_numbers = firebase.get_phone_number(is_active,caregiver_client_id)
        emails = firebase.get_email_address(is_active,caregiver_client_id)
        contact_info = [('addresses',addresses),('phone_numbers',phone_numbers),('emails',emails)]
        return contact_info
    else:
        raise Exception('invalid token')

def get_client_physicians(client_id,episode_type,token):
    if verify_ticket(client_id, token):
        episodes_dict = firebase.get_client_episodes(client_id,episode_type)
        # output_dict = {K: {
        #     'episode': V[0].to_dict(), 
        #     'hic': V[1].to_dict(), 
        #     'dr': V[2].to_dict()} for K,V in episodes_dict.items()}
        
        return episodes_dict
    else:
        raise Exception('invalid token')

def get_client_episodes(client_id,token, episode_type = 'All'):
    if verify_ticket(client_id, token):
        episodes_dict = firebase.get_client_episodes(client_id,episode_type)
        # output_dict = {K: {
        #     'episode': V[0].to_dict(), 
        #     'hic': V[1].to_dict(), 
        #     'dr': V[2].to_dict()} for K,V in episodes_dict.items()}
        
        return episodes_dict
    else:
        raise Exception('invalid token')

def get_client_episodes_in_range(client_id,token, start_date, end_date= datetime.datetime.now):
    try:
        if verify_ticket(client_id, token):
            episodes_dict = firebase.get_client_episodes_in_range(client_id, start_date,end_date)
            return episodes_dict
    except Exception as e:
        print(e)

def add_diet(client_id, diet,token):
    try:
        if verify_ticket(client_id, token):
            diet_dict = firebase.add_diet(client_id, diet)
            return diet_dict
    except Exception as e:
        print(e)

def add_advance_directive (client_id, ad,token):
    try:
        if verify_ticket(client_id, token):
            ad_dict = firebase.add_advance_directive(client_id, ad)
            return ad_dict
    except Exception as e:
        print(e)

def edit_client_contact_info(client_id, token, category,field,text,contact_type):
    try:
        if verify_ticket(client_id, token):
            ci = firebase.edit_client_contact_info(client_id, category,field,text,contact_type)
            return ci
    except Exception as e:
        print(e)

def edit_caregivers(client_id, token, name, relationship, is_primary):
    try:
        if verify_ticket(client_id, token):
            ci = firebase.edit_caregivers(client_id, name, relationship, is_primary)
            return ci
    except Exception as e:
        print(e)

def edit_caregiver_contacts(client_id, token, category,field,text,contact_type,is_primary):
    try:
        if verify_ticket(client_id, token):
            ci = firebase.edit_caregiver_contacts(client_id, category,field,text,contact_type,is_primary)
            return ci  
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print("[main] reached here")