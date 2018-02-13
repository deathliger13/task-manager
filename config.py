# config.py
# This module contains all the configurations for the start of the app

import os

# this grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRETE_KEY = "_rf!9135)kl=*&3gt5po2c&t8@-%4izu7q+7f1$^85(owav%v%"
    SQLALCHEMY_DATABASE_URI = 'mysql://root:kr34t1v1ty@127.0.0.1/task'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite3')
    WTF_CSRF_ENABLED = False


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:secret@localhost/ziptest_db'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}