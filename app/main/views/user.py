from flask import render_template, request, redirect, url_for, session, flash
from app.models import Users
from .. import main
from .index import login_required


@main.route('/user')
@login_required
def users():
   users = Users.query.filter_by(username='admin')
   return render_template('user.html', users=users)