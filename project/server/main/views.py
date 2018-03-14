# project/server/main/views.py
from flask import render_template, Blueprint
import requests



main_blueprint = Blueprint('main', __name__,)


@main_blueprint.route('/')
def home():
    return render_template('main/home.html')


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")

@main_blueprint.route('/api', methods=['GET'])
def api():
    r = requests.get('https://api.github.com/user', auth=('deathliger666', 'oleg13081995'))
    return 'Код невозврата = ' + str(r.status_code)
