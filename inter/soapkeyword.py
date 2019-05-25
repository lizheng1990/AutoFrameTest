# coding:utf8
import json

import jsonpath
from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor

from common.logger import logger


class SOAP:
    def __init__(self):
        # 设置基本url
        self.wsdl = ""
        # 设置返回信息值
        self.result = None
        # 设置返回信息json格式
        self.jsonre = None
        # 设置存储变量值的参数
        self.jsonparams = {}
        self.doctor = None
        self.client = None
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

    def adddoctor(self,location='',namespace=''):
        imp = Import('http://www.w3.org/2001/XMLSchema', location=location)
        imp.filter.add(namespace)
        self.doctor = ImportDoctor(imp)

    def setwsdl(self,url):
        self.wsdl = url
        self.client = Client(self.wsdl,headers = self.headers, doctor = self.doctor)

    def removeheader(self,key):
        try:
            self.headers.pop(key)
            # self.writer.write(self.writer.row, self.writer.clo, "PASS")
            # self.writer.write(self.writer.row, self.writer.clo + 1, str(self.session.headers))
            logger.info(str(self.headers))
        except Exception as e:
            # self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            # self.writer.write(self.writer.row, self.writer.clo + 1, e)
            logger.exception(e)
        self.client = Client(self.wsdl, headers=self.headers, doctor=self.doctor)

    def addheader(self,key,p=None):
        try:
            value = self.__get_value(p)
            self.headers[key] = value
            # self.writer.write(self.writer.row,self.writer.clo,"PASS")
            # self.writer.write(self.writer.row,self.writer.clo+1,str(self.session.headers))
            logger.info(str(self.headers))
        except Exception as e:
            # self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            # self.writer.write(self.writer.row,self.writer.clo+1,e)
            logger.exception(e)
        self.client = Client(self.wsdl, headers=self.headers, doctor=self.doctor)

    def callmethod(self,m,p=None):
        p = self.__get_value(p)
        try:
            if p == '':
                params = []
            else:
                try:
                    params = p.split('、')
                except Exception as e:
                    params = []
            self.result = self.client.service.__getattr__(m)(*params)
            print(self.result)
            self.jsonre = json.loads(self.result)
            logger.info(m)
            logger.info(p)
            logger.info(str(self.jsonre))
        except Exception as e:
            logger.info(m)
            logger.info(p)
            logger.exception(e)

    def assertequals(self,key,p):
        try:
            value = self.__get_value(p)
            if str(jsonpath.jsonpath(self.jsonre, key)[0]) == str(value):
                print('PASS')
                logger.info(str(self.jsonre))
            else:
                print('FAIL')
                logger.error(str(self.jsonre))
        except Exception as e:
            print('FAIL')
            logger.exception(e)

    # 保存值到jsonparams中
    def savejson(self, key, value):
        try:
            self.jsonparams[value] = str(jsonpath.jsonpath(self.jsonre, key)[0])
        except Exception as e:
            logger.exception(e)

    # 获取保存的参数值
    def __get_value(self, p=None):
        if p is None:
            p = ''
            return p
        else:
            for key in self.jsonparams.keys():
                p = p.replace("{" + key + "}", self.jsonparams[key])
            return p