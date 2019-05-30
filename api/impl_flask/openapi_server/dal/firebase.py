import sys
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from passlib.hash import sha256_crypt

# hack: for sibling imports, add the parent path to sys.path
dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(dir_path)

from openapi_server.models.web_user import WebUser
from openapi_server.models.health_profile import HealthProfile


cred = credentials.Certificate('/Users/mana/Dropbox/UO_Shared_With_Mana/Prototype Stuff/myphr-api-firebase-adminsdk-qfh5m-73a706148a.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

user_ref = db.collection('web_user')
client_ref = db.collection('client')
h_profile_ref = db.collection('health_profile')

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
                user = WebUser(client_id=doc_dict['client_id'], created_date=doc_dict['created_date'],hcn=doc_dict['hcn'],password=doc_dict['password'],status=doc_dict['status'],type=doc_dict['type'])
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

def get_client_basic_info(client_id):
    query_ref = client_ref.where('client_id','==',client_id)
    bi_list = list(query_ref.get())
    return bi_list

def get_client_health_profile(client_id):
    health_profiles = []
    try:
        query_ref = h_profile_ref.where('client_id','==',client_id)
        # .where('end_date','==','2200-01-01')
        hp_list = list(query_ref.get())
        if len(hp_list) >= 1:
            for hp in hp_list:
                hp_dict = hp.to_dict()
                health_profile = HealthProfile(health_profile_id=hp_dict['health_profile_id'], client_id=hp_dict['client_id'], name=hp_dict['name'], code=hp_dict['code'], start_date=hp_dict['start_date'], end_date=hp_dict['end_date'], diagnosing_healthcare_provider_id=hp_dict['diagnosing_healthcare_provider_id'], is_activity_impediment=hp_dict['is_activity_impediment'], is_risk_and_safety_issue=hp_dict['is_risk_and_safety_issue'], is_allergy=hp_dict['is_allergy'], is_health_condition=hp_dict['is_health_condition'])        
                
                health_profiles.append(health_profile)
            return health_profiles
        else:
            print('No health profile found')
            return []
    except:
        print('could not connect to database')
        raise
    

