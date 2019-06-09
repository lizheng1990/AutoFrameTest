# -*- coding： UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time,os,traceback

from selenium.webdriver.support.wait import WebDriverWait

from common import config
from common.logger import logger


class WEB:
    def __init__(self):
        self.driver = None

# 打开指定浏览器
    def openBrowser(self, browsertype = 'chrome'):
        if browsertype == 'chrome':
            op = Options()
            # 去掉浏览器中的提示信息
            op.add_argument("--disable-infobars")
            # 使用用户缓存文件：默认自动获取目录，错误则使用指定目录
            # try:
            #     userdir = os.environ['USERPROFILE']
            # except Exception as e:
            #     userdir = '--user-data-dir=C:\\\\Users\\\\leez\\\\AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data'
            # print(userdir)
            config.get_config('./lib/conf/conf.properties')
            userdir = config.config['chrome_user']
            op.add_argument(r'--user-data-dir=' + userdir)
            # 最大化浏览器
            op.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(executable_path='../lib/driver/chromedriver', options=op)
        elif browsertype == 'firefox':
            self.driver = webdriver.Firefox(executable_path='../lib/driver/geckodriver')
            self.driver.maximize_window()
        elif browsertype == 'ie':
            self.driver = webdriver.Ie(executable_path='../lib/driver/IEDriverServer')
            self.driver.maximize_window()
        else:
            op = Options()
            # 去掉浏览器中的提示信息
            op.add_argument("--disable-infobars")
            # 使用用户缓存文件：默认自动获取目录，错误则使用指定目录
            # try:
            #     userdir = os.environ['USERPROFILE']
            # except Exception as e:
            #     userdir = '--user-data-dir=C:\\\\Users\\\\leez\\\\AppData\\\\Local\\\\Google\\\\Chrome\\\\User Data'
            config.get_config('./lib/conf/conf.properties')
            userdir = config.config['chrome_user']
            op.add_argument(r'--user-data-dir=' + userdir)
            # 最大化浏览器
            op.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(executable_path='../lib/driver/chromedriver', options=op)
        self.driver.implicitly_wait(30)
        logger.info("打开浏览器" + browsertype + "成功")
        return self.driver

    # 打开指定url
    def openUrl(self, url):
        self.driver.get(url)
        logger.info("打开指定url：" + url + "成功")

    # 使用指定浏览器打开指定url
    def chooseBrowserOpenUrl(self, url, browsertype = 'chrome'):
        if browsertype == 'chrome':
            op = Options()
            # 去掉浏览器中的提示信息
            op.add_argument("--disable-infobars")
            # 使用用户缓存文件：默认自动获取目录，错误则使用指定目录
            # try:
            #     userdir = os.environ['USERPROFILE']
            # except Exception as e:
            #     userdir = '--user-data-dir=C:/Users/leez/AppData/Local/Google/Chrome/User Data/'
            config.get_config('./lib/conf/conf.properties')
            userdir = config.config['chrome_user']
            op.add_argument(r'--user-data-dir=' + userdir)
            # 最大化浏览器
            op.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(executable_path='../lib/driver/chromedriver', options=op)
        elif browsertype == 'firefox':
            self.driver = webdriver.Firefox(executable_path='../lib/driver/geckodriver')
            self.driver.maximize_window()
        elif browsertype == 'ie':
            self.driver = webdriver.Ie(executable_path='../lib/driver/IEDriverServer')
            self.driver.maximize_window()
        else:
            op = Options()
            # 去掉浏览器中的提示信息
            op.add_argument("--disable-infobars")
            # 使用用户缓存文件：默认自动获取目录，错误则使用指定目录
            # try:
            #     userdir = os.environ['USERPROFILE']
            # except Exception as e:
            #     userdir = '--user-data-dir=C:\\Users\\leez\\AppData\\Local\\Google\\Chrome\\User Data'
            config.get_config('./lib/conf/conf.properties')
            userdir = config.config['chrome_user']
            op.add_argument(r'--user-data-dir=' + userdir)
            # 最大化浏览器
            op.add_argument('--start-maximized')
            self.driver = webdriver.Chrome(executable_path='../lib/driver/chromedriver', options=op)
            self.driver.get(url)
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        # self.driver.execute_script(js)
        logger.info("使用浏览器：" + browsertype + "打开指定url：" + url + "成功")
        return self.driver

# 强制等待
    def waitMust(self,setTimes):
        time.sleep(int(setTimes))
        logger.info("强制等待：" + str(setTimes) + "s成功")

# 隐式等待
    def waitImplicit(self,setTimes):
        self.driver.implicitly_wait(int(setTimes))

# 显示等待
    def waitForXpath(self,setTimes,eXpath):
        # wait = WebDriverWait(self.driver, int(setTimes))
        # wait.until(EC.visibility_of_element_located((By.XPATH, eXpath)))
        WebDriverWait(self.driver, setTimes, 1).until(EC.presence_of_all_elements_located((By.XPATH,eXpath)))
        logger.info("隐式等待：" + str(setTimes) + "s成功")

# 点击元素
    def clickElement(self,eXpath):
        self.driver.find_element_by_xpath(eXpath).click()
        logger.info("点击元素：" + eXpath + "成功")

# 清除指定元素文本框文本
    def clearText(self,eXpath):
        self.driver.find_element_by_xpath(eXpath).clear()
        logger.info("清除元素：" + eXpath + "中的内容成功")

# 对指定元素文本框输入文本
    def inputText(self, eXpath, eText):
        # self.driver.find_element_by_xpath(eXpath).clear()
        self.driver.find_element_by_xpath(eXpath).send_keys(eText)
        logger.info("对指定元素：" + eXpath + "输入内容：" + eText + "成功")

    # 切换到指定iframe
    def switchToFrame(self,eXpath):
        elc = self.driver.find_element(By.XPATH, eXpath)
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

    # 鼠标悬停
    def mouseHover(self,eXpath):
        hover_element = self.driver.find_element_by_xpath(eXpath)
        #   对该元素执行悬停操作
        ActionChains(self.driver).move_to_element(hover_element).perform()
        logger.info("鼠标悬停" + eXpath + "成功")

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

    # 对alert提示框进行确认
    def alertYes(self):
        alert = self.driver.switch_to_alert()
        alert.accept()
        logger.info("对alert提示框进行确认成功")

    # 调用js操作页面，如window.scrollBy(0,300)，每次向下滑动页面300像素点，window.scroll(0,3000)移动到0,3000像素点位置
    def excuteJs(self,js):
        try:
            self.driver.execute_script(js)
            logger.info("操作js：" + js + "成功")
        except Exception as e:
            logger.error(str(traceback.format_exc()))

    # 针对按索引进行切换下拉列表option属性
    def selectByIndex(self,eXpath,index):
        Select(self.driver.find_element_by_xpath(eXpath)).select_by_index(index)
        logger.info("查找：" + eXpath + "中的索引：" + index + "成功")

    # 针对按value进行切换下拉列表option属性
    def selectByValue(self,eXpath,value):
        Select(self.driver.find_element_by_xpath(eXpath)).select_by_value(value)
        logger.info("查找：" + eXpath + "中的值：" + value + "成功")

    # 针对按text文本进行切换下拉列表option属性
    def selectByText(self,eXpath,text):
        Select(self.driver.find_element_by_xpath(eXpath)).select_by_visible_text (text)
        logger.info("查找：" + eXpath + "中的文本：" + text + "成功")

    # 针对按索引进行取消下拉列表option属性
    def deselectByIndex(self,eXpath,index):
        Select(self.driver.find_element_by_xpath(eXpath)).deselect_by_index(index)
        logger.info("取消：" + eXpath + "中的索引：" + index + "成功")

    # 针对按value进行取消下拉列表option属性
    def deselectByValue(self,eXpath,value):
        Select(self.driver.find_element_by_xpath(eXpath)).deselect_by_value(value)
        logger.info("取消：" + eXpath + "中的值：" + value + "成功")

    # 针对按text文本进行取消下拉列表option属性
    def deselectByText(self,eXpath,text):
        Select(self.driver.find_element_by_xpath(eXpath)).deselect_by_visible_text (text)
        logger.info("取消：" + eXpath + "中的文本：" + text + "成功")





# 关闭当前页面
    def closePage(self):
        self.driver.close()
        logger.info("关闭当前页面成功")

# 关闭浏览器
    def closeBrowsers(self):
        self.driver.quit()
        logger.info("关闭浏览器成功")

