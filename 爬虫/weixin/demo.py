import json
import re
import time
import pymysql
import requests
from lxml import etree
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Gzh_wz(object):
    def __init__(self):
        # self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='test')
        # self.cursor = self.conn.cursor()
        with open('title.txt', 'r', encoding='utf-8') as r:
            titles = r.read().replace('\ufeff', '')
            self.title_l = titles.split('\n')
        self.cookie = input('cookie：')
        self.pass_ticket = input('pass_ticket:')
        self.url_dict = {
            '揭阳蓝城生活': 'https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=5&fakeid=MzI0MTA2MDMwMA==&type=9&query=&token=abcd&lang=zh_CN&f=json&ajax=1',
            '揭东生活圈': 'https://mp.weixin.qq.com/cgi-bin/appmsg?action=list_ex&begin=0&count=5&fakeid=MzI0MzA1ODc0NQ==&type=9&query=&token=abcd&lang=zh_CN&f=json&ajax=1'
        }
        self.headers = {
            'cookie': self.cookie,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'referer': 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&token=370616041&lang=zh_CN',
        }
        self.app_url = "http://mp.weixin.qq.com/mp/getappmsgext"
        phoneCookie = "rewardsn=; wxtokenkey=777; wxuin=1797234910; devicetype=Windows10x64; version=62090529; lang=zh_CN; pass_ticket=hjymD+nRjMwS6tz25jYr1rByJW9Yzu8L6Y+I6VDM8EK8bM7Ltcee1dTvMsr6A2I1; wap_sid2=CN7B/tgGElxnWXktSExLc0EyTVFVNGJMTjJ5eVhwSWNDQk5tRHhSd21NaGZNMUoxaWJRdzBlcUJxZG1XUEtuQ1JTekt4dXctS3hLaVFWU0xqdWQxNVJleFAxTGZ4akVFQUFBfjDi67T5BTgNQAE="
        self.app_headers = {
            "Cookie": phoneCookie,
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400"
        }
        self.data = {
            "is_only_read": "1",
            "is_temp_url": "0",
            "appmsg_type": "9",
            'reward_uin_count': '0'
        }

    def get_link(self):
        for name, url in self.url_dict.items():
            print(name)
            self.url = url.replace('abcd', '1897236457')
            res = requests.get(self.url, headers=self.headers, verify=False).text
            res_dict = json.loads(res)
            details = res_dict['app_msg_list']
            self.appmsg_token = input('appmsg_token:')
            if self.appmsg_token == '1':
                continue
            self.key = input('key:')
            for detail in details:
                self.title = detail['title']
                self.detail_url = detail['link']
                self.get_response(detail)
        # self.conn.close()

    def get_response(self, detail):
        self.detail_res = requests.get(self.detail_url, headers=self.headers, verify=False).text
        con = ''.join(
            re.findall(r'<div class="rich_media_content " id="js_content".*?</div>', self.detail_res, re.DOTALL))
        video = re.search(r'video', con)
        if video:
            return None
        con = con.replace('\n', '').replace('style="visibility: hidden;"', '').replace('data-src', 'src')
        rep = re.search(r'<img.*?>', con, re.DOTALL)
        if rep:
            rep = rep.group()
        rep1 = '点击上方蓝色字体，关注我们'
        rep2 = '给我点【在看】你也越好看'
        self.content = con.replace(str(rep), '').replace(rep1, '').replace(rep2, '')
        publish = detail['create_time']
        self.cover_img = detail['cover']
        times = int(publish)
        timess = time.localtime(times)
        self.publish_time = time.strftime("%Y-%m-%d %H:%M:%S", timess)
        self.create_time = str(time.strftime("%Y-%m-%d %H:%M:%S"))
        create_time_date = self.create_time.split(' ')[0]
        re_time = re.findall(create_time_date, str(self.publish_time))
        if re_time:
            print('--' * 50)
            print(self.publish_time)
        else:
            return None
        if self.title in self.title_l:
            return None
        else:
            self.title_l.append(self.title)
            with open('title.txt', 'a', encoding='utf-8')as w:
                w.write('\n')
                w.write(self.title)
        self.tt_dict = {x.split('=')[0]: x.split('=')[1] for x in self.detail_url.split('&')}
        print(self.tt_dict)
        if self.tt_dict['idx'] == '1':
            self.is_headline = '1'
        else:
            self.is_headline = '0'
        detail_ret = etree.HTML(self.detail_res)
        fro = detail_ret.xpath('//span[contains(text(), "来源：")]')
        self.gzh_name = ''.join(detail_ret.xpath('//a[@id="js_name"]/text()')).strip()
        self.author = ' '
        if fro:
            self.is_original = '0'
        else:
            self.is_original = '1'
        self.get_nums()
        return None

    def get_nums(self):
        mid = self.detail_url.split("&")[1].split("=")[1]
        idx = self.detail_url.split("&")[2].split("=")[1]
        sn = self.detail_url.split("&")[3].split("=")[1]
        _biz = self.detail_url.split("&")[0].split("_biz=")[1]
        params = {
            "__biz": _biz,
            "mid": mid,
            "sn": sn,
            "idx": idx,
            "key": self.key,
            "pass_ticket": self.pass_ticket,
            "appmsg_token": self.appmsg_token,
            "uin": "MTc5NzIzNDkxMA==",
            "wxtoken": "777",
        }
        con2 = requests.post(self.app_url, headers=self.app_headers, data=self.data, params=params, verify=False).json()
        try:
            self.pageview = con2["appmsgstat"]["read_num"]
        except:
            self.pageview = 0

        try:
            self.look_count = con2["appmsgstat"]["like_num"]
        except:
            self.look_count = 0

        try:
            self.like_count = con2["appmsgstat"]['old_like_num']
        except:
            self.like_count = 0
        print(self.like_count)
        print(self.look_count)
        print(self.pageview)
        # self.deposit_mysql()
        return None

    # def deposit_mysql(self):
    #     sql = "insert into gzh_article(id, gzh_name, author, title, is_original, publish_time, is_headline, content, pageview, look_count, org_url, cover_img, like_count, create_time, import_time) values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, null)"
    #     self.cursor.execute(sql, (
    #         self.gzh_name, self.author, self.title, self.is_original, self.publish_time, self.is_headline, self.content,
    #         self.pageview, self.look_count, self.detail_url, self.cover_img, self.like_count, self.create_time))
    #     self.conn.commit()
    #     time.sleep(1)
    #     return None


if __name__ == '__main__':
    gzh = Gzh_wz()
    gzh.get_link()
