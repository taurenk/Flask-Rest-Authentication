__author__ = 'tauren'

from flask.ext.sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import backref
from passlib.apps import  custom_app_context as pwd_context

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    # email = db.Column(db.String(), nullable=False)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    title = db.Column(db.String(), nullable=False)
    # Relationship Link
    user = db.relationship(User, backref=backref('tasks', lazy='dynamic'))
