__author__ = 'tauren'

from flask import Flask, url_for, abort
from flask_restful import Resource, Api, reqparse
from flask.ext.restful import fields, marshal
from flask_login import login_required, current_user

def create_app(config_file):

    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    from restless_app.model import db, Task, User
    from restless_app.auth import auth_api, login_manager
    from restless_app.task_api import TaskListApi, TaskApi
    from restless_app.signup_api import SignUpApi

    db.init_app(app)
    login_manager.init_app(app)


    app.register_blueprint(auth_api, url_prefix='/api/auth')

    api = Api(app, decorators=[login_required])
    api.add_resource(TaskListApi, '/tasks', endpoint='tasks')
    api.add_resource(TaskApi, '/tasks/<int:id>', endpoint='task')
    api.add_resource(SignUpApi, '/users', endpoint='user')

    return app