import flask
from flask.json import jsonify
from flask import request
from openapi_server.models import *
from datetime import date


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

@app.route('/hco', methods=['GET'])
def list_HCOs():
    def_HCO = HCO(_DEF_HIC_ID,_DEF_HIC_NAME,_DEF_HIC_CREATION_DATE,_DEF_HIC_DEACTIVATION_DATE,_DEF_HIC_BIN,_DEF_HIC_ORGANIZATION_TYPE)   
    HCO_list = [def_HCO.to_dict()]
    return jsonify(HCO_list)


@app.route('/comments', methods=['POST'])
def post_comment():
    if not request.json:
        abort(400)
    comment = Comment.from_dict(request.json)
    return 'posted comment: "%s" ' % comment.comment_text

@app.route('/comments/<string:subject_healthcare_provider_id>', methods=['GET'])
def get_comment(subject_healthcare_provider_id):
    comments_list = []
    if subject_healthcare_provider_id ==  _subject_healthcare_provider_id:
        comments_list.append(_a_comment.comment_text)
        return jsonify(comments_list)
    else:
        return "no comment found!"



app.run()