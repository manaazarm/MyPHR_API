import sys
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from passlib.hash import sha256_crypt

from google.cloud import firestore as fs

# hack: for sibling imports, add the parent path to sys.path
dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(dir_path)

from openapi_server.models.web_user import WebUser
from openapi_server.models.health_profile import HealthProfile
from openapi_server.models.address import Address 
from openapi_server.models.phone_number import PhoneNumber
from openapi_server.models.caregiver import Caregiver
from openapi_server.models.episode import Episode
from openapi_server.models.organization_type import OrganizationType
from openapi_server.models.hco import HCO
from openapi_server.models.physician import Physician


cred = credentials.Certificate('/Users/mana/Dropbox/UO_Shared_With_Mana/Prototype Stuff/myphr-api-firebase-adminsdk-qfh5m-73a706148a.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

user_ref = db.collection('web_user')
client_ref = db.collection('client')
h_profile_ref = db.collection('health_profile')
audit_ref = db.collection('audit_trail')
contact_info_ref = db.collection('contact_info')
episode_ref = db.collection('episodes')
hic_ref = db.collection('hic')

def get_user(username, password):
    #grabs the user matching this username and password from the database
    try:
        query_ref = user_ref.where('hcn','==',username)
        usr = query_ref.get()
        doc_list = list(usr)
        if len(doc_list) >= 1:
            doc = doc_list[0]
            doc_dict = doc.to_dict()
            h=doc_dict['password']
            if sha256_crypt.verify(password,h):
                user = WebUser(
                    client_id=doc_dict['client_id'], 
                    user_id=doc_dict['user_id'],
                    created_date=doc_dict['created_date'],
                    hcn=doc_dict['hcn'],
                    password=doc_dict['password'],
                    status=doc_dict['status'],
                    type=doc_dict['type'])
                return user
            else:
                print('password is wrong!')       
    except:
        print(u'No such client!')
        raise

if __name__ == '__main__':
    get_user('H7777666699','mypass')

def get_client(user):
    user = WebUser()
    #hcn = user.hcn
    client_id = user.client_id
    query_ref = client_ref.where('client_id','==',client_id)
    clnt = query_ref.get()
    return clnt


def get_client_basic_info(client_id, user_id):
    try:
        query_ref = client_ref.where('client_id','==',client_id)
        bi_list = list(query_ref.get())
        bi = bi_list[0].to_dict()

        query_ref2 = audit_ref.where('user_id', '==', user_id).order_by('access_date', direction=fs.Query.DESCENDING).limit(1)
        last_record = list(query_ref2.get())
        last_access_date = last_record[0].get('access_date')
        bi['last_access_date']= last_access_date
        return bi
    except Exception as e:
        print(e)
        print('No such document!')
    

def get_client_health_profile(client_id):
    health_profiles = []
    try:
        query_ref = h_profile_ref.where('client_id','==',client_id)
        # .where('end_date','==','2200-01-01')
        hp_list = list(query_ref.get())
        if len(hp_list) >= 1:
            for hp in hp_list:
                hp_dict = hp.to_dict()
                health_profile = HealthProfile(
                    health_profile_id=hp_dict['health_profile_id'], 
                    client_id=hp_dict['client_id'], 
                    name=hp_dict['name'], 
                    code=hp_dict['code'], 
                    start_date=hp_dict['start_date'], 
                    end_date=hp_dict['end_date'], 
                    diagnosing_healthcare_provider_id=hp_dict['diagnosing_healthcare_provider_id'], 
                    is_activity_impediment=hp_dict['is_activity_impediment'], 
                    is_risk_and_safety_issue=hp_dict['is_risk_and_safety_issue'], 
                    is_allergy=hp_dict['is_allergy'], 
                    is_health_condition=hp_dict['is_health_condition']
                    )        
                
                health_profiles.append(health_profile)
            return health_profiles
        else:
            print('No health profile found')
            return []
    except:
        print('could not connect to database')
        raise

def get_address(is_active, client_id= None, healthcare_provider_id= None ):
    try:
        query_ref = None
        addresses = []
        if client_id != None:
            query_ref = contact_info_ref.where('client_id','==',client_id).where('category','==','address').where('is_active','==', is_active)
        elif healthcare_provider_id != None: 
            query_ref = contact_info_ref.where('healthcare_provider_id').where('category','==','address').where('is_active','==',is_active)
        else:
            print('should specify either a client_id or healthcare_provider_id')
        address_list = list(query_ref.get())
        if len(address_list)>=1:
            for ad in address_list:
                ad_dict = ad.to_dict()
                address = Address(
                    address_id = ad_dict['contact_id'],
                    address_type=ad_dict['type'],
                    client_id=ad_dict['client_id'],
                    healthcare_provider_id=ad_dict['healthcare_provider_id'],
                    is_active=ad_dict['is_active'],
                    start_date=ad_dict['start_date'],
                    end_date=ad_dict['end_date'],
                    country=ad_dict['country'],
                    city=ad_dict['city'],
                    street_type=ad_dict['street_type'],
                    street_name=ad_dict['street_name'],
                    street_number=ad_dict['street_number'],
                    unit_number=ad_dict['unit_number'],
                    postal_code=ad_dict['postal_code']
                )
                addresses.append(address)
            return addresses
        else:
            print('No address found')
            return []
    except:
        print('could not connect to database')
        raise
            
def get_phone_number(is_active, client_id= None, healthcare_provider_id= None):
    try:
        query_ref = None
        numbers = []
        if client_id != None:
            query_ref = contact_info_ref.where('client_id','==',client_id).where('category','==','phone').where('is_active','==',is_active)
        elif healthcare_provider_id != None:
            query_ref = contact_info_ref.where('healthcare_provider_id').where('category','==','phone').where('is_active','==',is_active)
        else:
            print('should specify either a client_id or healthcare_provider_id')
        phone_list = list(query_ref.get())
        if len(phone_list)>=1:
            for nu in phone_list:
                nu_dict = nu.to_dict()
                phone = PhoneNumber(
                    phone_num_id = nu_dict['contact_id'],
                    type=nu_dict['type'],
                    client_id=nu_dict['client_id'],
                    healthcare_provider_id=nu_dict['healthcare_provider_id'],
                    is_active=nu_dict['is_active'],
                    start_date=nu_dict['start_date'],
                    end_date=nu_dict['end_date'],
                    country_code=nu_dict['country_code'],
                    number=nu_dict['number']
                )
                numbers.append(phone)
            return numbers
        else:
            print('No phone number found')
            return []
    except:
        print('could not connect to database')
        raise

def get_email_address(is_active, client_id= None, healthcare_provider_id= None):
    try:    
        query_ref = None
        emails = []
        if client_id != None:
            query_ref = contact_info_ref.where('client_id','==',client_id).where('category','==','email').where('is_active','==',is_active)
        elif healthcare_provider_id != None:
            query_ref = contact_info_ref.where('healthcare_provider_id').where('category','==','email').where('is_active','==',is_active)
        else:
            print('should specify either a client_id or healthcare_provider_id')
        email_list = list(query_ref.get())
        if len(email_list)>=1:
            for em in email_list:
                email_dict = em.to_dict()
                email = email_dict['email_address']
                emails.append(email)
            return emails
        else:
            print('No phone number found')
            return []
    except:
        print('could not connect to database')
        raise

def get_care_givers(client_id,is_active):
    try:
        caregivers=[]
        query_ref = client_ref.where('caregiver_of_client_id','==',client_id).where('is_active','==',is_active)
        caregiver_list = list(query_ref.get())
        if len(caregiver_list)>= 1:
            for cg in caregiver_list:
                cg_dict = cg.to_dict()
                caregiver = Caregiver(
                    client_id = cg_dict['client_id'],
                    firstname = cg_dict['firstname'],
                    surname = cg_dict['surname'],
                    gender = cg_dict['gender'],
                    dob = cg_dict['dob'],
                    service_language = cg_dict['service_language'],
                    profile_start_date = cg_dict['profile_start_date'],
                    profile_end_date = cg_dict['profile_end_date'],
                    relationship = cg_dict['relationship'],
                    is_active = cg_dict['is_active'],
                    is_primary_caregiver = cg_dict['is_primary_caregiver'],
                    caregiver_of_client_id = cg_dict['caregiver_of_client_id']
                )
                caregivers.append(caregiver)
            return caregivers
        else:
            print('no caregiver found')
            return []
    except Exception as e:
        print(e)
        raise

def get_client_episodes(client_id, episode_type='All'):
    try: 
        episodes = {}
        
        if episode_type == 'All':
           query_ref = episode_ref.where('client_id','==',client_id)
        elif episode_type == 'Physician':
            query_ref = episode_ref.where('client_id','==',client_id).where('episode_type','==',episode_type).where('is_active', '==', True)
        else:
            query_ref = episode_ref.where('client_id','==',client_id).where('episode_type','==',episode_type)
        
        caregiver_list = list(query_ref.get())
        if len(caregiver_list)>=1:
            for e in caregiver_list:
                e_dict = e.to_dict()
                episode = Episode(
                    episode_id = e_dict['episode_id'],
                    client_id = e_dict['client_id'],
                    healthcare_provider_id = e_dict['healthcare_provider_id'],
                    start_date = e_dict['start_date'],
                    end_date = e_dict['end_date'],
                    is_active = e_dict['is_active'],
                    episode_type = e_dict['episode_type'],
                    physician_id = e_dict['physician_id']
                )
                
                hicl = list(hic_ref.where('hic_id','==',episode.healthcare_provider_id).get())
                if len(hicl)>=1:
                    hicd = hicl[0].to_dict()
                    hic = HCO(
                        healthcare_provider_id = hicd['hic_id'],
                        name = hicd['name'],
                        start_date = hicd['start_date'],
                        end_date = hicd['end_date'],
                        bin = hicd['bin'],
                        organization_type = hicd['organization_type']
                    )

                drl = list(hic_ref.where('hic_id','==',episode.physician_id).get())
                drd = drl[0].to_dict()
                dr = Physician(
                    healthcare_provider_id=drd['hic_id'], 
                    name=drd['name'], 
                    start_date=drd['start_date'], 
                    end_date=drd['end_date'], 
                    firstname=drd['firstname'], 
                    surname=drd['surname'], 
                    specialty=drd['specialty'], 
                    license_number=drd['license_number'], 
                    license_date=drd['license_date']
                )
                episodes[episode.episode_id] = (episode,hic,dr)
            return episodes
        else: 
            print('no episode found!')
            return []
    except Exception as e:
        print( e)
        raise

def get_client_episodes_in_range(client_id,start_date,end_date, episode_type='All'):
    try: 
        episodes = {}
        
        if episode_type == 'All':
           query_ref = episode_ref.where('client_id','==',client_id).where('start_date','>=',start_date).where('start_date','<=',end_date)
        elif episode_type == 'Physician':
            query_ref = episode_ref.where('client_id','==',client_id).where('episode_type','==',episode_type).where('start_date','>=',start_date).where('start_date','<=',end_date)
        else:
            query_ref = episode_ref.where('client_id','==',client_id).where('episode_type','==',episode_type).where('start_date','>=',start_date).where('start_date','<=',end_date)
        
        caregiver_list = list(query_ref.get())
        if len(caregiver_list)>=1:
            for e in caregiver_list:
                e_dict = e.to_dict()
                episode = Episode(
                    episode_id = e_dict['episode_id'],
                    client_id = e_dict['client_id'],
                    healthcare_provider_id = e_dict['healthcare_provider_id'],
                    start_date = e_dict['start_date'],
                    end_date = e_dict['end_date'],
                    is_active = e_dict['is_active'],
                    episode_type = e_dict['episode_type'],
                    physician_id = e_dict['physician_id']
                )
                
                hicl = list(hic_ref.where('hic_id','==',episode.healthcare_provider_id).get())
                if len(hicl)>=1:
                    hicd = hicl[0].to_dict()
                    hic = HCO(
                        healthcare_provider_id = hicd['hic_id'],
                        name = hicd['name'],
                        start_date = hicd['start_date'],
                        end_date = hicd['end_date'],
                        bin = hicd['bin'],
                        organization_type = hicd['organization_type']
                    )

                drl = list(hic_ref.where('hic_id','==',episode.physician_id).get())
                drd = drl[0].to_dict()
                dr = Physician(
                    healthcare_provider_id=drd['hic_id'], 
                    name=drd['name'], 
                    start_date=drd['start_date'], 
                    end_date=drd['end_date'], 
                    firstname=drd['firstname'], 
                    surname=drd['surname'], 
                    specialty=drd['specialty'], 
                    license_number=drd['license_number'], 
                    license_date=drd['license_date']
                )
                episodes[episode.episode_id] = (episode,hic,dr)
            return episodes
        else: 
            print('no episode found!')
            return []
    except Exception as e:
        print( e)
        raise