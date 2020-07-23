from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap



from flask_admin import Admin


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin()




login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):  # factory function
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    admin.init_app(app)

    # admin.add_view(ModelView(User,db.session))

    # Registering the blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint , url_prefix = '/authenticate')

    return app