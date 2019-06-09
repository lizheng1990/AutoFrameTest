# -*- coding：UTF-8 -*-

from app.appkeyword import APP

app = APP()
# # 打开模拟器
# app.runCMD('E:\\\"Program Files (x86)\"\\MuMu\\emulator\\nemu\\EmulatorShell\\NemuPlayer.exe')
# # 强制等待60s
# app.waitMust('60')
# # adb连接模拟器
# app.runCMD('adb connect 127.0.0.1:7555')
# 打开appium命令行版
app.openAppium('7777')
# 强制等待30s
app.waitMust('30')
# 打开QQ
app.openPackage('7555','com.tencent.mobileqq','.activity.SplashActivity')
# 强制等待30s
app.waitMust('10')
# 滑动页面
app.swipScreen('300','350','300','1200','1')

# 点击汽车之家小程序
app.runCMD('adb -e shell input tap ' + '80 250')
app.waitMust('10')
print(app.driver.contexts)
app.clickByXpath("//android.view.View[@content-desc='原创']")
app.waitMust('10')
# app.switchContext('WEBVIEW_com.tencent.mobileqq:mini1')
app.clickByXpath("/html/body/wx-view/wx-view[1]/wx-view/wx-view[2]/wx-view/wx-view/wx-view[4]/wx-view/wx-view")
# app.switchContext('NATIVE_APP')
app.clickByXpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.ImageView")
app.clickByXpath("//android.widget.ImageView[@content-desc='关闭']")
app.waitMust('10')
# 关闭应用
app.colseApp()
# 关闭appium命令行版
app.runCMD('taskkill /F /IM node.exe')
# 关闭模拟器
app.runCMD('taskkill /F /IM NemuPlayer.exe')
