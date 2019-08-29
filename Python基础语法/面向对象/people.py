class People(object):
    def work(self):
        print('people work.')


class Teacher(People):

    # 子类有work()函数，相当于覆盖了父类的函数，调用子类的work()函数。
    def work(self):
        print('teacher work.')

    def teach(self):
        print('teacher teach.')


class Professor(Teacher):
    def research(self):
        print('叫兽做研究...')


def action(people):
    people.work()


if __name__ == '__main__':
    teacher = Teacher()
    teacher.work()
    teacher.teach()
    # 判断teacher是否是People类型
    print(isinstance(teacher, People))
    people = People()
    people.work()

    action(People())
    action(Teacher())
