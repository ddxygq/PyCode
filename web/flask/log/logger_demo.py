from flask import Flask,redirect,url_for
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
from logging.handlers import SMTPHandler

app = Flask(__name__)

ADMINS = ['2864791604@qq.com']


"""
这种设置，INFO以上级别的日志都会保存到文件，ERROR级别的日志会通过邮件发送。
"""
if not app.debug:
    # 这个如果不设置，日志中就没有INFO级别的日志
    app.logger.setLevel(logging.INFO)

    # 设置日志格式
    formatter = Formatter('%(asctime)s %(levelname)s: %(module)s.%(funcName)s() %(message)s '
                          '[in %(pathname)s:%(lineno)d]')

    # INFO级别日志
    handler = RotatingFileHandler('flask.log', maxBytes=1024 * 1024 * 100, backupCount=10)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # 设置邮件日志
    mail_handler = SMTPHandler('smtp.126.com'
                               , 'ikeguang@126.com'
                               , ADMINS
                               , 'YourApplication Failed'
                               ,('ikeguang@126.com', 'Kg123456'))
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(formatter)
    app.logger.addHandler(mail_handler)


@app.route('/')
@app.route('/index')
def index():
    app.logger.info('index .')
    return 'logger_demo'


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('page_not_found...')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()

