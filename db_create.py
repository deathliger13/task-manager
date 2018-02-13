# db_create.py
# This file creates a database used for the task manager

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create():
    db.create_all()
    db.session.commit()
