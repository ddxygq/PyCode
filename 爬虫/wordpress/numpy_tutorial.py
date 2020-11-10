import requests
import posts
from bs4 import BeautifulSoup
from urllib import parse

domain = 'https://www.numpy.org.cn/'

# 加上请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/86.0.4240.183 Safari/537.36'}


def parse2bs(url_path, verify=True):
    """
    解析html到bs
    :param url_path:
    :param verify: 是否验证
    :return:
    """
    return BeautifulSoup(requests.get(url_path, headers=headers, verify=verify).content, features='html.parser')


def text2h2(s):
    return '<h2>' + s + '</h2>'


def get_content(url):
    if domain not in url:
        return
    print('*************************************************************************************')
    print('%s start ..' % url)
    soup = parse2bs(url, verify=False)
    main = soup.find('main', attrs={'class': 'page'})
    content_soup = main.find('div', attrs={'class': 'theme-default-content content__default'})
    title = content_soup.find_all('h1')[0].text.split('#')[1]
    content = ''.join([str(text2h2(item.text.replace('#', '').strip()) if item.name == 'h2' else item) for item in content_soup.contents[2:]])

    # 保存到wordpress

    # posts.post_new_article(title, content)
    print('%s finish ..' % url)

    # 获取下一页地址
    next_url_span = main.find('span', attrs={'class': 'next'})
    if next_url_span:
        next_url = parse.urljoin(domain, next_url_span.find('a')['href'])
        # 递归爬取
        get_content(next_url)


if __name__ == '__main__':
    get_content(parse.urljoin(domain, 'user/setting-up.html'))
