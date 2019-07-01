import flask
from flask.json import jsonify
from flask import request
from openapi_server.models import *
import controller_impl as con 
from datetime import date
from fhir.model import Patient, HumanName, Identifier, CodeableConcept, Coding, uri, Address, ContactPoint, ContactDetail

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
  
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


@app.route('/login', methods=['GET'])
def authenticate():
    username = request.args['username']
    password = request.args['password']
    return jsonify(con.get_authenticated(username, password))

@app.route('/basic_info', methods=['GET'])
def get_client_basic_info():
    client_id = request.args['client_id']
    user_id = request.args['user_id']
    token = request.args['token']
    bi = con.get_client_basic_info(client_id,user_id,token)
    return jsonify(bi)

######
## update data to fhir format
######
@app.route('/basic_info_fhir', methods=['GET']) ##Needs change  to /patient
def get_client_basic_info_fhir():
    client_id = request.args['client_id']
    user_id = request.args['user_id']
    token = request.args['token']
    is_active = __parse_bool(request.args['is_active'])
    bi = con.get_client_basic_info(client_id,user_id,token)
    contact = con.get_client_contact_info_fhir(client_id, is_active, token)

    #fhir operations
    p = Patient(id='patient1')                                  
    identifier = Identifier(
        type=CodeableConcept(coding=[Coding(system="http://hl7.org/fhir/v2/0203", code="MR")]),
        system='urn:oid:1.2.36.146.595.217.0.1',
        value='123456789'
    )
    p.identifier = [identifier]
    p.active = True
    #name information 
    name = HumanName()
    name.use = 'official'
    name.given = [bi['firstname']]
    name.family  =  bi['surname'] 
    p.name = [name]
    
    #gender
    p.gender = bi['gender']

    #address (from contactInfo)
    address = Address()
    address.city = contact[0][0]['city']
    address.use = contact[0][0]['address_type']
    address.city = contact[0][0]['city']
    address.country = contact[0][0]['country']
    address.postalCode = contact[0][0]['postal_code']
    address.line = [contact[0][0]['street_number']+' '+ contact[0][0]['street_name']+' '+ contact[0][0]['street_type']]
    p.address = [address] 

    #telecom (from contactInfo)
    phone = ContactPoint()
    phone.system = 'phone'
    phone.value = contact[1][0]['number']
    phone.use = contact[1][0]['type']
    email = ContactPoint()
    email.system = 'email'
    email.value = contact[2][0]
    p.telecom = [phone, email]

    #contact persons (caregiver)
    
    return p.dumps('json')


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
    start_date = request.args['start_date']
    end_date = request.args['end_date']
    episodes = con.get_client_episodes_in_range(client_id, token,start_date, end_date)
    return jsonify(episodes)



# @app.route('/hco', methods=['GET'])
# def list_HCOs():
#     def_HCO = HCO(_DEF_HIC_ID,_DEF_HIC_NAME,_DEF_HIC_CREATION_DATE,_DEF_HIC_DEACTIVATION_DATE,_DEF_HIC_BIN,_DEF_HIC_ORGANIZATION_TYPE)   
#     HCO_list = [def_HCO.to_dict()]
#     return jsonify(HCO_list)

# @app.route('/comments', methods=['POST'])
# def post_comment():
#     if not request.json:
#         abort(400)
#     comment = Comment.from_dict(request.json)
#     return 'posted comment: "%s" ' % comment.comment_text

# @app.route('/comments/<string:subject_healthcare_provider_id>', methods=['GET'])
# def get_comment(subject_healthcare_provider_id):
#     comments_list = []
#     if subject_healthcare_provider_id ==  _subject_healthcare_provider_id:
#         comments_list.append(_a_comment.comment_text)
#         return jsonify(comments_list)
#     else:
#         return "no comment found!"

# @app.route('/clients', method=['GET'])
# def get_clients():
#     return "blank"



app.run()