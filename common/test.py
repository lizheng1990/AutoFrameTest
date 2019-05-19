# coding:utf8

mail_info={}
att1={}
mail_info['filenames'] = ['result-HTTP接口用例20190519210314.xls']
att1['Content-Disposition'] = 'attachment; filename= "' + mail_info['filenames'][0] + '"'
print(att1)