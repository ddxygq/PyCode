from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
from email import encoders

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def get_server(username):
    servers = {'qq' : 'smtp.qq.com'
               , '126' : 'smtp.126.com'
               , '163' : 'smtp.163.com'
               , '139' : 'smtp.139.com'}
    for key,value in servers.items():
        if key in username:
            return value


def send_mail_multipart(username, password, to, sender_name, subject, content, email_type):
    from_addr = username
    password = password
    to_addr = to
    smtp_server = get_server(username)

    msg = MIMEMultipart()
    # 邮件正文是MIMEText类型
    msg.attach(MIMEText('%s'%(content), '%s'%(email_type), 'utf-8'))
    msg['From'] = _format_addr('%s<%s>' % (sender_name, from_addr))
    msg['To'] = _format_addr('<%s>' % to_addr)
    msg['Subject'] = Header('%s'%(subject), 'utf-8').encode()

    # 读取附件
    filename = 'D:/我的文件/Codes/PyCode/source/image/0.jpg'
    with open(filename, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'jpg', filename='0.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='0.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    # 普通登陆端口是25，带ssl验证时候端口是465
    # smtplib.SMTP_SSL(smtp_server, 465)
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


if __name__ == '__main__':
    """发送带附件的邮件"""
    username = '******@126.com'
    password = '******'
    sender_name = 'ikeguang'
    subject = 'test 附件'
    content = '<html><h1>ikeguang 的来信</h1></html> <a href="http://www.ikeguang.com">ikeguang.com</a>'
    # email_type 取值：plain,文本类型邮件;html,html类型邮件
    email_type = 'html'
    _to = ['******@qq.com', '******@163.com']
    for to in _to:
        send_mail_multipart(username, password, to, sender_name, subject, content, email_type)
        print('send mail to %s success' % (to))