# coding:utf8

import requests,json

from common.logger import logger


class HTTP():
    # writer = Writer()
    def __init__(self,w):
        # 设置初始化session
        self.session = requests.session()
        # 设置基本url
        self.url = ""
        # 设置参数map
        self.params = {}
        # 设置返回信息值
        self.result = None
        # 设置返回信息json格式
        self.jsonre = None
        # 设置存储变量值的参数
        self.jsonparams = {}
        self.writer = w

# 设置基本url
    def seturl(self,url):
        try:
            self.url = url
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            self.writer.write(self.writer.row,self.writer.clo+1,str(self.url))
            logger.info(self.url)
        except  Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,e)
            logger.exception(e)

# 清除header中的参数
    def removeheader(self,key):
        try:
            self.session.headers.pop(key)
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            self.writer.write(self.writer.row,self.writer.clo+1,str(self.session.headers))
            logger.info(str(self.session.headers))
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,e)
            logger.exception(e)

# 增加header中的参数
    def addheader(self,key,p=None):
        try:
            value = self.__get_value(p)
            self.session.headers[key] = value
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            self.writer.write(self.writer.row,self.writer.clo+1,str(self.session.headers))
            logger.info(str(self.session.headers))
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,e)
            logger.exception(e)

# post封装
    def post(self,path,p=None):
        try:
            self.result = self.session.post(self.url+"/"+path,self.__get_params(p))
            self.jsonre = json.loads(self.result.text)
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            self.writer.write(self.writer.row,self.writer.clo+1,str(self.jsonre))
            logger.info(str(str(self.jsonre)))
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,e)
            logger.exception(e)

    # get封装
    def get(self,path,p=None):
        try:
            path = path + "?" + p
            self.result = self.session.get(self.url+"/"+path)
            self.jsonre = json.loads(self.result.text)
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            self.writer.write(self.writer.row,self.writer.clo+1,str(self.jsonre))
            logger.info(str(str(self.jsonre)))
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,e)
            logger.exception(e)

    def __to_json(self,re):
        return re[re.find("(")+1:re.find(")")]

# 设置参数格式为dict
    def __get_params(self,p):
        self.params.clear()
        if p is None or p == "":
            return self.params
        else:
            params_list = p.split("&")
            for param in params_list:
                key = param.split("=")[0]
                value = param.split("=")[1]
                self.params[key] = value
            return self.params

# 断言封装
    def assertequals(self,key,value):
        try:
            if str(self.jsonre[key]) == value:
                # print("PASS")
                self.writer.write(self.writer.row,self.writer.clo,"PASS")
                self.writer.write(self.writer.row,self.writer.clo+1,str(self.jsonre[key]))
                logger.info(str(str(self.jsonre)))
            else:
                # print("FAIL")
                self.writer.write(self.writer.row,self.writer.clo,"FAIL")
                self.writer.write(self.writer.row,self.writer.clo+1,str(self.jsonre[key]))
                logger.error(str(str(self.jsonre)))
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,e)
            logger.exception(e)

# 保存值到jsonparams中
    def savejson(self,key,value):
        try:
            self.jsonparams[value] = self.jsonre[key]
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            self.writer.write(self.writer.row,self.writer.clo+1,str(self.jsonparams))
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,e)
            logger.exception(e)

# 获取保存的参数值
    def __get_value(self,p=None):
        if p is None:
            return p
        else:
            for key in self.jsonparams.keys():
                p = p.replace("{" + key + "}", self.jsonparams[key])
            return p




















