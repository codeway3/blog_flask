import os
from flask import send_from_directory
from flask import render_template, flash, request, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .form import LoginForm
from .models import User


users = [
    {'nickname': 'aaa', 'id': '111111'}
]


@app.before_request
def before_request():
    pass


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@lm.user_loader
def load_user(user_id):
    for user in users:
        if user['nickname'] == user_id:
            return User(nickname=user['nickname'], id=user['id'])


@lm.unauthorized_handler
def handle_needs_login():
    flash("You have to be logged in to access this page.")
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(nickname=form.name.data)
        g.user = user
        login_user(user=user, remember=True)
        flash('Logged in successfully.')
        return redirect('/index')
    else:
        flash('Login failed')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/')
def red():
    return redirect('/index')


@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    if user.is_authenticated:
        return render_template('index.html', title='Home', user=user, posts=posts)
    else:
        return redirect('/login')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
