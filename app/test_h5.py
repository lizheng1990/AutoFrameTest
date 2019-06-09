# -*- coding：UTF-8 -*-

from app.appkeyword import APP

app = APP()
# 打开模拟器
app.runCMD('E:\\\"Program Files (x86)\"\\MuMu\\emulator\\nemu\\EmulatorShell\\NemuPlayer.exe')
# 强制等待30s
app.waitMust('60')
# adb连接模拟器
app.runCMD('adb connect 127.0.0.1:7555')
# 打开appium命令行版
app.openAppium('7777')
# 强制等待20s
app.waitMust('20')
# 打开浏览器
app.visitH5('https://mkt.51job.com/tg/lp_pz/index.php','7555','Browser')
app.waitMust('30')
# 切换为NATIVE_APP
app.switchContext("NATIVE_APP")
# 关闭弹出框
app.clickByXpath("//android.webkit.WebView[@content-desc='前程无忧']/android.view.View[23]")
# 切换为CHROMIUM
app.switchContext("CHROMIUM")
# 搜索：软件测试
app.inputTextByXpath("//*[@id='search']",'软件测试')
# 点击搜索按钮
app.clickByXpath("//*[@id='submit_but']")
# 选择一级选项：所有职能
app.clickByXpath("//*[@id='funtypename']",)
# 选择二级选项：点击计算机软件
app.clickByXpath("//*[@id='rollAss']/div[1]/div[1]/div/div[1]/div/div/ul/li[3]/label")
# 选择三级选项：计算机软件
app.clickByXpath("//*[@id='rollAss']/div[1]/div[2]/div/div[1]/div/div/ul/li[1]")
# 点击确定按钮
app.clickByXpath("//*[@id='rollAss']/div[2]/span[4]")
# 点击申请职位
app.clickByXpath("//*[@id='pageContent']/div[5]/span[3]")
# 点击弹出框的确定按钮
app.clickByXpath("/html/body/div[3]/div/div[2]/span")
# 切换为NATIVE_APP
app.switchContext("NATIVE_APP")
# 点击顶部logo回首页
app.clickByXpath("//android.view.View[@content-desc='前程无忧']")
# 取消记住偏好设置复选框
app.clickById("com.android.browser:id/remember")
# 点击拒绝按钮
app.clickById("com.android.browser:id/dont_share_button")
app.waitMust('10')
# 关闭应用
app.colseApp()
# 关闭appium命令行版
app.runCMD('taskkill /F /IM node.exe')
# 关闭模拟器
app.runCMD('taskkill /F /IM NemuPlayer.exe')
