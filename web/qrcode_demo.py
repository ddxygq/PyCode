import qrcode
import sys


def run(url, path):
    """
    Python生成二维码
    :param url: 要做成二维码的url地址
    :param path:  二维码的名称，即完整路径
    :return:
    """
    qr_image = qrcode.make(url)
    qr_image.save(path)


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print('argv lenth invalid')
        print('please input cmd like python qrgenerator.py https://www.baidu.com e:/a.jpg')
        sys.exit(1)

    # https://www.baidu.com
    url = args[1]

    # d:/a.png
    path = args[2]

    run(url, path)