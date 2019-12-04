import threading
import time
import threading


class MyThread(threading.Thread):
    """
    继承threading.Thread类，重写run()方法
    """
    def __init__(self, thread_name):
        super(MyThread, self).__init__(name=thread_name)

    def run(self):
        print('%s 正在运行中.' % self.name)


def show(arg):
    time.sleep(1)
    print('thread ' + str(arg) + 'running...')


if __name__ == '__main__':

    # 实现线程两种方法:1)、继承threading.Thread()类，2)、实例化threading.Thread对象的时候，将要执行的方法传入线程.
    for i in range(10):
        MyThread('thread-' + str(i)).start()

    for i in range(10):
        threading.Thread(target=show, args=(i, )).start()
