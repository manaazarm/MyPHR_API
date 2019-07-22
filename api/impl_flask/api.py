import flask
from flask.json import jsonify
from flask import request
from openapi_server.models import *
import controller_impl as con 
from datetime import date
from datetime import datetime
import openapi_server.dal.firebase as firebase


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# default HCO to get the first method running before I set up firebase
_DEF_HIC_ID = '000000001'
_DEF_HIC_NAME = 'MANA DEFAULT HIC'
_DEF_HIC_CREATION_DATE = date(2018,12,17)
_DEF_HIC_DEACTIVATION_DATE = None
_DEF_HIC_BIN = 'HELLO123456'
_DEF_HIC_ORGANIZATION_TYPE = OrganizationType.HOSPITAL

# creating a comment object for before I set up firebase
_comment_id= '123345667'
_user_id='777777777'
_subject_healthcare_provider_id=_DEF_HIC_ID
_subject_client_id=None
_comment_date=date(2018,12,27)
_comment_text='Excellent'
_a_comment = Comment(_comment_id, _user_id, _subject_healthcare_provider_id, _subject_client_id, _comment_date, _comment_text)


def __parse_bool(s):
    if s is None:
        return False
    return s.lower() in ('true', '1')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/login', methods=['GET'])
def authenticate():
    username = request.args['username']
    password = request.args['password']
    a = con.get_authenticated(username, password)
    cred = jsonify(a)
    firebase.add_audit_trail(a['client_id'], a['token'], 'login attempt', a['user_id'])
    return cred

@app.route('/basic_info', methods=['GET'])
def get_client_basic_info():
    client_id = request.args['client_id']
    user_id = request.args['user_id']
    token = request.args['token']
    bi = con.get_client_basic_info(client_id,user_id,token)
    return jsonify(bi)

@app.route('/health_profile', methods=['GET'])
def get_client_health_profile():
    client_id = request.args['client_id']
    token = request.args['token']
    hplist = con.get_client_health_profile(client_id,token)
    return jsonify(hplist)

@app.route('/contact_info', methods=['GET'])
def get_contact_info():
    client_id = request.args['client_id']
    is_active = __parse_bool(request.args['is_active'])
    token = request.args['token']
    contact = con.get_client_contact_info(client_id, is_active, token)
    return jsonify(contact)

@app.route('/caregiver', methods=['GET'])
def get_caregiver_info():
    client_id = request.args['client_id']
    token = request.args['token']
    is_active = __parse_bool(request.args['is_active'])
    cgs= con.get_client_caregiver_info(client_id, is_active, token)
    return jsonify(cgs)

@app.route('/caregiver_contact_info', methods=['GET'])
def get_caregiver_contact_info():
    client_id = request.args['client_id']
    token = request.args['token']
    caregiver_client_id = request.args['caregiver_client_id']
    is_active = __parse_bool(request.args['is_active'])
    cgs= con.get_client_caregiver_contact_info(client_id, is_active, token, caregiver_client_id)
    return jsonify(cgs)

@app.route('/physician', methods=['GET'])
def get_client_physicians():
    client_id = request.args['client_id']
    token = request.args['token']
    episode_type = 'Physician'
    episodes = con.get_client_episodes(client_id, token,episode_type)
    return jsonify(episodes)

@app.route('/episodes', methods=['GET'])
def get_client_episodes():
    client_id = request.args['client_id']
    token = request.args['token']
    episodes = con.get_client_episodes(client_id, token)
    return jsonify(episodes)

@app.route('/episodes_by_range', methods=['GET'])
def get_client_episodes_by_range():
    client_id = request.args['client_id']
    token = request.args['token']
    start_date_arg = request.args['start_date']
    start_date = datetime.strptime(start_date_arg,'%Y-%m-%d')
    end_date_arg = request.args['end_date']
    end_date = datetime.strptime(end_date_arg,'%Y-%m-%d')
    episodes = con.get_client_episodes_in_range(client_id, token,start_date, end_date)
    return jsonify(episodes)

@app.route('/client/<client_id>/service_language', methods=['POST'])
def edit_client_service_language(client_id):
    service_language = request.args['service_language']
    token = request.args['token']
    message = con.update_service_language(client_id, service_language,token)
    return message

@app.route('/client/<client_id>/add_diet', methods=['POST'])
def edit_client_diet(client_id):
    diet = request.args['diet']
    token = request.args['token']
    message = con.add_diet(client_id, diet,token)
    return message

@app.route('/client/<client_id>/add_advance_directive', methods=['POST'])
def add_client_advance_directive(client_id):
    ad = request.args['advance_directive']
    token = request.args['token']
    message = con.add_advance_directive(client_id, ad, token)
    return message

@app.route('/client/<client_id>/edit_contact_info', methods=['POST'])
def edit_client_contact(client_id):
    category = request.args['category']
    field = ''
    if category == 'email':
        field = 'email'
    elif category == 'phone':
        field = 'number'
    elif category == 'address': 
        field = 'address'
    text = request.args['text']
    token = request.args['token']
    contact_type = request.args['type']
    message = con.edit_client_contact_info(client_id, token, category,field,text,contact_type)
    return message

@app.route('/client/<client_id>/edit_caregivers', methods=['POST'])
def edit_caregivers(client_id):
    token = request.args['token']
    name = request.args['name']
    relationship = request.args['relationship']
    is_primary = __parse_bool(request.args['is_primary'])
    message = con.edit_caregivers(client_id, token, name, relationship, is_primary)
    return message
    
@app.route('/client/<client_id>/edit_caregiver_contacts', methods=['POST'])
def edit_caregiver_contact(client_id):
    category = request.args['category']
    field = ''
    if category == 'email':
        field = 'email'
    elif category == 'phone':
        field = 'number'
    elif category == 'address': 
        field = 'address'
    text = request.args['text']
    token = request.args['token']
    contact_type = request.args['type']
    is_primary = __parse_bool(request.args['is_primary'])
    message = con.edit_caregiver_contacts(client_id, token, category,field,text,contact_type,is_primary)
    return message

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello</h1>"

if __name__ == '__main__':
    app.run()
