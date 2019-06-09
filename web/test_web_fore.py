# -*- coding： UTF-8 -*-

# 调用关键字类
import time

from web.webkeyword import WebKeyWord

web = WebKeyWord()
# 打开浏览器
web.openBrowser('chrome')
# 进入商城首页
web.openUrl('http://112.74.191.10:8000/')
# 点击进入登录页面
web.clickElement("//a[contains(text(), '登录')]")
# 输入用户名
web.inputText("//*[@id='username']", "453600806@qq.com")
# 输入密码
web.inputText("//*[@id='password']", "123456")
# 输入验证码
web.inputText("//*[@id='verify_code']", "1")
# 点击登录按钮
web.clickElement("//a[@name='sbtbutton']")
# 点击进入首页
web.clickElement("//a[contains(text(), '首页')]")
# 鼠标悬停电脑配件
web.mouseHover("//a[@title='电脑']")
# 点击笔记本
web.clickElement("//a[text()='笔记本']")
# 切换到新窗口
web.switchWindowColseOld()
# 对第一个商品数量进行增加一次
web.clickElement("/html/body/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[5]/div[1]/p/a[1]")
# 对第一个商品进行添加
web.clickElement("/html/body/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[5]/div[2]/a")
# 对弹出的alert进行确认
web.waitMust(5)
web.alertYes()
# 添加购物车
web.clickElement("//a[@id='join_cart']")
# 切换iframe
web.switchToFrame("//iframe[@id='layui-layer-iframe1']")
# 点击去购物车结算
web.clickElement("//*[@id='addCartBox']/div[1]/div/div/a[2]")
# 增加商品数量
web.clickElement("//a[starts-with(@id,'decrement_')]")
# 减少商品数量
web.clickElement("//a[starts-with(@id,'increment_')]")
# 设置商品数量
web.inputText("//input[starts-with(@id,'changeQuantity_')]",'2')
web.waitMust(5)
# 去结算
web.clickElement("//a[contains(text(),'去结算')]")
# 提交订单
web.waitMust(2)
web.clickElement("//button[contains(text(),'提交订单')]")
# 选择货到付款
web.clickElement("//input[@value='pay_code=cod']")
# 确认支付方式
web.clickElement("//*[@id='cart4_form']/div/div/div/a")
# 查看订单
web.clickElement("/html/body/div[1]/div/ul/li[1]/a")
# 点击退出
web.clickElement("//a[contains(text(), '退出')]")
# 切换到新窗口
web.switchWindowColseOld()
# 关闭浏览器
web.closeBrowsers()