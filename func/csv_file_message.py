import csv
import os


# 读取csv文件的方法
def reader(filename):
    # 先定位当前路径
    base_path = os.path.dirname(__file__)
    # 在替换成test_data/下
    path = base_path.replace("func", "test_data/" + filename)
    table_list = []
    # 打开文件后关闭文件
    with open(path) as file:
        # 读取文件数据
        table = csv.reader(file)
        num = 0
        # 循环读取每一行数据，最后输出一个列表，第一行是标题需要跳过
        for row in table:
            if num != 0:
                table_list.append(row)
            num = num + 1
    return table_list
