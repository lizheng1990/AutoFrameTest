# coding:utf8
import inspect

from common.Excel import *
from common import config
from common.excelresult import Res
from common.mail import Mail
from inter.httpkeywordbyexcel import HTTP

def runCases(line):
    if len(line[0]) > 0 or len(line[1]) > 0:
        pass
    else:
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
    res = Res()
    reader = Reader()
    writer = Writer()
    http = HTTP(writer)
    start_time = time.time()
    ctime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    reader.open_excel('./lib/cases/HTTP接口用例.xls')
    writer.copy_open('./lib/cases/HTTP接口用例.xls', './lib/results/result-HTTP接口用例' + ctime +'.xls')
    sheetname = reader.get_sheets()
    writer.set_sheet(sheetname[0])
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(start_time)
    writer.write(1,3,str(start_time))
    for sheet in sheetname:
        # 设置当前读取的sheet页面
        reader.set_sheet(sheet)
        writer.set_sheet(sheet)
        for i in range(reader.rows):
            writer.row = i
            writer.clo = 7
            line = reader.readline()
            runCases(line)
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(end_time)
    writer.set_sheet(sheetname[0])
    writer.write(1,4,str(end_time))
    writer.save_close()
    r = res.get_res('./lib/results/result-HTTP接口用例' + ctime +'.xls')
    print(r)
    # config.get_config('./lib/conf/conf.properties')
    # mail = Mail()
    # mail.mail_info['mail_subject'] = '接口测试结果邮件' + '_' + ctime
    # mail.mail_info['filepaths'] = ['./lib/results/result-HTTP接口用例' + ctime +'.xls']
    # mail.mail_info['filenames'] = ['result-HTTP接口用例' + ctime +'.xls']
    # mail.send(mail.mail_info['html'])