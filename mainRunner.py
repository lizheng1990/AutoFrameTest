# coding:utf8
import inspect

from app.appkeywordbyexcel import APP
from common.Excel import *
from common import config
from common.excelresult import Res
from common.mail import Mail
from common.mysql import Mysql
from inter.httpkeywordbyexcel import HTTP
from inter.soapkeywordbyexcel import SOAP
from web.webkeywordbyexcel import WEB


def runCases(line,type):
    if len(line[0]) > 0 or len(line[1]) > 0 or len(line[2]) == 0:
        pass
    else:
        func = getattr(type, line[3])
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
    key = 'APP'
    if key == 'HTTP':
        runType = HTTP(writer)
        name = 'HTTP接口'
    elif key == 'SOAP':
        runType = SOAP(writer)
        name = 'SOAP接口'
    elif key == 'REST':
        runType = HTTP(writer)
        name = 'REST接口'
    elif key == 'WEB':
        runType = WEB(writer)
        name = 'WEB'
    elif key == 'APP':
        runType = APP(writer)
        name = 'APP'
    ctime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    case = './lib/cases/' + name + '用例'
    result = './lib/results/result-' + name + '用例'
    reader.open_excel(case + '.xls')
    writer.copy_open(case + '.xls', result + ctime +'.xls')
    sheetname = reader.get_sheets()
    writer.set_sheet(sheetname[0])
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    writer.write(1,3,str(start_time))
    for sheet in sheetname:
        # 设置当前读取的sheet页面
        reader.set_sheet(sheet)
        writer.set_sheet(sheet)
        for i in range(reader.rows):
            writer.row = i
            writer.clo = 7
            line = reader.readline()
            runCases(line, runType)
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    writer.set_sheet(sheetname[0])
    writer.write(1,4,str(end_time))
    writer.save_close()
    r = res.get_res(result + ctime +'.xls')
    print(r)
    config.get_config('./lib/conf/conf.properties')

    mysql = Mysql()
    mysql.init_mysql('C:\\Users\\leez\\Documents\\Navicat\\MySQL\\servers\\112\\test_project\\userinfo.sql')

    mail = Mail()
    mail.mail_info['mail_subject'] = r['title'] + '_' + ctime
    mail.mail_info['filepaths'] = [result + ctime +'.xls']
    mail.mail_info['filenames'] = ['result-' + name + '用例' + ctime +'.xls']
    config.config['mail_html'] = config.config['mail_html'].replace('title',r['title'])
    if r['status'] == 'Fail':
        config.config['mail_html'] = config.config['mail_html'].replace('color: #00d800;">status','color: #FF0000;">status')
        config.config['mail_html'] = config.config['mail_html'].replace('status',r['status'])
    else:
        config.config['mail_html'] = config.config['mail_html'].replace('status',r['status'])
    config.config['mail_html'] = config.config['mail_html'].replace('runtype',r['runtype'])
    config.config['mail_html'] = config.config['mail_html'].replace('passrate',r['passrate'])
    config.config['mail_html'] = config.config['mail_html'].replace('starttime',r['starttime'])
    config.config['mail_html'] = config.config['mail_html'].replace('casecount',r['casecount'])
    config.config['mail_html'] = config.config['mail_html'].replace('endtime',r['endtime'])
    mail.send(config.config['mail_html'])
