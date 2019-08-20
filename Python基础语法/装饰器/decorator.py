def di(f):
    print('%s 打卡,滴...' % f.__name__)
    return f()


def boot():
    print('开机')


def open():
    print('开门')


if __name__ == '__main__':
    """
    程序员开机之前，前台开门之前，都需要先在门外指纹机打卡。
    """
    di(boot)
    di(open)
