import requests
from urllib import parse
from bs4 import BeautifulSoup

url = 'http://ljgk.envsc.cn/'

# 加上请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/86.0.4240.75 Safari/537.36'}


def parse2bs(url_path):
    """
    解析html到bs
    :param url_path:
    :return:
    """
    return BeautifulSoup(requests.get(url_path, headers=headers).content, features='html.parser')


def spider():
    soup = parse2bs(url)
    print(soup)


if __name__ == '__main__':
    spider()
