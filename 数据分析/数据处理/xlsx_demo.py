import xlrd
import xlwt
import re


def _re(regx, s):
    pattern = re.compile(regx)
    results = pattern.search(s)
    if results:
        return results[0]
    else:
        return ''


def read_excel(file_name, sheet):
    """
    读取excel数据
    :return:
    """

    # 读取excel
    data = xlrd.open_workbook(file_name)
    Sheet1 = data.sheet_by_name(sheet)

    rows = [(0, '序号', '姓名', '销售额')]
    for rownumber in range(1, Sheet1.nrows):
        row_data = Sheet1.row_values(rownumber)

        # 取出数字
        pattern = '[1-9]\d*\.?\d*|0\.\d*[1-9]'
        row_data[2] = _re(r'{}'.format(pattern), row_data[2])
        rows.append((rownumber, int(row_data[0]), row_data[1], row_data[2]))

    return rows


def write_excel(rows, filename, sheet):
    # 写excel
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet(sheet)
    for row in rows:
        worksheet.write(row[0], 0, row[1])
        worksheet.write(row[0], 1, row[2])
        worksheet.write(row[0], 2, row[3])
    workbook.save(filename)


if __name__ == '__main__':

    # 读取excel
    file_name = '1.xlsx'
    sheet = 'Sheet1'
    rows = read_excel(file_name, sheet)

    # 保存到excel
    print(rows)
    write_excel(rows, '_1.xlsx', 'Sheet1处理结果')
