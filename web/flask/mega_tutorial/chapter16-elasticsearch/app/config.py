import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'afjah3ur38thgh'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or\
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '2601538122@qq.com'
    MAIL_PASSWORD = '******'
    ADMINS = ['2601538122@qq.com']

    POSTS_PER_PAGE = 5

    LANGUAGES = ['zh']

    # ES url
    ELASTICSEATCH_URL = os.environ.get('ELASTICSEATCH_URL') or 'http://localhost:9200'
