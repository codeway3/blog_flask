from flask import Flask
from flask_login import LoginManager, AnonymousUserMixin
from flask_sqlalchemy import SQLAlchemy


class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'


app = Flask(__name__)
app.config.from_object('config')
track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'users.login'
lm.anonymous_user = Anonymous


from app import views, models
