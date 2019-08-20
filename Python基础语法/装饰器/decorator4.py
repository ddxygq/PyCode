# 带参数的装饰器
def di_args(time):

    def di(f):
        """
        程序员开机之前，前台开门之前，都需要先在门外指纹机打卡。
        :param f: 传入一个函数
        :return:
        """
        def wrapper(*args, **kwargs):
            if time < '9:00':
                print('来的真早，很棒。。。')

            print('%s 打卡,滴...' % f.__name__)
            return f(*args, **kwargs)
        return wrapper
    return di


@di_args('8:00')
def boot(name):
    print('%s 开机' % name)


if __name__ == '__main__':
    boot('keguang')