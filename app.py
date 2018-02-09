from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash,g
from flask_sqlalchemy import SQLAlchemy
from models import user
from flask_bootstrap import Bootstrap
import config

app = Flask(__name__)
Bootstrap(app)
app.secret_key = config.SECRETE_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)


# Test DB


@app.route('/db-test')
def testdb():
    try:
        admin = user.Users(username='admin', email='admin@example.com')
        manager = user.Users(username='manager', email='guest@example.com')
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


@app.route('/user')
@login_required
def users():
   users = user.Users.query.filter_by(username='admin')
   return render_template('user.html', users=users)


@app.route("/")
@login_required
def home():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials.'
        else:
            session['logged_in'] = True
            flash('You were just logged in')
            return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out')
    return redirect(url_for('welcome'))


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
