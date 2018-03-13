from flask import render_template, request, redirect, url_for, session, flash

from .. import main

from app import db
from manage import app
from functools import wraps
from app.models import Users



@main.route("/")
def index():
    return render_template('index.html')


@main.route('/db-test')
def testdb():
    try:
        admin = Users(username='admin', email='admin@example.com', password='123456')
        manager = Users(username='manager', email='guest@example.com', password='123456')
        db.session.add(admin)
        db.session.add(manager)
        db.session.commit()
        return '<h1>User were sucessfully created</h1>'
    except:
        return '<h1>Nothing happend</h1>'


# login required decorator


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@main.route('/welcome')
def welcome():
    return render_template('welcome.html')
