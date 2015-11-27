__author__ = 'tauren'

from flask import abort
from flask_restful import Resource
from flask.ext.restful import fields, marshal
from flask_login import current_user
from restless_app.model import Task

task_fields = {
        'title': fields.String,
        'user_id': fields.Integer,
        'uri': fields.Url('task')
}

class TaskListApi(Resource):

    def get(self):
        tasks = Task.query.filter_by(user_id=current_user.id).all()
        if not tasks:
            return abort(404)
        return {'results': marshal(tasks, task_fields)}

class TaskApi(Resource):

    def get(self, id):
        task = Task.query.filter_by(id=id, user_id=current_user.id).first()
        if not task:
            return abort(404)
        return {'results': marshal(task, task_fields)}

