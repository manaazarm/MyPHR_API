import flask
from flask.json import jsonify
from flask import request
from openapi_server.models import *
import controller_impl as con 
from datetime import date
from datetime import datetime


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
    try:
        client_id = request.args.get('client_id')
        hcn = request.args.get('hcn')
        token = request.args.get('token')
        if client_id == None:
            client_id = con.get_client_id_from_hcn (hcn)
        episodes = con.get_client_episodes(client_id, token)
        return jsonify(episodes)
    except Exception as e:
        print(e)

@app.route('/episodes_by_range', methods=['GET'])
def get_client_episodes_by_range():
    client_id = request.args['client_id']
    token = request.args['token']
    
    hcn = request.args['hcn']
    if client_id == None:
        client_id = con.get_client_id_from_hcn (hcn)
    
    start_date_arg = request.args['start_date']
    start_date = datetime.strptime(start_date_arg,'%Y-%m-%d')
    end_date_arg = request.args['end_date']
    end_date = datetime.strptime(end_date_arg,'%Y-%m-%d')
    episodes = con.get_client_episodes_in_range(client_id, token,start_date, end_date)
    return jsonify(episodes)

@app.route('/episodes', methods=['POST'])
def send_client_episodes():
    hcn = request.args.get('hcn')
    token = request.args.get('token')
    client_id = con.get_client_id_from_hcn (hcn)
    episodes = con.save_client_episodes(client_id, token)
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