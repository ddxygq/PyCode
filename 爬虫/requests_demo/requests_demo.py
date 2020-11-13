import requests
from urllib import parse
from bs4 import BeautifulSoup

url = 'https://www.zhaogaoxiao.com/'

# 加上请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/86.0.4240.75 Safari/537.36'}


def parse_local_u(friend_link):
    """
    各地大学名录
    :param friend_link:
    :return:
    """
    menu = friend_link.find('p', attrs={'class': 'title9'}).text
    links = friend_link.find_all('a')
    print(menu, links)

    # (title, href)
    infos = []
    for link in links:
        attres = link.attrs
        if attres.keys().__contains__('title'):
            infos.append((link['title'], link['href']))
    for info in infos:
        title = info[0]
        info_url = info[1]

        # 保存一个地区的所有数据
        u_infos = []
        u_infos.append('## {}'.format(title))
        u_infos.append('|校徽|学校名称|院校省份|院校性质|院校类型|学历层次|院校属性|')
        u_infos.append('|------------| ------------ |------------|------------| ------------ |------------|------------|')

        while '/' in info_url:
            info_url_abs = parse.urljoin(url, info_url)
            info_soup = parse2bs(info_url_abs)
            u_table = info_soup.find_all('table', attrs={'id': 'table'})
            u_trs = u_table[0].find_all('tr')

            # 保存一个地区的一页数据
            # u_infos = []

            # 表格内容
            for u_tr in u_trs[1:]:
                u_tds = u_tr.find_all('td')
                ulogo = parse.urljoin(url, u_tds[0].find('img')['src'])

                # u_info保存每个学校的信息[logo，名称, 院校省份	院校性质	院校类型	学历层次	院校属性]
                u_info = ['', ulogo]
                for u_td in u_tds[1:-2]:
                    u_info.append(u_td.text.strip().replace('\n', ','))

                # 学校简介
                u_desc_link = parse.urljoin(url, u_tds[-2].find('a')['href'])
                u_desc_bs = parse2bs(u_desc_link)
                u_desc = u_desc_bs.find('div', attrs={'class': 'box-con'})
                # u_desc_p = u_desc.find_all('p')
                # u_info.append(u_desc_p)
                u_infos.append('|'.join(u_info))

            # 获取下一页地址
            nextPage = info_soup.find('ul', attrs={'id': 'pageUl'}).find_all('a')[-1]
            info_url = nextPage['href']

        print('\n'.join(u_infos))


def parse2bs(url_path):
    """
    解析html到bs
    :param url_path:
    :return:
    """
    return BeautifulSoup(requests.get(url_path, headers=headers).content, features='html.parser')


def subject_extract(friend_link):
    print('=================================================')
    menu = friend_link.find('p', attrs={'class': 'title9'}).text
    links = friend_link.find_all('a')
    print(menu, links)

    # (title, href)
    infos = []
    for link in links:
        attres = link.attrs
        if attres.keys().__contains__('title'):
            infos.append((link['title'], link['href']))

    # 遍历每个专业大类
    for info in infos:
        print(info)
        info_url = info[1]
        max_page = 10**7
        cur_age = 1
        while cur_age <= max_page:
            # 保存专业
            sub_infos = []

            info_url_abs = parse.urljoin(url, info_url)
            print(info_url_abs)
            info_soup = parse2bs(info_url_abs)
            # 总页数
            max_page = int(info_soup.find_all('li')[1].text.split('/')[1][0:-1])
            print('------------------------------------')
            u_table = info_soup.find('tbody', attrs={'id': 'lists'})
            u_trs = u_table.find_all('tr')
            for u_tr in u_trs:
                sub_info = []
                sub_infos.append(sub_info)

                u_tds = u_tr.find_all('td')
                for u_td in u_tds:
                    sub_info.append(u_td.text)

                # 获取专业详情
                sub_info_desc_soup = parse2bs(parse.urljoin(url, u_tds[3].find('a')['href']))
                box1 = sub_info_desc_soup.find('div', attrs={'class': 'box box1'})
                box2 = sub_info_desc_soup.find('div', attrs={'class': 'box box2'})
                box3 = sub_info_desc_soup.find('div', attrs={'class': 'box box3'})
                box4 = sub_info_desc_soup.find('div', attrs={'class': 'box box4'})
                sub_info.append([box1.text, box2.text, box3.text, box4.text])

            for sub_info in sub_infos:
                print(sub_info)

            # 获取下一页地址
            nextPage = info_soup.find('ul', attrs={'id': 'pageUl'}).find_all('a')[-1]
            info_url = nextPage['href']

            cur_age = cur_age + 1


if __name__ == '__main__':
    soup = parse2bs(url)
    friend_links = soup.find_all(name='div', attrs={'class': 'friend_links wrap1200'})
    parse_local_u(friend_links[1])
    # subject_extract(friend_links[2])
