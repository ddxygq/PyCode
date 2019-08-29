class People(object):
    eye = True

    def work(self):
        print('people work.')


def f():
    pass


if __name__ == '__main__':
    people = People()
    print(type(people))
    print(type(people.work))
    print(type(max))

    import types
    print(types.FunctionType == type(max))
    print(types.BuiltinFunctionType == type(max))
    print(types.FunctionType == type(f))

    # 获得对象所有属性和方法
    pros = dir(people)
    print(pros)
    print(people.__class__)

    """
    类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
    在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，
    它自动去调用该对象的__len__()方法
    """

    # 测试对象的属性
    print(hasattr(people, 'eye'))
    setattr(people, 'name', 'ikeguang.com')
    print(getattr(people, 'name'))
    print(hasattr(people, 'work'))
    print(getattr(people, 'work'))