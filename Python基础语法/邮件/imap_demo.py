import imaplib


def run():
    # 账户密码
    email = '15107281868@163.com'
    password = 'kg123456'
    # 链接邮箱服务器
    conn = imaplib.IMAP4_SSL("imap.163.com", 993)
    # 登录
    conn.login(email, password)
    # 收邮件
    conn.select()
    # 全部邮件
    type, data = conn.search(None, 'ALL')


if __name__ == '__main__':
    run()