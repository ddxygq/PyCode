# user defined exception


class MyError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


if __name__ == '__main__':
    try:
        raise MyError("自定义异常.")
    except MyError as e:
        print(e)