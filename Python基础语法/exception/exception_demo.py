
def div(a, b):
    try:
        a / b
    except ZeroDivisionError:
        print('error : b should not be zero')
    except Exception as e:
        print('unexpect error : {}'.format(e))
    else:
        print('run into else when everything goes well...')
    finally:
        print('always run into finally block.')


def f(a, b):
    a / b


def f2():
    try:
        f(1, 0)
    except Exception as e:
        raise


if __name__ == '__main__':
    # 不能捕获的异常
    # div(2, 'a')
    # 捕获了异常
    # div(2, 0)

    f2()