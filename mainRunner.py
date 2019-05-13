# coding:utf8
from common.Excel import *
from inter.httpkeywordbyexcel import HTTP

if __name__ == "__main__":
    print("主框架入口")

    http = HTTP()

    reader = Reader()
    reader.open_excel('./lib/cases/HTTP接口用例.xls')
    sheetname = reader.get_sheets()
    # for sheet in sheetname:
    #     # 设置当前读取的sheet页面
    #     reader.set_sheet(sheet)
    #     for i in range(reader.rows):
    #         print(reader.readline())
    reader.set_sheet(sheetname[1])
    for i in range(reader.rows):
        line = reader.readline()
        print(line[3])
        if line[3] == 'seturl':
            http.seturl(line[4])
        if line[3] == 'removeheader':
            http.removeheader(line[4])
        if line[3] == 'post':
            print(line[5])
            http.post(line[4],line[5])
        if line[3] == 'assertequals':
            http.assertequals(line[4],line[5])
        if line[3] == 'addheader':
            http.addheader(line[4])
        if line[3] == 'savejson':
            http.savejson(line[4],line[5])

    # writer = Writer()
    # ctime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # writer.copy_open('./lib/cases/HTTP接口用例.xls', './lib/results/result-HTTP接口用例' + ctime +'.xls')
    # sheetname = writer.get_sheets()
    # writer.set_sheet(sheetname[0])
    # writer.write(1, 1, 'William')
    # writer.save_close()