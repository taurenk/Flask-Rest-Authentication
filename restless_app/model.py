__author__ = 'tauren'

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from passlib.apps import custom_app_context as pwd_context
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer

login_serializer = URLSafeTimedSerializer('SECRET KEY')
db = SQLAlchemy()


class User(db.Model, UserMixin):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password_hash = db.Column(db.String(), nullable=False)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def get_auth_token(self):
        data = [str(self.id), self.password_hash]
        return login_serializer.dumps(data)


class Task(db.Model):

    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    title = db.Column(db.String(), nullable=False)

    # Link user_id back to user table
    user = db.relationship(User, backref=backref('tasks', lazy='dynamic'))

