import requests
from bs4 import BeautifulSoup
from urllib import parse
import posts
import time
import urllib3

domain = 'https://wizardforcel.gitbooks.io/matplotlib-user-guide/content/'

# 加上请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/86.0.4240.183 Safari/537.36'}

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
    soup = parse2bs(domain)
    chapters = soup.find('nav', attrs={'role': 'navigation'}).find_all('li', attrs={'class': 'chapter'})[1:]
    links = []
    for chapter in chapters:
        hrefs = []
        chapter_links = chapter.find_all('a')
        for chapter_link in chapter_links:
            hrefs.append(parse.urljoin(domain, chapter_link['href']))

        links = links + hrefs

    return links


def get_content(url):
    if domain not in url:
        return
    print('*************************************************************************************')
    print('%s start ..' % url)
    soup = parse2bs(url, verify=False)
    main = soup.find('div', attrs={'class': 'search-noresults'}).find('section', attrs={'class': 'normal markdown-section'})
    title = 'Matplotlib ' + main.find('h1').text
    content = ''.join([str(item).strip() for item in main.contents])

    # 保存到wordpress
    posts.post_new_article(title, content)
    time.sleep(10)
    print('%s finish ..' % url)


if __name__ == '__main__':
    links = get_urls()
    for link in links:
        get_content(link)
