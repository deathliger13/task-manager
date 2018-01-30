# db_create.py
# This file creates a database used for the task manager

from app import db
from models import user

db.create_all()
db.session.commit()