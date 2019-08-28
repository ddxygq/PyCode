class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.__score = score

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score


if __name__ == '__main__':
    student = Student('ikeguang', 24, 91)
    print(student.name)
    student.name = 'keguang'
    print(student.name)
    # 读数据
    print(student.get_score())
    # 修改数据
    student.set_score(100)
    print(student.get_score())
