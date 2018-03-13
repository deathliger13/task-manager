from flask import render_template, request, redirect, url_for, session, flash
from app.models import Users
from .. import main
from .index import login_required


@main.route('/user')
@login_required
def users():
   users = Users.query.filter_by(username='admin')
   return render_template('user.html', users=users)


@main.route('/create', methods=['GET', 'POST'])
def register():
    form = CreateUser(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)