import json,jsonpath

from suds.client import Client
from suds.xsd.doctor import ImportDoctor,Import

# imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
# imp.filter.add('http://WebXml.com.cn/')
# doctor = ImportDoctor(imp)
# client = Client('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl', doctor=doctor)
#
# res = client.service.getWeatherbyCityName('重庆')
# print(res)

# imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
# imp.filter.add('http://soap.testingedu.com/')
# doctor = ImportDoctor(imp)
# print(imp.filter)
# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl')
#
# res = client.service.auth()
# print(res)
# res = json.loads(res)
# print(str(jsonpath.jsonpath(res,'token')[0]))
# client = Client('http://112.74.191.10:8081/inter/SOAP?wsdl', headers={'token':str(jsonpath.jsonpath(res,'token')[0])})
# res = client.service.__getattr__('auth')()
# print(res)
# res = client.service.__getattr__('login')('Will','123456')
# print(res)
# res = client.service.logout()
# print(res)

# from inter.soapkeyword import SOAP

# soap = SOAP()
# soap.adddoctor()
# soap.setwsdl('http://112.74.191.10:8081/inter/SOAP?wsdl')
#
# soap.callmethod('auth')
# soap.assertequals('status','200')
#
# soap.addheader('token')
# soap.callmethod('auth')
# soap.assertequals('status','200')
#
# soap.addheader('token','adsfklajfkalfkalfaklsdjfkadsljfklasdfjaldsfjklasdfjkdsajfklds')
# soap.callmethod('auth')
# soap.assertequals('status','200')
# soap.savejson('token','t')
#
# soap.addheader('token','5c4e6acab39e4072814e2af85bb300aa')
# soap.callmethod('auth')
# soap.assertequals('status','200')
#
# soap.addheader('token','{t}')
# soap.callmethod('auth')
# soap.assertequals('status', '201')

from inter.soapkeyword import SOAP

soap = SOAP()
soap.adddoctor('http://www.w3.org/2001/XMLSchema.xsd','http://WebXml.com.cn/')
soap.setwsdl('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl')
soap.callmethod('getWeatherbyCityName','重庆市')

# imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
# imp.filter.add('http://WebXml.com.cn/')
# doctor = ImportDoctor(imp)
# client = Client('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl', doctor=doctor)
#
# res = client.service.getWeatherbyCityName('重庆市')
# print(res)