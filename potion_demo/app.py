from flask import Flask, abort, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_potion.routes import Relation, Route, FieldSet
from flask_potion import ModelResource, fields, Api, Resource

from flask_login import LoginManager, login_user, UserMixin, login_required, logout_user


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://taurenk:Wrangler631@demodb.csxsl6g3bmig.us-east-1.rds.amazonaws.com/demodb"
db = SQLAlchemy(app)

""" Authentication """
login_manager = LoginManager()
login_manager.init_app(app)
app.config["SECRET_KEY"] = "NEWSECRET"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    user = User.query.filter_by(email=data.get('email')).first()
    if user.password == data.get('password'):
        login_user(user)
        return jsonify(**{'success': 'Login Successful'})
    else:
        abort(400)

""" Models """
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    title = db.Column(db.String(), nullable=False)
    user = db.relationship(User, backref=backref('tasks', lazy='dynamic'))

db.create_all()

""" Resources """
class TaskResource(ModelResource):
    class Meta:
        model = Task


class UserResource(ModelResource):
    tasks = Relation('task')

    class Meta:
        model = User
api = Api(app, decorators=[login_required])
api.add_resource(TaskResource)
api.add_resource(UserResource)

if __name__ == '__main__':
    app.run(debug=True)
