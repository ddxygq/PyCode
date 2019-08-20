import functools

# 业务逻辑函数需要参数
def di(f):
    """
    程序员开机之前，前台开门之前，都需要先在门外指纹机打卡。
    :param f: 传入一个函数
    :return:
    """
    # 把原始函数的__name__等属性复制到wrapper()
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print('%s 打卡,滴...' % f.__name__)
        return f(*args, **kwargs)
    return wrapper


@di
def boot(name):
    print('%s 开机' % name)


if __name__ == '__main__':
    boot('keguang')