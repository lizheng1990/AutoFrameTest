# coding:utf8
import inspect

from common.Excel import *
from inter.httpkeywordbyexcel import HTTP
reader = Reader()
writer = Writer()
http = HTTP(writer)
reader.open_excel('./lib/cases/HTTP接口用例.xls')
sheetname = reader.get_sheets()
for sheet in sheetname:
    # 设置当前读取的sheet页面
    reader.set_sheet(sheet)
    for i in range(reader.rows):
        line = reader.readline()
        if len(line[0]) > 0 or len(line[1]) > 0:
            pass
        else:
            func = getattr(http, line[3])
            print(func)
            p = inspect.getfullargspec(func).__str__()
            p = p[p.find("args=")+5:p.find(", varargs")]
            p = eval(p)
            print(type(p))
            p.remove('self')
            print(p)