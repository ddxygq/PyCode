"""
遍历目录下的所有文件夹下的目录和文件，生成github文章目录
"""

import os

path = 'D:\\我的文件\\Java大数据与数据仓库\\all-kinds-book'

__EXCLUDE_DIR__ = ['.git', '面试题']


def generate_list(path):
    indexs = path.split('\\')[4:]
    # 锚点
    if len(indexs) > 0:
        print((len(indexs) - 1) * '  ' + '- [' + indexs[-1] + '](#' + '-'.join(indexs) + ')')

    # 文章目录
    # print(len(indexs)*'#' + ' ' + '-'.join(indexs))

    files = os.listdir(path)
    for file in files:
        abs_path = os.path.join(path, file)
        if os.path.isfile(abs_path):
            name = file.split('.')[0]
            # 文章链接
            # print('- [%s](%s)' % (name, '/'.join(abs_path.replace('\\', '/').split('/')[4:])))
        if os.path.isdir(abs_path) and file not in __EXCLUDE_DIR__:
            generate_list(abs_path)


if __name__ == '__main__':
    generate_list(path)
