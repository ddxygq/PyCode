# 面向对象高级

class Teacher(object):

    # 限制该类能动态添加的属性
    __slots__ = ('name', 'age')
    pass


def set_name(self, name):
    self.name = name


def set_age(self, age):
    self.age = age


if __name__ == '__main__':
    teacher = Teacher()

    # 给实例绑定方法
    from types import MethodType
    teacher.set_name = MethodType(set_name, teacher)
    teacher.set_name('keguang')
    print(teacher.name)

    # 给类绑定方法
    Teacher.set_age = set_age

    teacher2 = Teacher()
    teacher2.set_age(24)
    print(teacher2.age)
