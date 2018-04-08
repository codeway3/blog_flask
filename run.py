from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


@login_manager.user_loader
def load_user(user_id):
    return int(user_id)


@app.route('/')
def index():
    return 'Hello world'


if __name__ == '__main__':
    app.run()
