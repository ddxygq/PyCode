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
### 继承和多态
面向对象编程中，定义`class`是可以从已经存在的类继承的，暂且称为父类，子类可以拥有父类的所有属性与函数。
我们定一个一个类叫`People`，拥有`work()`函数。
```python
class People(object):
    def work(self):
        print('people work.')
```
下面定义一个`Teacher`类，继承了`People`这个父类，拥有`teach`函数(行为)。
```
class Teacher(People):

    def teach(self):
        print('teacher teach.')
```
实例化一个`Teacher`实例，加了一个函数`teach`函数，`isinstance`可以判断`teacher`是否属于`People`这个类型。
```
if __name__ == '__main__':
    teacher = Teacher()
    teacher.work()
    teacher.teach()
    print(isinstance(teacher, People))
```
结果
```
people work.
teacher teach.
True
```
可以看到，子类`Teacher`继承了父类`People`，也拥有`work`函数，同时也可以添加自己的函数，`isinstance`得出结论：`Teacher`(老师)也是`People`人。
### 多态
如果，子类`Teacher`想修改父类`People`的`work`方法呢，这也是可以的：
```python
class People(object):
    def work(self):
        print('people work.')


class Teacher(People):

    # 子类有work()函数，相当于覆盖了父类的函数，调用子类的work()函数。
    def work(self):
        print('teacher work.')

    def teach(self):
        print('teacher teach.')


if __name__ == '__main__':
    teacher = Teacher()
    teacher.work()
    teacher.teach()
```
结果
```
teacher work.
teacher teach.
```
子类重写父类的`work`函数，调用的就不再是父类的而是自己的`work`函数了，打印的是`teacher work.`，这就是**多态**。多态有什么好处呢？
```
def action(people):
    people.work()


if __name__ == '__main__':
    action(People())
    action(Teacher())
```
`action`传入一个`People`的对象`People()`，就调用`People`类的`work()`函数，传入`Teacher`的对象，它肯定也有`work`方法，因为`Teacher`也是`People`类型，就调用`Teacher`对应的`work`函数。结果：
```
people work.
teacher work.
```
可以发现，`action`函数可以传入`People`对象，也能传入`Teacher`对象，函数不需要做任何修改，这就是多态的好处。

### 多层继承
当然了，类也可以多继承，父亲继承于爷爷，孙子继承于父亲，接着上面，`Teacher`老是还可以有教授这个子分类。
```
class Professor(Teacher):
    def research(self):
        print('叫兽做研究...')
```
类型`Professor`继承于`Teacher`，而`Teacher`继承自`People`。

### 获取对象信息
通过`type`函数，可以获取一个对象的类型信息，
```python
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
```
结果
```
<class '__main__.People'>
<class 'method'>
<class 'builtin_function_or_method'>
```
想判断一个对象是否是函数，可以用`types`模块中定义的常量。

如果想获得对象的所有属性和方法，可以使用`dir`函数。
```
import types
print(types.FunctionType == type(max))
print(types.BuiltinFunctionType == type(max))
print(types.FunctionType == type(f))
```
结果
```
False
True
True
```
