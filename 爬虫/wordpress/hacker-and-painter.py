import requests
from bs4 import BeautifulSoup
from urllib import parse
import posts
import time
import urllib3

domain = 'https://www.kancloud.cn/imxieke/hacker-and-painter/'

# 加上请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/86.0.4240.183 Safari/537.36'}

terms_names = {
    'category': ['书籍'],
    'post_tag': ['书籍']
}

urllib3.disable_warnings()


def parse2bs(url_path, verify=True):
    """
    解析html到bs
    :param url_path:
    :param verify: 是否验证
    :return:
    """
    return BeautifulSoup(requests.get(url_path, headers=headers, verify=verify).content, features='html.parser')


def get_urls():
    soup = parse2bs(parse.urljoin(domain, '107318'))
    lis = soup.find('div', attrs={'class': 'catalog'}).find_all('li')
    links = []
    for li in lis:
        title = li.find('a').text
        link = parse.urljoin(domain, li.find('a')['href'])
        links.append((title, link))

    return links


def get_content(link):
    title = '黑客与画家 ' + link[0]
    url = link[1]
    print('*************************************************************************************')
    print('%s start ..' % url)
    soup = parse2bs(url, verify=False)
    main = soup.find('div', attrs={'class': 'content'})
    content = ''.join([str(item).strip() for item in main.contents]) + '\n\n原文链接: ' + url

    # 保存到wordpress
    posts.post_new_article(title, content, terms_names)
    time.sleep(1)
    print('%s finish ..' % url)


if __name__ == '__main__':
    links = get_urls()
    for link in links:
         get_content(link)
