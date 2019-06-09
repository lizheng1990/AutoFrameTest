# coding:utf8
from inspect import getfullargspec

from inter.httpkeyword import HTTP

testType = HTTP()
func = getattr(testType,'seturl')
# func("http://www.baidu.com")
args = getfullargspec(func).__str__()
print(args)
print(args.find('args='))
args = args[args.find('args=') + 5:args.find(', varargs')]
print(args)
print(type(args))
args = eval(args)
print(args)
print(type(args))
args.remove('self')
print(args)
l = len(args)
print(l)
