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

# app.secret_key = 'afjah3ur38thgh'

login = LoginManager()
login.login_view = 'login'
login.login_message = _l('Please log in to access this page.')


db = SQLAlchemy()
migrate = Migrate()
# 邮件
mail = Mail()
# css框架Bootstrap
bootstrap = Bootstrap()
# 日期和时间处理
moment = Moment()
# 语言翻译
babel = Babel()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app)
    login.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    babel.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # 日志
    app.logger = logging_module.getLogger('log/log.log', 'mylog')

    return app


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
