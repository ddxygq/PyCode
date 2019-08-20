import functools

# 类装饰器
class di(object):
    def __init__(self, f):
        self._f = f

    def __call__(self, *args, **kwargs):
        print('decorator start...')
        self._f()
        print('decorator end...')


@di
def boot():
    print('开机')


if __name__ == '__main__':
    boot()