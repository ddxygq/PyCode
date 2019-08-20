# 简单装饰器
def di(f):
    """
    程序员开机之前，前台开门之前，都需要先在门外指纹机打卡。
    :param f: 传入一个函数
    :return:
    """
    def wrapper():
        print('%s 打卡,滴...' % f.__name__)
        return f()
    return wrapper


def boot():
    print('开机')


def open():
    print('开门')


# @ 语法糖
@di
def boot2():
    print('开机')


@di
def open2():
    print('开门')


if __name__ == '__main__':

    # 第一种，简单装饰器
    a = di(boot)
    a1 = di(open)
    a()
    a1()

    # 第二种，@ 语法糖
    boot2()
    open2()