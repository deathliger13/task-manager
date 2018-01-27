from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import pymysql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kr34t1v1ty'
app.config['MYSQL_DB'] = 'task'

db = SQLAlchemy(app)

# this route will test the database connection and nothing more
@app.route('/db-test')
def testdb():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return '<h1>It works.</h1>'
    except:
        return '<h1>Something is broken.</h1>'

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