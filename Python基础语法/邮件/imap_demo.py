import imaplib


def run():
    # 账户密码
    email = '******@qq.com'
    password = '123456'
    # 链接邮箱服务器
    conn = imaplib.IMAP4_SSL("imap.qq.com", 993)
    # 登录
    conn.login(email, password)
    # 收邮件
    INBOX = conn.select("INBOX")
    # 全部邮件
    type, data = conn.search(None, 'ALL')
    # 邮件列表
    msgList = data[0].split()
    # 最后一封
    last = msgList[len(msgList) - 1]
    # 取最后一封
    _type, datas = conn.fetch(last, '(RFC822)')
    # 把取回来的邮件写入txt文档
    with open('email.txt', 'w')as f:
        f.write(datas[0][1].decode('utf-8'))


if __name__ == '__main__':
    run()