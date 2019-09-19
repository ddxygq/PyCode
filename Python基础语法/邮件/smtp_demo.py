from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def get_server(username):
    """
    通过邮箱地址获得邮箱服务器
    :param username:用户名，比如：123456@qq.com
    :return: 邮箱服务器地址，比如：smtp.qq.com
    """
    servers = {'qq' : 'smtp.qq.com'
               , '126' : 'smtp.126.com'
               , '163' : 'smtp.163.com'
               , '139' : 'smtp.139.com'}

    for key,value in servers.items():
        if key in username:
            return value


def send_mail(username, password, to, sender_name, subject, content, email_type):
    from_addr = username
    password = password
    to_addr = to
    smtp_server = get_server(username)

    # 邮件正文是MIMEText类型
    msg = MIMEText('%s'%(content), '%s'%(email_type), 'utf-8')
    msg['From'] = _format_addr('%s<%s>' % (sender_name, from_addr))
    msg['To'] = _format_addr('<%s>' % to_addr)
    msg['Subject'] = Header('%s'%(subject), 'utf-8').encode()

    # 普通登陆端口是25，带ssl验证时候端口是465
    # smtp_server = 'smtp.exmail.qq.com'
    # server = smtplib.SMTP_SSL(smtp_server, 465)
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


if __name__ == '__main__':
    """发送简单文本邮件"""
    username = '******@126.com'
    password = '******'
    sender_name = '******@126.com'
    subject = 'test 邮件'
    content = '<html><h1>ikeguang 的来信</h1></html> <a href="http://www.ikeguang.com">ikeguang.com</a></html>'
    # email_type 取值：plain,文本类型邮件;html,html类型邮件
    email_type = 'html'
    _to = ['******@126.com', '******@qq.com']
    for to in _to:
        send_mail(username, password, to, sender_name, subject, content, email_type)
        print('send mail to %s success' % to)
