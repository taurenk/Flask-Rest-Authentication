__author__ = 'tauren'

from flask import Flask
from flask_potion import ModelResource, Api
from flask_potion.routes import Relation
from flask_login import LoginManager, login_required, current_user
from flask_principal import Principal, Identity, AnonymousIdentity, identity_loaded, UserNeed

from flask_potion import fields, signals, Api
from flask_potion.contrib.principals import PrincipalResource

def create_app(config_file):

    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    login_manager = LoginManager()
    login_manager.init_app(app)

    from app.models import db, User, Task
    from auth import auth_api
    db.init_app(app)


    """ Principal Permissions """
    """
    principals = Principal(app)

    @principals.identity_loader
    def read_identity_from_flask_login():
        if current_user.is_authenticated:
            return Identity(current_user.id)
        return AnonymousIdentity()


    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        if not isinstance(identity, AnonymousIdentity):
            identity.provides.add(UserNeed(identity.id))

    """

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id).first()

    class TaskResource(ModelResource):
        class Meta:
            model = Task

        class Schema:
            user = fields.ToOne('user')

    class UserResource(ModelResource):
        tasks = Relation('task')

        class Meta:
            model = User

    app.register_blueprint(auth_api, url_prefix='/api/auth')
    api = Api(app, decorators=[login_required])
    api.add_resource(TaskResource)
    api.add_resource(UserResource)

    return app