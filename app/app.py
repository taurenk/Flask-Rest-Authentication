__author__ = 'tauren'

from flask import Flask
from flask.ext.restful import Api
from taskApi import TaskListAPI, TaskAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')

if __name__ == '__main__':
    app.run(debug=True)