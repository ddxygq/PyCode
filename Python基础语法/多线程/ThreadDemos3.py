import threading
import time
import ctypes


"""
知识点三：
此时join的作用就凸显出来了，join所完成的工作就是线程同步，即主线程任务结束之后，进入阻塞状态，一直等待其他的子线程执行结束之后，主线程在终止，
"""


def run():
    print('当前线程的名字是： ', threading.current_thread().name, '开始执行', time.strftime(format))
    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name, '执行结束', time.strftime(format))


if __name__ == '__main__':

    start_time = time.time()
    format = '%Y-%m-%d %H:%M:%S'

    print('这是主线程：', threading.current_thread().name)
    thread_list = []
    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        task_start_time = time.time()
        print(t.name, ' start -> ', time.strftime(format))
        # 是否设置为守护线程，结果一样
        t.setDaemon(True)
        t.start()
        t.join(2)

        if time.time()-task_start_time >= 2:
            print('%s 超时... %d' % (t.name, time.time()-task_start_time))
        print(t.name, ' end -> ', time.strftime(format))

    # for t in thread_list:
    #     t.join(1.5)

    print('主线程结束了！' , threading.current_thread().name)
    print('一共用时：', time.time()-start_time)
