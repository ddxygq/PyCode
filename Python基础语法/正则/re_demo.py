import re


def match_demo():
    p = re.compile('[a-z]+')

    print(p.pattern)
    result = p.match("abc123abc")
    print(result)
    print(result.span())
    print(result.string)
    print(result.group())


def search_demo():
    p = re.compile('[a-z]+')
    result = p.match("abc123def")
    print(result)
    print(result.group())


def findall_demo():
    p = re.compile('[a-z]+')
    result = p.findall("abc123abc")
    print(result)


if __name__ == '__main__':
    # match_demo()
    # search_demo()
    findall_demo()
