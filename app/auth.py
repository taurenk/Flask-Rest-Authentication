from flask import Blueprint, json, jsonify, request, abort, url_for
from models import User
from flask_login import login_user
from app.models import db
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


@auth_api.route('/user', methods=['POST'])
def new_user():
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        abort(400)

    if User.query.filter_by(username=username).first() is not None:
        abort(400)

    user = User(username=username)
    user.hash_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({'username': user.username}), 201
