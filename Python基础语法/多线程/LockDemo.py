import threading
import time


number = 0
lock = threading.Lock()


def plus():
    global number
    for _ in range(1000000):
        number = number + 1
    print('子线程 %s 运算结束后，number = %s' % (threading.current_thread().getName(), number))


def plus2(lk):
    global number
    lk.acquire()
    for _ in range(1000000):
        number = number + 1
    print('子线程 %s 运算结束后，number = %s' % (threading.current_thread().getName(), number))
    lk.release()


if __name__ == '__main__':
    for i in range(2):
        t = threading.Thread(target=plus2, args=(lock, ))
        t.start()
