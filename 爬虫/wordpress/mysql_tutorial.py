import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from urllib import parse
import posts
import time
import sys


sys.path.append('../util')
import oss


"""
https://www.ikeguang.com/
"""


domain = 'http://www.manongjc.com/'

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


def get_urls(main_page):
    """
    获取所有要下载页面的url
    :param main_page: 入口
    :return:
    """
    soup = parse2bs(main_page)
    chapters = soup.find('div', attrs={'class': 'course-left'}).find_all('li')[1:]
    links = []
    for chapter in chapters:
        chapter_link = chapter.find_all('a')[0]
        if 'href' in chapter_link.attrs:
            links.append(parse.urljoin(domain, chapter_link['href']))

    return links


def get_content(url, terms_names):
    """
    将详情页保存
    :param url:
    :return:
    """
    if domain not in url:
        return
    print('*************************************************************************************')
    print('%s start ..' % url)
    soup = parse2bs(url, verify=False)
    main = soup.find('div', attrs={'class': 'course-right'})
    course_content = main.find('div', attrs={'class': 'course-content'})

    content_details = []
    for content_detail in course_content.children:
        content_detail_img = content_detail.find('img')

        # 如果是图片，拼接地址，下载后上传到cdn，拼接上传后的地址。
        if isinstance(content_detail_img, Tag):
            image_src = parse.urljoin(domain, content_detail_img['src'])
            # 上传到oss
            image_oss = oss.put_image(image_src)
            content_detail = '<img src="' + image_oss + '">'

        content_details.append(content_detail)

    title = main.find('h1').text
    content = ''.join([str(item).strip() for item in content_details])

    # 保存到wordpress
    posts.post_new_article(title, content, terms_names)
    time.sleep(1)
    print('%s finish ..' % url)


if __name__ == '__main__':
    main_page = 'http://www.manongjc.com/redis/redis_tutorial.html'
    terms_names = {
        # 文章所属标签，没有则自动创建
        'post_tag': ['Redis'],
        # 文章所属分类，没有则自动创建
        'category': ['Redis教程']
    }
    links = get_urls(main_page)

    for link in links:
        get_content(link, terms_names)
