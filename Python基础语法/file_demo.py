import os

"""
多层文件夹下面有很多文件，删除除了.jpg, .R, .pptx 以外的所有文件.
"""

path = 'D:\我的文件\网易云课堂\R语言\资料'
g = os.walk(path)

for path, dir_list, file_list in g:
    for file_name in file_list:
        whole_path = os.path.join(path, file_name)
        if 'pptx' not in whole_path and '.jpg' not in whole_path and '.R' not in whole_path:
            os.remove(whole_path)
