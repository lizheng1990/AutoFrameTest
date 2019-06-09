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
    def __init__(self,w):
        self.driver = None
        self.caps = {}
        self.port = '4723'
        self.writer = w

    def runCMD(self,command):
        """
        命令前加"start /b "则不显示命令窗口；命令前加"cmd /c start "则显示命令窗口
        :param command:
        :return:
        """
        # os.popen('cmd /c start ' + command)
        try:
            p = subprocess.Popen('cmd /c start ' + command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            p.wait()
            # os.system(command)
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            logger.info('运行cmd命令：' + str('start /b ' + 'cmd /c start ' + command) + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def openAppium(self,port='4723'):
        try:
            self.port = port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect(('127.0.0.1', int(port)))
                s.shutdown(2)
                logger.error('port %s is uesd !' % port)
                self.writer.write(self.writer.row,self.writer.clo,"PASS")
                portstatus = False
            except Exception as e:
                self.writer.write(self.writer.row,self.writer.clo,"FAIL")
                self.writer.write(self.writer.row,self.writer.clo+1,str(e))
                logger.info('port %s is available!' % port)
                portstatus = True
            bootstrap_port = str(int(port) + 1)
            dir_path = dirname(dirname(abspath(__file__)))
            logPath = dir_path + "./lib/logs/AppiumLog.log";
            try:
                if portstatus:
                    cmd = 'cmd /c start appium -a ' + '127.0.0.1 -p ' + str(port) + ' --bootstrap-port ' + str(bootstrap_port) + " --log " + logPath + " --log-timestamp --local-timezone"
                    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    logger.info('运行cmd命令：' + str('start /b ' + cmd) + '成功')
                    p.wait()
                    self.writer.write(self.writer.row,self.writer.clo,"PASS")
            except Exception as e:
                self.writer.write(self.writer.row, self.writer.clo, "FAIL")
                self.writer.write(self.writer.row, self.writer.clo + 1, str(e))
                logger.info('运行cmd命令：' + str('start /b ' + cmd) + '失败')
                logger.error(str(e))
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def openPackage(self,deviceName = "7555",appPackage = "com.android.browser",appActivity = ".BrowserActivity"):
        try:
            config.get_config('./lib/conf/conf.properties')
            self.caps = {}
            self.caps["deviceName"] = config.config['deviceName' + deviceName]
            self.caps["platformName"] = config.config['platformName' + deviceName]
            self.caps["platformVersion"] = config.config['platformVersion' + deviceName]
            self.caps["appPackage"] = appPackage
            self.caps["appActivity"] = appActivity
            self.caps["noReset"] = True
            if appPackage == 'com.tencent.mm':
                self.caps['chromeOptions'] = "{'androidProcess': 'com.tencent.mm:appbrand0'}"
            else:
                pass
            self.driver = webdriver.Remote("http://127.0.0.1:" + self.port + "/wd/hub", self.caps)
            self.driver.implicitly_wait(30)
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            logger.info('使用设备：' + config.config['deviceName' + deviceName] + '打开应用：' + appPackage + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def visitH5(self,url,deviceName = "7555",browserName = "Browser"):
        try:
            config.get_config('./lib/conf/conf.properties')
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
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('获取到的当前句柄：' + str(self.driver.contexts))
            logger.info('使用浏览器：' + browserName + '打开网站：' + url + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def switchContext(self, name):
        try:
            self.driver.switch_to.context(name)
            self.writer.write(self.writer.row,self.writer.clo,"PASS")
            logger.info('切换句柄为：' + name + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)


    def clickById(self,eId):
        try:
            self.driver.find_element_by_id(eId).click()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('点击元素ID为：' + eId + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def clickByXpath(self,eXpath):
        try:
            self.driver.find_element_by_xpath(eXpath).click()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('点击元素xpath为：' + eXpath + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def clearTextById(self,eId):
        try:
            self.driver.find_element_by_id(eId).clear()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('清除元素ID：' + eId + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def clearTextByXpath(self,eXpath):
        try:
            self.driver.find_element_by_xpath(eXpath).clear()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('清除元素xpath：' + eXpath + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def inputTextById(self,eId,eText):
        try:
            self.driver.find_element_by_id(eId).send_keys(eText)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('对元素ID：' + eId + '发送文本：' + eText + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def inputTextByXpath(self,eXpath,eText):
        try:
            self.driver.find_element_by_xpath(eXpath).send_keys(eText)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('对元素xpath：' + eXpath + '发送文本：' + eText + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def keyEvent(self,num):
        try:
            num = int(num)
            self.driver.keyevent(num)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('操作keyevent：' + str(num) + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def waitMust(self,etime):
        try:
            time.sleep(int(etime))
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('强制等待：' + etime + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def swipeUp(self, t=500, n=1):
        try:
            '''向上滑动屏幕'''
            l = self.driver.get_window_size()
            x1 = l['width'] * 0.5  # x坐标
            y1 = l['height'] * 0.75  # 起始y坐标
            y2 = l['height'] * 0.25  # 终点y坐标
            for i in range(n):
                self.driver.swipe(x1, y1, x1, y2, t)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('从' + str(x1) + ',' + str(y1) + '滑动到' + str(x1) + ',' + str(y2) + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def swipeDown(self, t=500, n=1):
        try:
            '''向下滑动屏幕'''
            l = self.driver.get_window_size()
            x1 = l['width'] * 0.5  # x坐标
            y1 = l['height'] * 0.25  # 起始y坐标
            y2 = l['height'] * 0.75  # 终点y坐标
            for i in range(n):
                self.driver.swipe(x1, y1, x1, y2, t)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('从' + str(x1) + ',' + str(y1) + '滑动到' + str(x1) + ',' + str(y2) + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def swipLeft(self, t=500, n=1):
        try:
            '''向左滑动屏幕'''
            l = self.driver.get_window_size()
            x1 = l['width'] * 0.75
            y1 = l['height'] * 0.5
            x2 = l['width'] * 0.25
            for i in range(n):
                self.driver.swipe(x1, y1, x2, y1, t)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('从' + str(x1) + ',' + str(y1) + '滑动到' + str(x2) + ',' + str(y1) + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def swipRight(self, t=500, n=1):
        try:
            '''向右滑动屏幕'''
            l = self.driver.get_window_size()
            x1 = l['width'] * 0.25
            y1 = l['height'] * 0.5
            x2 = l['width'] * 0.75
            for i in range(n):
                self.driver.swipe(x1, y1, x2, y1, t)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('从' + str(x1) + ',' + str(y1) + '滑动到' + str(x2) + ',' + str(y1) + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    def swipScreen(self,sx,sy,ex,ey,eTime):
        try:
            self.driver.swipe(int(sx), int(sy), int(ex), int(ey), int(float(eTime) * 1000))
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('从' + str(sx) + ',' + str(sy) + '滑动到' + str(ex) + ',' + str(ey) + '成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 长按ID
    def longPressById(self,eId,eTime):
        try:
            TouchAction(self.driver).long_press(self.driver.find_element_by_id(eId)).wait(
                int(float(eTime) * 1000)).perform()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('长按ID:' + eId + eTime + 's成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 长按Xpath
    def longPressByXpath(self, eXpath, eTime):
        try:
            TouchAction(self.driver).long_press(self.driver.find_element_by_xpath(eXpath)).wait(
                int(float(eTime) * 1000)).perform()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('长按Xpath:' + eXpath + eTime + 's成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 点击坐标eCoor=(615, 52), (690, 146),eTime是秒
    def tapCoor(self,eCoor,eTime):
        try:
            self.driver.tap('[' + eCoor + ']', int(float(eTime)*1000))
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("点击坐标：" + eCoor +"成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)


    # 关闭应用
    def colseApp(self):
        try:
            self.driver.close_app()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info('关闭app成功')
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 切换到指定iframe
    def switchToFrame(self,eXpath):
        try:
            elc = self.driver.find_element_by_xpath(eXpath)
            self.driver.switch_to.frame(elc)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("切换到指定frame" + eXpath +"成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 回到上一个iframe
    def switchToLastFrame(self):
        try:
            self.driver.switch_to.parent_frame()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("回到上一个iframe成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 回到最外层iframe
    def switchToParentFrame(self):
        try:
            self.driver.switch_to.default_content()
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("回到最外层iframe成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 切换新窗口
    def switchWindowColseOld(self):
        try:
            handle = self.driver.current_window_handle
            handles = self.driver.window_handles
            for h in handles:
                if handle != h:
                    new = h
                    self.driver.close()
                    self.driver.switch_to.window(new)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("切换新窗口成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 关闭其他窗口
    def closeOldWindow(self):
        try:
            handle = self.driver.current_window_handle
            for temHandle in self.driver.window_handles:
                if temHandle != handle:
                    self.driver.close()
                    self.driver.switch_to().window(temHandle)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("关闭其他窗口成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 调用js操作页面，如window.scrollBy(0,300)，每次向下滑动页面300像素点，window.scroll(0,3000)移动到0,3000像素点位置
    def excuteJs(self, js):
        try:
            self.driver.execute_script(js)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("操作js：" + js + "成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.error(str(traceback.format_exc()))

    # 针对按索引进行切换下拉列表option属性
    def selectByIndex(self, eXpath, index):
        try:
            Select(self.driver.find_element_by_xpath(eXpath)).select_by_index(index)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("查找：" + eXpath + "中的索引：" + index + "成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 针对按value进行切换下拉列表option属性
    def selectByValue(self, eXpath, value):
        try:
            Select(self.driver.find_element_by_xpath(eXpath)).select_by_value(value)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("查找：" + eXpath + "中的值：" + value + "成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 针对按text文本进行切换下拉列表option属性
    def selectByText(self, eXpath, text):
        try:
            Select(self.driver.find_element_by_xpath(eXpath)).select_by_visible_text(text)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("查找：" + eXpath + "中的文本：" + text + "成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 针对按索引进行取消下拉列表option属性
    def deselectByIndex(self, eXpath, index):
        try:
            Select(self.driver.find_element_by_xpath(eXpath)).deselect_by_index(index)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("取消：" + eXpath + "中的索引：" + index + "成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 针对按value进行取消下拉列表option属性
    def deselectByValue(self, eXpath, value):
        try:
            Select(self.driver.find_element_by_xpath(eXpath)).deselect_by_value(value)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("取消：" + eXpath + "中的值：" + value + "成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)

    # 针对按text文本进行取消下拉列表option属性
    def deselectByText(self, eXpath, text):
        try:
            Select(self.driver.find_element_by_xpath(eXpath)).deselect_by_visible_text(text)
            self.writer.write(self.writer.row, self.writer.clo, "PASS")
            logger.info("取消：" + eXpath + "中的文本：" + text + "成功")
        except Exception as e:
            self.writer.write(self.writer.row,self.writer.clo,"FAIL")
            self.writer.write(self.writer.row,self.writer.clo+1,str(e))
            logger.exception(e)