import os
import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
from logging.handlers import SMTPHandler


def getLogger(logfile, logname=None):
	"""
	return a logger which special log file path and log name.
	"""

	if '/' in logfile:
		logdir = logfile[:(len(logfile) - logfile[::-1].find('/') - 1)]
		if not os.path.exists(logdir):
			os.makedirs(logdir)

	logger = logging.getLogger(logname)
	# 这个如果不设置，日志中就没有INFO级别的日志
	logger.setLevel(logging.INFO)

	# 设置日志格式
	formatter = Formatter('%(asctime)s %(levelname)s: %(module)s.%(funcName)s() %(message)s \
		[in %(pathname)s:%(lineno)d]')

	# INFO级别日志文件，按照100M滚动
	handler = RotatingFileHandler(logfile, maxBytes=1024 * 1024 * 100, backupCount=10)
	handler.setLevel(logging.INFO)
	handler.setFormatter(formatter)
	logger.addHandler(handler)

	# 邮件日志
	receivers = ['ikeguang@126.com'
		]
	subject = 'application error.'
	mail_handler = SMTPHandler(get_server('******@163.com')
							, '******@163.com'
							, receivers
							, subject
							, ('******@163.com', '******')
							)
	mail_handler.setLevel(logging.ERROR)
	mail_handler.setFormatter(formatter)
	logger.addHandler(mail_handler)

	return logger


def get_server(username):
	"""
	通过邮箱地址获得邮箱服务器
	:param username:用户名，比如：123456@qq.com
	:return: 邮箱服务器地址，比如：smtp.qq.com
	:param username:
	:return:
	"""
	servers = {'qq': 'smtp.qq.com'
		, '126': 'smtp.126.com'
		, '163': 'smtp.163.com'
		, '139': 'smtp.139.com'
		}

	for key,value in servers.items():
		if key in username:
			return value
