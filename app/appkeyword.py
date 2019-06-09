# -*- coding： UTF-8 -*-
import os
import socket
import subprocess
import time
import traceback
from os.path import dirname, abspath

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from common import config
from common.logger import logger


class APP:
    def __init__(self):
        self.driver = None
        self.caps = {}
        self.port = '4723'

    def runCMD(self,command):
        """
        命令前加"start /b "则不显示命令窗口；命令前加"cmd /c start "则显示命令窗口
        :param command:
        :return:
        """
        # os.popen('cmd /c start ' + command)
        p = subprocess.Popen('cmd /c start ' + command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()
        # os.system(command)
        logger.info('运行cmd命令：' + str('start /b ' + 'cmd /c start ' + command) + '成功')

    def openAppium(self,port='4723'):
        self.port = port
        self.caps = {}
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(('127.0.0.1', int(port)))
            s.shutdown(2)
            logger.error('port %s is uesd !' % port)
            portstatus = False
        except:
            logger.info('port %s is available!' % port)
            portstatus = True
        bootstrap_port = str(int(port) + 1)
        dir_path = dirname(dirname(abspath(__file__)))
        logPath = dir_path + "/lib/logs/AppiumLog.log";
        try:
            if portstatus:
                cmd = 'cmd /c start appium -a ' + '127.0.0.1 -p ' + str(port) + ' --bootstrap-port ' + str(bootstrap_port) + " --log " + logPath + " --log-timestamp --local-timezone"
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                logger.info('运行cmd命令：' + str('start /b ' + cmd) + '成功')
                p.wait()
        except Exception as e:
            logger.info('运行cmd命令：' + str('start /b ' + cmd) + '失败')
            logger.error(str(e))

    def openPackage(self,deviceName = "7555",appPackage = "com.android.browser",appActivity = ".BrowserActivity"):
        config.get_config('../lib/conf/conf.properties')
        self.caps = {}
        self.caps["deviceName"] = config.config['deviceName' + deviceName]
        self.caps["platformName"] = config.config['platformName' + deviceName]
        self.caps["platformVersion"] = config.config['platformVersion' + deviceName]
        self.caps["appPackage"] = appPackage
        self.caps["appActivity"] = appActivity
        self.caps["noReset"] = True
        # 下面chromeOptions的添加很重要，涉及小程序的能否定位
        if appPackage == 'com.tencent.mm':
            self.caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:appbrand0'}
        elif appPackage == 'com.tencent.mobileqq':
            self.caps['chromeOptions'] = {'androidProcess': 'com.tencent.mobileqq:mini'}
        else:
            pass
        self.driver = webdriver.Remote("http://127.0.0.1:" + self.port + "/wd/hub", self.caps)
        self.driver.implicitly_wait(30)
        logger.info('使用设备：' + config.config['deviceName' + deviceName] + '打开应用：' + appPackage + '成功')

    def visitH5(self,url,deviceName = "7555",browserName = "Browser"):
        config.get_config('../lib/conf/conf.properties')
        self.caps = {}
        self.caps["deviceName"] = config.config['deviceName' + deviceName]
        self.caps["platformName"] = config.config['platformName' + deviceName]
        self.caps["platformVersion"] = config.config['platformVersion' + deviceName]
        self.caps["browserName"] = browserName
        self.caps["noReset"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:" + self.port + "/wd/hub", self.caps)
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        if browserName == 'chrome':
            try:
                WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element_by_xpath('//*[@text="否"]')).click()
                logger.info('翻译提示已出现，且关闭')
            except:
                logger.info('翻译提示未出现')
        else:
            pass
        logger.info('获取到的当前句柄：' + str(self.driver.contexts))
        logger.info('使用浏览器：' + browserName + '打开网站：' + url + '成功')

    def switchContext(self, name):
        self.driver.switch_to.context(name)
        logger.info('切换句柄为：' + name + '成功')



    def clickById(self,eId):
        self.driver.find_element_by_id(eId).click()
        logger.info('点击元素ID为：' + eId + '成功')

    def clickByXpath(self,eXpath):
        self.driver.find_element_by_xpath(eXpath).click()
        logger.info('点击元素xpath为：' + eXpath + '成功')

    def clearTextById(self,eId):
        self.driver.find_element_by_id(eId).clear()
        logger.info('清除元素ID：' + eId + '成功')

    def clearTextByXpath(self,eXpath):
        self.driver.find_element_by_xpath(eXpath).clear()
        logger.info('清除元素xpath：' + eXpath + '成功')

    def inputTextById(self,eId,eText):
        self.driver.find_element_by_id(eId).send_keys(eText)
        logger.info('对元素ID：' + eId + '发送文本：' + eText + '成功')

    def inputTextByXpath(self,eXpath,eText):
        self.driver.find_element_by_xpath(eXpath).send_keys(eText)
        logger.info('对元素xpath：' + eXpath + '发送文本：' + eText + '成功')

    def keyEvent(self,num):
        num = int(num)
        self.driver.keyevent(num)
        logger.info('操作keyevent：' + str(num) + '成功')

    def waitMust(self,etime):
        time.sleep(int(etime))
        logger.info('强制等待：' + etime + '成功')

    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipScreen(self,sx,sy,ex,ey,eTime):
        self.driver.swipe(int(sx), int(sy), int(ex), int(ey), int(float(eTime) * 1000))

    # 长按ID
    def longPressById(self,eId,eTime):
        TouchAction(self.driver).long_press(self.driver.find_element_by_id(eId)).wait(
            int(float(eTime) * 1000)).perform()

    # 长按Xpath
    def longPressByXpath(self, eXpath, eTime):
        TouchAction(self.driver).long_press(self.driver.find_element_by_xpath(eXpath)).wait(
            int(float(eTime) * 1000)).perform()

    # 点击坐标eCoor=(615, 52), (690, 146),eTime是秒
    def tapCoor(self,eCoor,eTime):
        self.driver.tap('[' + eCoor + ']', int(float(eTime)*1000))
        logger.info("点击坐标：" + eCoor +"成功")

    # 关闭应用
    def colseApp(self):
        self.driver.close_app()

    # 切换到指定iframe
    def switchToFrame(self,eXpath):
        elc = self.driver.find_element_by_xpath(eXpath)
        self.driver.switch_to.frame(elc)
        logger.info("切换到指定frame" + eXpath +"成功")

    # 回到上一个iframe
    def switchToLastFrame(self):
        self.driver.switch_to.parent_frame()
        logger.info("回到上一个iframe成功")

    # 回到最外层iframe
    def switchToParentFrame(self):
        self.driver.switch_to.default_content()
        logger.info("回到最外层iframe成功")

    # 切换新窗口
    def switchWindowColseOld(self):
        handle = self.driver.current_window_handle
        handles = self.driver.window_handles
        for h in handles:
            if handle != h:
                new = h
                self.driver.close()
                self.driver.switch_to.window(new)
        logger.info("切换新窗口成功")

    # 关闭其他窗口
    def closeOldWindow(self):
        handle = self.driver.current_window_handle
        for temHandle in self.driver.window_handles:
            if temHandle != handle:
                self.driver.close()
                self.driver.switch_to().window(temHandle)
        logger.info("关闭其他窗口成功")

    # 调用js操作页面，如window.scrollBy(0,300)，每次向下滑动页面300像素点，window.scroll(0,3000)移动到0,3000像素点位置
    def excuteJs(self, js):
        try:
            self.driver.execute_script(js)
            logger.info("操作js：" + js + "成功")
        except Exception as e:
            logger.error(str(traceback.format_exc()))

    # 针对按索引进行切换下拉列表option属性
    def selectByIndex(self, eXpath, index):
        Select(self.driver.find_element_by_xpath(eXpath)).select_by_index(index)
        logger.info("查找：" + eXpath + "中的索引：" + index + "成功")

    # 针对按value进行切换下拉列表option属性
    def selectByValue(self, eXpath, value):
        Select(self.driver.find_element_by_xpath(eXpath)).select_by_value(value)
        logger.info("查找：" + eXpath + "中的值：" + value + "成功")

    # 针对按text文本进行切换下拉列表option属性
    def selectByText(self, eXpath, text):
        Select(self.driver.find_element_by_xpath(eXpath)).select_by_visible_text(text)
        logger.info("查找：" + eXpath + "中的文本：" + text + "成功")

    # 针对按索引进行取消下拉列表option属性
    def deselectByIndex(self, eXpath, index):
        Select(self.driver.find_element_by_xpath(eXpath)).deselect_by_index(index)
        logger.info("取消：" + eXpath + "中的索引：" + index + "成功")

    # 针对按value进行取消下拉列表option属性
    def deselectByValue(self, eXpath, value):
        Select(self.driver.find_element_by_xpath(eXpath)).deselect_by_value(value)
        logger.info("取消：" + eXpath + "中的值：" + value + "成功")

    # 针对按text文本进行取消下拉列表option属性
    def deselectByText(self, eXpath, text):
        Select(self.driver.find_element_by_xpath(eXpath)).deselect_by_visible_text(text)
        logger.info("取消：" + eXpath + "中的文本：" + text + "成功")