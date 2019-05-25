import jsonpath

j = {'a':'111', 'b':'222', 'c':'333'}
p = None
# p = '{re}'
# for key in j:
#     p = p.replace("{" + key + "}", j[key])
# print(p)

try:
    p = jsonpath.jsonpath(j, 'v')
except:
    p = None
print(p)
# try:
#     p['x'] = str(jsonpath.jsonpath(j, 'v')[0])
#     print(p)
# except Exception as e:
#     print(1111111)