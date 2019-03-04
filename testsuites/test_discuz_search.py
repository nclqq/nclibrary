from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_search_mail import SearchPage
import unittest
from framework.logger import Logger
from ddt import ddt,data,unpack


logger=Logger(logger="DiscuzSearch").getlog()

@ddt
class DiscuzSearch(BaseTestCase):

    @unpack
    def test_three(self):
        search_page = SearchPage(self.driver)
        name = search_page.login("admin", "admin")
        logger.info("登录成功")
        if "admin" in name:
            self.driver.switch_to.window(self.driver.current_window_handle)  # 激活当前页面
            result=search_page.search_mail("haotest")
            try:
                self.assertEqual(result, "haotest", msg=result)
                search_page.logout()
            except Exception as e:
                print("搜索错误或查找不到")



if __name__=="__main__":
    unittest.main(verbosity=2)