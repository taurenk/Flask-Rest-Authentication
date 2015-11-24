from flask import Blueprint, json, jsonify, request, abort
from models import User
from flask_login import login_user

auth_api = Blueprint('auth_api', __name__)


@auth_api.route('/session_login', methods=['POST'])
def session_login():
    data = json.loads(request.data)
    user = User.query.filter_by(email=data.get('email')).first()
    if user.password == data.get('password'):
        login_user(user)
        return jsonify(**{'success': 'Login Successful'})
    else:
        abort(400)