# coding:utf8
import inspect

from common.Excel import *
from inter.httpkeywordbyexcel import HTTP

def runCases(line):
    if len(line[0]) > 0 or len(line[1]) > 0:
        pass
    else:
        # if line[3] == 'seturl':
        #     http.seturl(line[4])
        # if line[3] == 'removeheader':
        #     http.removeheader(line[4])
        # if line[3] == 'post':
        #     http.post(line[4], line[5])
        # if line[3] == 'assertequals':
        #     http.assertequals(line[4], line[5])
        # if line[3] == 'addheader':
        #     http.addheader(line[4], line[5])
        # if line[3] == 'savejson':
        #     http.savejson(line[4], line[5])

        func = getattr(http, line[3])
        p = inspect.getfullargspec(func).__str__()
        p = p[p.find("args=") + 5:p.find(", varargs")]
        p = eval(p)
        p.remove('self')

        if len(p) == 0:
            func()
        elif len(p) == 1:
            func(line[4])
        elif len(p) == 2:
            func(line[4],line[5])
        elif len(p) == 3:
            func(line[4],line[5],line[6])
        else:
            print("waring:只支持三个参数！")


if __name__ == "__main__":
    reader = Reader()
    writer = Writer()
    http = HTTP(writer)
    ctime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    reader.open_excel('./lib/cases/HTTP接口用例.xls')
    writer.copy_open('./lib/cases/HTTP接口用例.xls', './lib/results/result-HTTP接口用例' + ctime +'.xls')
    sheetname = reader.get_sheets()
    for sheet in sheetname:
        # 设置当前读取的sheet页面
        reader.set_sheet(sheet)
        writer.set_sheet(sheet)
        for i in range(reader.rows):
            writer.row = i
            writer.clo = 7
            line = reader.readline()
            runCases(line)
    writer.save_close()