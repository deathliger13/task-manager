# project/server/config.py

import os

# this grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))
APP_SETTINGS="project.server.config.DevelopmentConfig"
FLASK_DEBUG=1


class BaseConfig(object):
    """Base configuration."""
    BCRYPT_LOG_ROUNDS = 4
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='my_precious')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    WTF_CSRF_ENABLED = False
    SECRETE_KEY = "_rf!9135)kl=*&3gt5po2c&t8@-%4izu7q+7f1$^85(owav%v%"
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:kr34t1v1ty@127.0.0.1/task'


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(basedir, 'dev.db'))


class TestingConfig(BaseConfig):
    """Testing configuration."""
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite3')
    TESTING = True
    WTF_CSRF_ENABLED = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://localhost/exampleDb'
    WTF_CSRF_ENABLED = True
