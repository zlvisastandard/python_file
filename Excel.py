import xlrd


def Open_Excel():
    file = "/Users/zhangliang/Desktop/全渠道/v2.1.0-全渠道-测试用例支付宝-20190429.xlsx"
    data = xlrd.open_workbook(file)
    return data

def Shell_Excel():
    data = Open_Excel()
    table = data.sheets()[0]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    list_a = ["\n"]
    for i in range(0,nrows):
        list_a.append(table.row_values(i))
    print(list_a)



def main():
    res = Shell_Excel()
    # print(res)


if __name__ == '__main__':
    main()