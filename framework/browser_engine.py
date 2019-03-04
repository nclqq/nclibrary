import os
import time
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getlog()

class BrowserEngine:
    dir=os.path.dirname(os.path.abspath('.')) #获取绝对路径
    chrome_driver_path=dir+'/tools/chromedriver.exe' #得到谷歌驱动的路径
    ie_driver_path = dir + '/tools/IEDriverServer.exe'  # 得到ie驱动的路径
    firefox_driver_path = dir + '/tools/geckodriver.exe'  # 得到火狐驱动的路径


    # 在配置文件中读取浏览器类型并返回该浏览器
    def open_browser(self):
        config = ConfigParser()
        # 相对路径
        # file_path=os.path.dirname(os.getcwd())+'/config/config.ini'
        # 绝对路径
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        # config.read(file_path)  # 读取文件
        config.read(file_path, encoding='utf-8')

        # 选择浏览器
        browser = config.get("browerType", "browserName")
        logger.info("你选择了 %s 浏览器" % browser)
        # 选择要测试的url
        url = config.get("testServer", "URL")
        logger.info("测试的url是 ：%s" % url)

        # 判断
        if browser == "Firefox":
            # 启动火狐
            self.driver = webdriver.Firefox(executable_path=self.firefox_driver_path)
            logger.info("开启火狐浏览器")
        elif browser == "Chrome":
            # 启动谷歌
            self.driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("开启谷歌浏览器")
        elif browser == "IE":
            # 启动ie
            self.driver = webdriver.Ie(self.ie_driver_path)
            logger.info("开启ie浏览器")

        self.driver.get(url)  # 打开要测试的网页
        logger.info("打开：%s" % url)
        self.driver.maximize_window()
        logger.info("最大化当前窗口")
        self.driver.implicitly_wait(10)
        logger.info("设置隐式等待10秒")

        return self.driver
        time.sleep(8)


    def quit_browser(self):
        time.sleep(10)
        logger.info("关闭并退出当前窗口")
        self.driver.quit()
