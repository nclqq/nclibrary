from selenium import webdriver
import unittest
from ddt import ddt,data,unpack
import time
from framework.util import Utils

testdata=Utils.read_excel("E:/Discuz/data/data_excel.xlsx","Sheet1")

@ddt
class Search_by_ddt(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(10)


    @data(*testdata)
    def test_search_by_ddt(self,data):
        search_string=data["content"]
        print("搜索内容->:%s"%search_string)
        search_input=self.driver.find_element_by_id("kw")


        search_input.send_keys(search_string)
        time.sleep(4)
        search_input.submit()

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main()