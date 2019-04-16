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


cred = credentials.Certificate('/Users/mana/Dropbox/UO_Shared_With_Mana/Prototype Stuff/myphr-api-firebase-adminsdk-qfh5m-73a706148a.json')
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()

user_ref = db.collection('web_user')
client_ref = db.collection('client')

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

#def get_client_basic_info(client):
    

