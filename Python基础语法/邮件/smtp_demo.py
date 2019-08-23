from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def get_server(username):
    servers = {'qq' : 'smtp.qq.com'
               , '126' : 'smtp.126.com'
               , '163' : 'smtp.163.com'}
    for key,value in servers.items():
        if key in username:
            return value


def send_mail(username, password, to):
    from_addr = username
    password = password
    to_addr = to
    smtp_server = get_server(username)

    msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
    msg['From'] = _format_addr('ikeguang <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


if __name__ == '__main__':
    """发送邮件"""
    username = 'username@qq.com'
    password = 'username'
    _to = ['username@qq.com', 'username@163.com', 'username@126.com']
    for to in _to:
        send_mail(username, password, to)
        print('send mail to %s success'%(to))