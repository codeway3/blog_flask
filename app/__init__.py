from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
track_modifications = app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

from app import views, models
