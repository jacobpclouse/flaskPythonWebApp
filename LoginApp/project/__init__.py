# Login: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
# Using Web Forms: https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application
''' Forms Google: https://www.google.com/search?q=sending+form+data+with+flask&rlz=1C1GCEU_
enUS990US990&oq=sending+form+data+with+flask&aqs=chrome..69i57.10167j0j1&sourceid=chrome&ie=UTF-8'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app