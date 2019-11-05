import os


def run():
    """
    将目录中的所有csv文件中的T, Z去掉。
    :return:
    """
    path = '.'
    for file in os.listdir(path):
        if not os.path.isdir(file) and ".csv" in file:
            file_modify = file + "_"
            with open(file, 'r') as f:
                f_modify = open(file_modify, 'a+')
                line = f.readline().strip()
                while line:
                    s = line.split(",")
                    if len(s) == 2:
                        s[1] = s[1].replace('T', '').replace('Z', '')
                        f_modify.writelines(",".join(s) + "\n")
                    line = f.readline().strip()
                f_modify.close()


if __name__ == '__main__':
    run()
