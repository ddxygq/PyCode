# -*- coding: utf-8 -*-
"""
 @Time   : 2020/10/29 9:54
 @Athor   : LinXiao
 @功能   :
"""
# ------------------------------
import datetime
import io
import random
import string
import uuid

import requests
import oss2


# 储存的路径
# filePath="/house/2020-10-29/xxxx.jpg"  # xxxxx  wei
# # 指定Bucket实例，所有文件相关的方法都需要通过Bucket实例来调用。
# bucket=oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)

def parser(img, imageName, dirpath):
    endpoint = 'http://oss-cn-chengdu.aliyuncs.com'
    access_key_id = 'LTAI4FzinZX9M4**************'
    access_key_secret = 'x97sjRShD***************'
    bucket_name = 'fzp-*****************'
    # 指定Bucket实例，所有文件相关的方法都需要通过Bucket实例来调用。
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
    result = bucket.put_object(f'{dirpath}/{imageName}', img.getvalue())
    print('图片上传oss success!')
    return result.status


def main(url):
    # 测试的阿里云oss储存路径,正式的为house
    dirpath = 'house-test'
    domain = 'http://oss.fapai******fang.top/'

    now = datetime.datetime.now()
    nonce = str(uuid.uuid4())

    random_name = now.strftime("%Y-%m-%d") + "/" + nonce

    imageName = '{}.jpg'.format(random_name)

    img = io.BytesIO(requests.get(url, timeout=300).content)

    statusCode = parser(img, imageName, dirpath)

    if statusCode == 200:
        new_oss_url = domain + dirpath + '/' + imageName
        print(new_oss_url)
        # print(type(new_oss_url))   # <class 'str'>
        return new_oss_url


if __name__ == '__main__':
    # url='https://img.alicdn.com/bao/uploaded/i3/TB1LMGLiP39YK4jSZPctrBrUFXa_460x460.jpg'
    url = 'https://img.alicdn.com/bao/uploaded/i4/O1CN01CW2jEc1pOLaFef85M_!!0-paimai.jpg_460x460.jpg'

    main(url)