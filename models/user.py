from app import db
from sqlalchemy_utils import PasswordType, force_auto_coercion


# User table


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt'], )
        , nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
