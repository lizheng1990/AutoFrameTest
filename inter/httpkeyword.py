# coding:utf8

import requests,json

class HTTP():
    def __init__(self):
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

# 设置基本url
    def seturl(self,url):
        self.url = url

# 清除header中的参数
    def removeheader(self,key):
        try:
            self.session.headers.pop(key)
        except Exception as e:
            print("header中没有" + key)

# 增加header中的参数
    def addheader(self,key,p=None):
        value = self.__get_value(p)
        self.session.headers[key] = value

# post封装
    def post(self,path,p=None):
        self.result = self.session.post(self.url+"/"+path,self.__get_params(p))
        self.jsonre = json.loads(self.result.text)

    # get封装
    def get(self,path,p=None):
        path = path + "?" + p
        self.result = self.session.get(self.url+"/"+path)
        self.jsonre = json.loads(self.result.text)

    def __to_json(self,re):
        return re[re.find("(")+1:re.find(")")]

# 设置参数格式为dict
    def __get_params(self,p):
        self.params.clear()
        if p is None:
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
        if str(self.jsonre[key]) == value:
            print("PASS")
        else:
            print("FAIL")

# 保存值到jsonparams中
    def savejson(self,key,value):
        self.jsonparams[value] = self.jsonre[key]

# 获取保存的参数值
    def __get_value(self,p=None):
        if p is None:
            return p
        else:
            for key in self.jsonparams.keys():
                p = p.replace("{" + key + "}", self.jsonparams[key])
            return p




















