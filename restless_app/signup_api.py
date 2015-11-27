__author__ = 'tauren'

from flask_restful import Resource, reqparse
from restless_app.model import User, db

class SignUpApi(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True,
                                   help='No username provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='No password provided', location='json')
        super(SignUpApi, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        new_user = User(args['username'], args['password'])
        db.session.add(new_user)
        return 201