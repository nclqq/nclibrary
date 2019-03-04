from selenium import webdriver
from framework.browser_engine import BrowserEngine
import unittest


class BaseTestCase(unittest.TestCase):


    # setUp()主要是测试的前提准备工作
    def setUp(self):
        # self.driver =webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        self.be=BrowserEngine()
        self.driver=self.be.open_browser()


    #测试结束后的操作
    def tearDown(self):
        self.be.quit_browser()
        # self.driver.quit()
        # BrowserEngine().quit_browser()
