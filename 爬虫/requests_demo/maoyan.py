import requests
from requests.exceptions import  RequestException
import re
import json

def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def get_data(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?<img.*?alt.*?src="(.*?)".*?</a>.*?data-act.*?>(.*?)'
                          + '</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield{
            'index': item[0],
            'image': item[1],
            'name': item[2].strip(),
            'actor': item[3].split('：')[-1].strip(),
            'time': item[4].split('：')[-1].strip(),
            'score': item[5] + item[6]
        }


if __name__ == '__main__':
    base_url = 'https://maoyan.com/board/4?offset='
    for i in range(10):
        url = base_url + str(i*10)
        items = get_data(get_page(url))
        with open('D:\logs\猫眼.txt','a', encoding='utf-8') as f:
            for item in items:
                f.writelines(json.dumps(item, ensure_ascii=False))
