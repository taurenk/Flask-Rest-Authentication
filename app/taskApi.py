__author__ = 'tauren'

from flask import Flask, abort, jsonify
from flask.ext.restful import Api, Resource
from flask.ext.restful import reqparse
from flask.ext.restful import fields, marshal
from auth import auth, get_user_id

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}

tasks = [
    {
        'id': 1,
        'user_id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'user_id': 1,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    },
    {
        'id': 3,
        'user_id': 2,
        'title': u'Learn To Play Fetch, The Hard Way!',
        'description': u'Henry dog doesnt know how to play fetch!',
        'done': False
    }
]


class TaskListAPI(Resource):

    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
            help='No task title provided', location='json')
        self.reqparse.add_argument('description', type=str, default="", location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        print 'Fetching Data for user: %s' % auth.username()
        return {'tasks': [marshal(task, task_fields) for task in tasks if task['user_id'] == get_user_id(auth.username())]}

    def post(self):
        pass

class TaskAPI(Resource):

    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

    def get(self, id):
        print 'Fetching Data for user: %s' % auth.username()
        task = [task for task in tasks if task['id'] == id and task['user_id'] == get_user_id(auth.username())]
        if len(task) == 0:
            abort(404)
        return {'task': marshal(task[0], task_fields)}

    def put(self, id):
        task = filter(lambda t: t['id'] == id, tasks)
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                task[k] = v
        return { 'task': marshal(task, task_fields) }

    def delete(self, id):
        pass
