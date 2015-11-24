__author__ = 'tauren'

from flask import Flask
from flask_potion import ModelResource, Api
from flask_potion.routes import Relation
from flask_login import LoginManager, login_required

def create_app(config_file):

    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    login_manager = LoginManager()
    login_manager.init_app(app)

    from app.models import db, User, Task
    from auth import auth_api
    db.init_app(app)
    #db.create_all()


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter_by(id=user_id).first()

    class TaskResource(ModelResource):
        class Meta:
            model = Task

    class UserResource(ModelResource):
        tasks = Relation('task')

        class Meta:
            model = User

    app.register_blueprint(auth_api, url_prefix='/login')
    api = Api(app, decorators=[login_required])
    api.add_resource(TaskResource)
    api.add_resource(UserResource)

    return app