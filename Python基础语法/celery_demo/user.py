# 在主程序中调用任务，将任务发送给 Broker， 而不是真正执行该任务，比如下面的主程序是 register
from tasks import send_mail
import time


def register():
    start = time.time()
    print("1. 插入记录到数据库")
    print("2. celery 帮我发邮件")
    result = send_mail.delay("xx@gmail.com")
    print("3. 告诉用户注册成功")
    print("耗时：%s 秒 " % (time.time() - start))

    # 获取结果
    while True:
        if result.get():
            print(result.get())
            break


if __name__ == '__main__':
    register()
