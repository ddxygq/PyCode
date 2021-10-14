# -*- coding: utf-8 -*-
"""
 @Time   : 2020/10/29 9:54
 @Athor   : LinXiao
 @功能   :
"""
# ------------------------------
import datetime
import io
import uuid

import requests
import oss2


def get_bucket():
    endpoint = 'http://oss-cn-shanghai.aliyuncs.com'
    access_key_id = '阿里云oss的key'
    access_key_secret = '阿里云oss的secret'
    bucket_name = 'ikeguang.com'
    bucket = oss2.Bucket(oss2.Auth(access_key_id, access_key_secret), endpoint, bucket_name)
    return bucket


def put_image(url, dirpath='image', headers={'Content-Type': 'image/jpg'}):
    """
    上传文件到oss，并且返回oss地址
    :param url: 网络上的图片地址
    :param dirpath: 要保存到oss的地址
    :param headers: 用户指定的HTTP头部。可以指定Content-Type、Content-MD5、x-oss-meta-开头的头部，Content-Type文档：https://help.aliyun.com/knowledge_detail/39522.html
    :return: 上传后图片在oss的地址
    """

    access_domain = 'https://ikeguang.oss-cn-shanghai.aliyuncs.com'

    # 随机生成图片地址
    now = datetime.datetime.now()
    nonce = str(uuid.uuid4())
    random_name = now.strftime("%Y-%m-%d") + "/" + nonce
    image_name = '{}.jpg'.format(random_name)
    img = io.BytesIO(requests.get(url, timeout=300).content)

    # headers的设置可以看：https://help.aliyun.com/knowledge_detail/39522.html
    bucket = get_bucket()
    result = bucket.put_object(f'{dirpath}/{image_name}', img.getvalue(), headers)

    if result.status == 200:
        return f'{access_domain}/{dirpath}/{image_name}'


if __name__ == '__main__':
    url = 'https://ikeguang.oss-cn-shanghai.aliyuncs.com/image/2021-10-14/2a002f37-5724-4575-9cec-c436e9bcd7d8.jpg'
    path = put_image(url)
    print(path)
