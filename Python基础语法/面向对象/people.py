class People(object):
    def work(self):
        print('work.')


class Teacher(People):
    def teach(self):
        print('teach.')


if __name__ == '__main__':
    teacher = Teacher()
    teacher.work()
    teacher.teach()
    # 判断teacher是否是People类型
    print(isinstance(teacher, People))
