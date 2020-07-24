import time
from celery import Celery


'''
第一种方法
app = Celery('tasks',
             broker='redis://:redis@192.168.199.198:6379',
             backend='redis://:redis@192.168.199.198:6379')
'''

# 第二种：通过配置文件
app = Celery('tasks')
app.config_from_object('celeryconfig')


@app.task
def send_mail(email):
    print('send mail to %s' % email)
    time.sleep(5)
    return 'success'

# 启动命令 celery -A tasks worker --loglevel=info  --pool=solo
