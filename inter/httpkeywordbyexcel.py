# coding:utf8

import requests,json,jsonpath

from common.logger import logger


class HTTP():
    def __init__(self,w):
        # 设置初始化session
        self.session = requests.session()
        # 设置基本url
        self.url = ""
        # 设置参数map
        self.params = {}
        # 设置返回信息值
        self.result = None
        self.status = ""
        # 设置返回信息json格式
        self.jsonre = None
        # 设置存储变量值的参数
        self.jsonparams = {}
        self.writer = w
        self.session.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

# 设置基本url
    def seturl(self,url):
        try:
            self.url = url
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            self.writer.write(self.writer.row,self.writer.clo+1,str(self.url))
            logger.info(self.url)
        except  Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
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
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
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
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

# post封装
    def post(self,path,p=None):
        path = self.__get_value(path)
        try:
            if p.find("=")>=0 or p == "":
                self.result = self.session.post(self.url + "/" + path,data=self.__get_params(p))
            else:
                self.result = self.session.post(self.url + "/" + path + '?' + p)
            if int(self.result.status_code) > 300:
                self.status = str(self.result.status_code)
                self.writer.write(self.writer.row, self.writer.clo, "PASS")
                self.writer.write(self.writer.row, self.writer.clo + 1, str(self.result.status_code))
            else:
                self.status = str(self.result.status_code)
                self.jsonre = json.loads(self.result.text)
                self.writer.write(self.writer.row, self.writer.clo, "PASS")
                self.writer.write(self.writer.row, self.writer.clo + 1, str(self.jsonre))
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def post_rest(self, path, p=None):
        path = self.__get_value(path)
        try:
            if p.find("=")>=0 or p == "":
                self.result = self.session.post(self.url + "/" + path,data=self.__get_params(p))
            else:
                self.result = self.session.post(self.url + "/" + path + '?' + p)
            if int(self.result.status_code) > 300:
                self.status = str(self.result.status_code)
                self.writer.write(self.writer.row, self.writer.clo, "PASS")
                self.writer.write(self.writer.row, self.writer.clo + 1, str(self.result.status_code))
            else:
                self.status = str(self.result.status_code)
                self.jsonre = json.loads(self.result.text)
                self.writer.write(self.writer.row,self.writer.clo,"PASS")
                self.writer.write(self.writer.row,self.writer.clo+1,str(self.jsonre))
            logger.info(str(self.jsonre))
        except Exception as e:
            self.writer.write(self.writer.row, self.writer.clo, "FAIL")
            self.writer.write(self.writer.row, self.writer.clo + 1, str(e))
            logger.exception(e)

    # get封装
    def get(self,path,p=None):
        try:
            path = path + "?" + p
            self.result = self.session.get(self.url+"/"+path)
            self.jsonre = json.loads(self.result.text)
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            self.writer.write(self.writer.row,self.writer.clo+1,str(self.jsonre))
            logger.info(str(self.jsonre))
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def get_rest(self,path,p=None):
        try:
            path = path + "?" + p
            self.result = self.session.get(self.url+"/"+path)
            self.jsonre = json.loads(self.result.text)
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            self.writer.write(self.writer.row,self.writer.clo+1,str(self.jsonre))
            logger.info(str(self.jsonre))
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
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
    def assertequals(self,key,p):
        value = self.__get_value(p)
        try:
            if int(self.status) > 300:
                if key == "status":
                    if self.status == value:
                        self.writer.write(self.writer.row, self.writer.clo, "PASS")
                        self.writer.write(self.writer.row, self.writer.clo + 1, str(self.status))
                        logger.info(str(self.status))
                    else:
                        self.writer.write(self.writer.row, self.writer.clo, "FAIL")
                        self.writer.write(self.writer.row, self.writer.clo + 1, str(self.status))
                        logger.error(str(self.status))
                else:
                    self.writer.write(self.writer.row, self.writer.clo, "FAIL")
                    self.writer.write(self.writer.row, self.writer.clo + 1, str(self.status))
                    logger.error(str(self.status))
            else:
                if str(jsonpath.jsonpath(self.jsonre, key)[0]) == str(value):
                    self.writer.write(self.writer.row,self.writer.clo,"PASS")
                    self.writer.write(self.writer.row,self.writer.clo+1,str(self.jsonre))
                    logger.info(str(self.jsonre))
                else:
                    self.writer.write(self.writer.row,self.writer.clo,"FAIL")
                    self.writer.write(self.writer.row,self.writer.clo+1,str(self.jsonre))
                    logger.error(str(self.jsonre))
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

# 保存值到jsonparams中
    def savejson(self,key,value):
        try:
            self.jsonparams[value] = str(jsonpath.jsonpath(self.jsonre, key)[0])
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            self.writer.write(self.writer.row,self.writer.clo+1,str(self.jsonparams))
            logger.info(self.jsonparams)
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

# 获取保存的参数值
    def __get_value(self,p=None):
        if p is None:
            return p
        else:
            for key in self.jsonparams.keys():
                p = p.replace("{" + key + "}", self.jsonparams[key])
            return p




















