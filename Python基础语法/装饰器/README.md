# Python装饰器

在Python里面，函数可以作为参数传入一个函数，函数也可以复制给变量，通过变量调用函数。装饰器可以扩展一个函数的功能，为函数做一个装饰器注解，可以把装饰器里面定义的功能于所有函数提前执行，提升代码的复用程度。

现在有这么个场景。
## 打卡
互联网公司里面有各种员工，程序员，前台...，程序员在打开电脑前，需要打卡，前台要早点来开门（我也不清楚，谁开门，这里假定，前台开门），前台开门前也需要打卡。也就是说，打卡是所有员工的最先的公共动作，那么可以把打卡这个功能抽出来作为公共逻辑。

## 普通函数调用方法
自然想到，可以实现如下。
```python
def di(f):
    print('%s 打卡,滴...' % f.__name__)
    return f()


def boot():
    print('开机')


def open():
    print('开门')


if __name__ == '__main__':
    """
    程序员开机之前，前台开门之前，都需要先在门外指纹机打卡。
    """
    di(boot)
    di(open)

```
定义了一个函数`di(f)`，可以打印`f.__name__`即`f`的函数名信息，同时返回f()的执行结果。

注意：`__name__`如果作为模块导入，`module.__name__`就是模块自己的名字，如果模块自己作为脚本执行，返回`__main__`。

执行结果：
```
boot 打卡,滴...
开机
open 打卡,滴...
开门
```
这样设计，如果有很多函数都要调用，就很麻烦，那么装饰器就排上了用场。

## 简单装饰器 与 @语法糖
**装饰器**：在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
### 简单装饰器
定义一个`di(f)`方法，还是把要执行的逻辑的函数作为参数传入，里面定义一个`wrapper`函数，返回值是`f`的执行结果。
在`if __name__ == '__main__':`里面，调用了这个装饰器，不修改定义好了的函数，在运行期间动态添加功能"打卡"。
```python
import functools

# 简单装饰器
def di(f):
    """
    程序员开机之前，前台开门之前，都需要先在门外指纹机打卡。
    :param f: 传入一个函数
    :return:
    """
    # 把原始函数的__name__等属性复制到wrapper()
    @functools.wraps(f)
    def wrapper():
        print('%s 打卡,滴...' % f.__name__)
        return f()
    return wrapper


def boot():
    print('开机')


def open():
    print('开门')


if __name__ == '__main__':

    # 第一种，简单装饰器
    a = di(boot)
    a1 = di(open)
    print(a.__name__) # 结果wrapper 加@functools.wraps(f)后结果为 boot
    a()
    a1()
```

`di(boot)`的返回值a就是`wrapper`函数，通过`a()`就调用了`wrapper`函数，得到`boot`的返回值。同理，`di(open)`一样。

**结果**
```
boot
boot 打卡,滴...
开机
open 打卡,滴...
开门
```
由于`di(boot)`的返回值`a`就是`wrapper`函数，那么`print(a.__name__)`的结果就理所当然是是`wrapper`，我们希望是`boot`，怎么办，`@functools.wraps(f)`这个注解可以把原始函数`boot`的`__name__`等属性复制到`wrapper()`，把这行代码注释也能运行，那么`print(a.__name__)`的结果就是`wrapper`。

### 第二种，@ 语法糖
通过`@`语法糖，也能将装饰器应用于函数上面，推荐。
```python
import functools

def di(f):
    """
    程序员开机之前，前台开门之前，都需要先在门外指纹机打卡。
    :param f: 传入一个函数
    :return:
    """
    # 把原始函数的__name__等属性复制到wrapper()
    @functools.wraps(f)
    def wrapper():
        print('%s 打卡,滴...' % f.__name__)
        return f()
    return wrapper


# @ 语法糖
@di
def boot2():
    print('开机')


@di
def open2():
    print('开门')
    
    
if __name__ == '__main__':

    # 第二种，@ 语法糖
    boot2()
    open2()
```
`@di`标记相当于，`a2 = di(boot2)  a2()`。不用这么麻烦，因为加了`@`符号标记，直接用`boot2()`调用装饰器即可。

**结果**
```
boot2 打卡,滴...
开机
open2 打卡,滴...
开门
```

## 业务逻辑函数需要参数
业务逻辑函数可能需要参数，比如：
```python
def boot(name):
    print('%s 开机' % name)
```
那么，只需要将前面的装饰器修改为：
```python
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
```

结果：
```
boot 打卡,滴...
keguang 开机
```

给`wrapper`也加上`*args, **kwargs`参数，在`boot`里面直接调用`f(*args, **kwargs)`即可。顺便提一下：
- *args：可以传入一个数组参数
- **kwargs：可以传入一个`k-v`对参数

先后顺序对应，数组参数在前。举例：
```python
def f(*args, **kwargs):
    print('args=', args)
    print('kwargs=', kwargs)

print(f(1, 2, 3, a = 'a', b = 'b'))

# 结果
# args= (1, 2, 3)
# kwargs= {'a': 'a', 'b': 'b'}
```

## 带参数的装饰器
如果装饰器也带参数，比如现在如果某个员工早晨上班来得早`< 9:00`，咱可以做个表扬，那么相当于只需要在前面的`di()`外面套一层函数,`di_args`即可，在`wrapper`里面。使用这个参数
```python
import functools

# 带参数的装饰器
def di_args(time):
    def di(f):
        """
        程序员开机之前，前台开门之前，都需要先在门外指纹机打卡。
        :param f: 传入一个函数
        :return:
        """
        # 把原始函数的__name__等属性复制到wrapper()
        @functools.wraps(f)
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
```
参数在`@di_args('8:00')`传入即可，有点像`java`里面的注解。最后还是通过`boot('keguang')`调用即可，结果：
```
来的真早，很棒。。。
boot 打卡,滴...
keguang 开机
```
## 类装饰器
类装饰器主要依靠类的`__call__`方法，当使用 `@` 形式将装饰器附加到函数上时，就会调用此方法。
```python
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
```
加上`@di`装饰器标识，会用`boot`去实例化`di`类，然后执行`__call__`函数，`object`表示这个类可以传入任何类型参数。
运行结果
```
decorator start...
开机
decorator end...
```
装饰器有一个典型的应用场景就是打`log`日志，如果所有逻辑都需要日志记录程序的运行状况，那么可以对这些逻辑(函数)加日志模块装饰器，就能达到相应目的。

![](https://github.com/ddxygq/PyCode/raw/master/source/image/0.jpg)