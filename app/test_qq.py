# -*- coding：UTF-8 -*-

from app.appkeyword import APP

app = APP()
# 打开模拟器
# app.runCMD('E:\\\"Program Files (x86)\"\\MuMu\\emulator\\nemu\\EmulatorShell\\NemuPlayer.exe')
# # 强制等待30s
# app.waitMust('30')
# # adb连接模拟器
# app.runCMD('adb connect 127.0.0.1:7555')
# 打开appium命令行版
app.openAppium('7777')
# 强制等待20s
app.waitMust('20')
# 打开QQ
app.openPackage('7555','com.tencent.mobileqq','.activity.SplashActivity')
# 强制等待30s
app.waitMust('30')
# 清除用户名
app.clearTextByXpath("//android.widget.EditText[@content-desc='请输入QQ号码或手机或邮箱']")
# 输入用户名
app.inputTextByXpath("//android.widget.EditText[@content-desc='请输入QQ号码或手机或邮箱']",'304594568')
# 清除密码
app.clearTextByXpath("//android.widget.EditText[@content-desc='密码 安全']")
# 输入密码
app.inputTextByXpath("//android.widget.EditText[@content-desc='密码 安全']",'Liz48225248')
# 点击登录
app.clickByXpath("//android.widget.ImageView[@content-desc='登 录']")
# 点击头像
app.clickByXpath("//android.widget.Button[@content-desc='帐户及设置']")
# 点击设置
app.clickByXpath("//android.widget.Button[@content-desc='设置']/android.widget.TextView")
# 点击账号管理
app.clickByXpath("//android.widget.TextView[@content-desc='帐号管理']")
# 点击退出当前账号
app.clickByXpath("//android.widget.TextView[@content-desc='退出当前帐号']")
# 点击确认退出
app.clickByXpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[2]")
app.colseApp()
# 关闭appium命令行版
app.runCMD('taskkill /F /IM node.exe')
# 关闭模拟器
app.runCMD('taskkill /F /IM NemuPlayer.exe')
