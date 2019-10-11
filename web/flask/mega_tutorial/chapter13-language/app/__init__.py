from flask import Flask, request
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login.login_manager import LoginManager
from app.log import logging_module
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l

app = Flask(__name__)
app.config.from_object(Config)
# app.secret_key = 'afjah3ur38thgh'

login = LoginManager(app)
login.login_view = 'login'
login.login_message = _l('Please log in to access this page.')

# 日志
app.logger = logging_module.getLogger('log/log.log', 'mylog')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 邮件
mail = Mail(app)

# css框架Bootstrap
bootstrap = Bootstrap(app)

# 日期和时间处理
moment = Moment(app)

# 语言翻译
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
