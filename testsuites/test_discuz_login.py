from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_login import LoginPage
import unittest
from framework.logger import Logger


logger=Logger(logger="DiscuzLogin").getlog()

class DiscuzLogin(BaseTestCase):

    # 测试登录
    def test_login_search(self):
        #声明HomePage类对象
        login_page = LoginPage(self.driver)
        #调用首页搜索功能
        name=login_page.login("admin","admin")
        logger.info("管理员登录成功")
        if "admin" in name:
            self.driver.switch_to.window(self.driver.current_window_handle)  # 激活当前页面
            # your_title = input("请输入您要发表的帖子标题：")
            # your_text = input("请输入您要发表的帖子内容：")
            login_page.send_mail("5", "8787878")
            logger.info("帖子发表成功")
            # your_replay = input("请输入您要回复的内容：")
            login_page.replay_mail("888")
            logger.info("回复帖子成功")
            login_page.logout()
            logger.info("退出成功")



if __name__=="__main__":
    unittest.main(verbosity=2)