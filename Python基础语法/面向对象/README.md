# 面向对象
面向对象编程是一种程序设计思想，对象包含数据和操作的函数。

## 类
类作为一个模板，可以实例化出实际对象，包含属性和函数。
### 定义一个类
```python
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
```
这就定义了一个类，`class`关键字声明这是一个类，后接`Student`是类的名字，括号里面的`object`表示这个类的继承类(好比父母亲)，如果没有类继承，通常所有类都继承自`object`类，`__init__`这个函数在实例化一个对象的时候使用，包含成员变量`name`和`age`，`self`表示当前对象，由`Python`解释器传入，只需要传入`name`和`age`即可。`self.name = name`表示根据传入的变量给当前实例的数据赋值。
### 创建实例对象
实例是一个类的实际对象，对于人这个大的类别，张三，李四，都是一个个实例对象，他们必须有自己的名字和年龄。
```
student = Student('ikeguang', 24, 91)
print(student.name)
```
结果是这样
```
ikeguang
```
### 私有变量
上面的`self.name`在类的外面是可以直接访问的，有时候我们可能希望有些变量是在类的外部无法访问的，以双下划线`__`开头的变量是私有变量，在类的外面无法访问，只能在类的内部访问。
```python
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.__score = score


if __name__ == '__main__':
    student = Student('ikeguang', 24, 91)
    print(student.__score)
```
这里定义了一个私有变量`__score`，在类的外部访问会报错：
```
Traceback (most recent call last):
  File "F:/我的文件/code/PyCode/Python基础语法/面向对象/Student.py", line 16, in <module>
    print(student.__score)
AttributeError: 'Student' object has no attribute '__score'
```
那么，需要怎么获取(读)，修改(写)呢，既然私有变量`__score`只能在类的内部访问，那么可以在类的内部提供`get`(读)和`set`(写)的`public`方法：
```python
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
```
这里使用内部的`get_score()`公共方法提供读取数据的功能，使用`set_score()`公共方法提供修改数据的功能。
**注意**:类似于`__name__`这种双下划线开头结尾的变量是`Python`内部定义的特殊变量，可以直接访问，定义变量时，不允许使用双下划线开头结尾的变量。
