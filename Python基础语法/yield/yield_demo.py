def foo():
    print('starting...')
    while True:
        res = yield 4
        print('res -> ', res)


def foo2(num):
    print('starting...')
    while num < 10:
        num = num + 1
        yield num


if __name__ == '__main__':
    # g = foo()
    # print(next(g))
    # print('*' * 20)
    # print(g.send(7))
    for n in foo2(0):
        print(n)
