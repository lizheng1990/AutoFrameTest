# coding:utf8
import jsonpath,json
import requests

from inter.httpkeyword import HTTP

# mail_info={}
# att1={}
# mail_info['filenames'] = ['result-HTTP接口用例20190519210314.xls']
# att1['Content-Disposition'] = 'attachment; filename= "' + mail_info['filenames'][0] + '"'
# print(att1)

# s = '{"store":{"book": [{"category": "reference","author": "Nigel Rees","title": "Sayings of the Century","price": 8.95},{"category": "fiction","author": "Evelyn Waugh","title": "Sword of Honour","price": 12.99},{"category": "fiction","author": "Herman Melville","title": "Moby Dick","isbn": "0-553-21311-3","price": 8.99},{"category": "fiction","author": "J. R. R. Tolkien","title": "The Lord of the Rings","isbn": "0-395-19395-8","price": 22.99}],"bicycle": {"color": "red","price": 19.95}},"expensive": 10}'
# s = '{"a":"1","b":"2","c":"3"}'
# s = json.loads(s)
# a = jsonpath.jsonpath(s,'c')
# print(a)
