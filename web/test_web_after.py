# -*- coding： UTF-8 -*-

# 调用关键字类
import time

from web.webkeyword import WebKeyWord

web = WebKeyWord()
# 打开浏览器
web.openBrowser('chrome')
# 进入商城首页
web.openUrl('http://112.74.191.10:8000/Admin/Admin/login')
# 输入用户名
web.inputText("//input[@name='username']", "admin")
# 输入密码
web.inputText("//*[@name='password']", "123456")
# 输入验证码
web.inputText("//*[@id='vertify']", "1")
# 点击登录按钮
web.clickElement("//input[@name='submit']")
# 点击商城按钮
web.clickElement("//li[@data-param='shop']/a")
# 进入iframe
web.switchToFrame("//iframe[@id='workspace']")
# 点击添加商品
web.clickElement("/html/body/div[3]/div[3]/div[3]/div[1]/div[1]/a/div")
# 输入商品名
web.inputText("//*[@id='addEditGoodsForm']/div[1]/dl[1]/dd/input","leez测试商品")
# 选择商品分类1
web.selectByIndex("//select[@id='cat_id']",'3')
web.waitMust(1)
# 选择商品分类2
web.selectByValue("//select[@id='cat_id_2']",'36')
web.waitMust(1)
# 选择商品分类3
web.selectByText("//select[@id='cat_id_3']",'支架')
web.waitMust(1)
# 填写商品售价
web.inputText("//*[@id='addEditGoodsForm']/div[1]/dl[9]/dd/input",'200.00')
# 填写市场售价
web.inputText("//*[@id='addEditGoodsForm']/div[1]/dl[10]/dd/input",'99.99')
# 点击弹出商品图片上传
web.clickElement("//*[@id='addEditGoodsForm']/div[1]/dl[13]/dd/div/span[2]/input[3]")
web.waitMust(2)
# 切换进照片上传iframe
web.switchToFrame("//iframe[starts-with(@id,'layui-layer-iframe')]")
web.waitMust(2)
# 选择照片
web.inputText("//*[@id='filePicker']/div[2]/input","G:\\testing\\test.jpg")
web.waitMust(2)
# 确定使用
web.clickElement("//*[@id='uploader']/div[1]/div[3]/div[3]")
web.waitMust(2)
# 选择包邮
web.switchToLastFrame()
web.clickElement("//*[@id='is_free_shipping_label_1']")
# 确认提交
web.clickElement("//*[@id='submit']")
# 关闭浏览器
web.closeBrowsers()