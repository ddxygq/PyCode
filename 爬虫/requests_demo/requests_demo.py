import requests
from urllib import parse
from bs4 import BeautifulSoup

url = 'https://www.zhaogaoxiao.com/'

# 加上请求头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/86.0.4240.75 Safari/537.36'}
re = requests.get(url, headers=headers)
soup = BeautifulSoup(re.content, features='html.parser')
friend_links = soup.find_all(name='div', attrs={'class': 'friend_links wrap1200'})[1:2]

for friend_link in friend_links:
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
    for info in infos:
        info_url = info[1]
        while '/' in info_url:
            info_url_abs = parse.urljoin(url, info_url)
            print(info_url_abs)
            info_soup = BeautifulSoup(requests.get(info_url_abs, headers=headers).content, features='html.parser')
            print('------------------------------------')
            u_table = info_soup.find_all('table', attrs={'id': 'table'})
            u_trs = u_table[0].find_all('tr')
            u_infos = []

            # 表头
            u_table_header = []
            u_tr = u_trs[0]
            for th in u_tr.find_all('th')[:-2]:
                u_table_header.append(th.text)
            u_infos.append(u_table_header)

            # 表格内容
            for u_tr in u_trs[1:]:
                u_tds = u_tr.find_all('td')
                ulogo = parse.urljoin(url, u_tds[0].find('img')['src'])
                u_info = [ulogo]
                for u_td in u_tds[1:-2]:
                    u_info.append(u_td.text)
                u_infos.append(u_info)

            for u_info in u_infos:
                print(u_info)

            # 获取下一页地址
            nextPage = info_soup.find('ul', attrs={'id': 'pageUl'}).find_all('a')[-1]
            info_url = nextPage['href']
