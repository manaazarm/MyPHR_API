import sys
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from passlib.hash import sha256_crypt
from datetime import date
import uuid

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
    

def get_client_health_profile(client_id):
    health_profiles = []
    try:
        query_ref = h_profile_ref.where('client_id','==',client_id)
        hp_list = list(query_ref.get())
        if len(hp_list) >= 1:
            for hp in hp_list:
                hp_dict = hp.to_dict()
                if hp_dict.get('end_date') == None:
                    health_profiles.append(hp_dict)
            return health_profiles
        else:
            print('No health profile found')
            return []
    except Exception as e:
        print(e)
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
                addresses.append(ad_dict)
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
                numbers.append(nu_dict)
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
                caregivers.append(cg_dict)
            return caregivers
        else:
            print('no caregiver found')
            return []
    except Exception as e:
        print(e)
        raise

def get_client_episodes(client_id, episode_type='All'):
    try: 
        episodes = []
        
        if episode_type == 'All':
           query_ref = episode_ref.where('client_id','==',client_id)
        elif episode_type == 'Physician':
            query_ref = episode_ref.where('client_id','==',client_id).where('episode_type','==',episode_type).where('is_active', '==', True)
        else:
            query_ref = episode_ref.where('client_id','==',client_id).where('episode_type','==',episode_type)
        
        episodes_list = list(query_ref.get())
        if len(episodes_list)>=1:
            for e in episodes_list:
                e_dict = e.to_dict()
                
                hicl = list(hic_ref.where('hic_id','==',e_dict['healthcare_provider_id']).get())
                hicd = hicl[0].to_dict()
                data = {'Healthcare_provider_name': hicd['name']}
                e_dict.update(data)
                    
                drl = list(hic_ref.where('hic_id','==',e_dict['physician_id']).get())
                drd = drl[0].to_dict()
                data = {'Physician name': drd['name']}
                e_dict.update(data)
                episodes.append(e_dict)
            return episodes
        else: 
            print('no episode found!')
            return []
    except Exception as e:
        print( e)
        raise

def get_client_episodes_in_range(client_id,start_date,end_date, episode_type='All'):
    try: 
        episodes = []
        
        if episode_type == 'All':
           query_ref = episode_ref.where('client_id','==',client_id).where('start_date','>=',start_date).where('start_date','<=',end_date)
        elif episode_type == 'Physician':
            query_ref = episode_ref.where('client_id','==',client_id).where('episode_type','==',episode_type).where('start_date','>=',start_date).where('start_date','<=',end_date)
        else:
            query_ref = episode_ref.where('client_id','==',client_id).where('episode_type','==',episode_type).where('start_date','>=',start_date).where('start_date','<=',end_date)
        
        episodes_list = list(query_ref.get())
        if len(episodes_list)>=1:
            for e in episodes_list:
                e_dict = e.to_dict()
                
                hicl = list(hic_ref.where('hic_id','==',e_dict['healthcare_provider_id']).get())
                hicd = hicl[0].to_dict()
                data = {'Healthcare_provider_name': hicd['name']}
                e_dict.update(data)
                    
                drl = list(hic_ref.where('hic_id','==',e_dict['physician_id']).get())
                drd = drl[0].to_dict()
                data = {'Physician name': drd['name']}
                e_dict.update(data)
                episodes.append(e_dict)
            return episodes
        else: 
            print('no episode found!')
            return []
    except Exception as e:
        print( e)
        raise

def update_service_language(client_id, service_language):
    try:
        query_ref = client_ref.where('client_id','==',client_id)
        c_list = list(query_ref.get())
        c = c_list[0]
        document_id = c.id
        cd = c.to_dict()
        cd['service_language']=service_language
        client_ref.document(document_id).set(cd)
        return 'Service language updated successfully :-D'
    except Exception as e:
        print (e)

def add_diet(client_id, diet):
    try: 
        data = {
            'health_profile_id': str(uuid.uuid4()),
            'client_id': client_id,
            'start_date': date.today().strftime('%d-%b-%Y (%H:%M:%S.%f)'),
            'type': 'Dietary Regimen',
            'name': diet
        }
        h_profile_ref.add(data)
        return '{} dietary regiman is successfully added!'.format(diet)
    except Exception as e:
        print(e)


