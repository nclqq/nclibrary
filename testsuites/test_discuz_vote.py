from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_vote import VotePage
import unittest
from framework.logger import Logger
import time


logger=Logger(logger="DiscuzFourSearch").getlog()

class DiscuzVote(BaseTestCase):

    def test_four(self):
        vote_page = VotePage(self.driver)
        name = vote_page.login("admin", "admin")
        logger.info("管理员登录成功")
        if "admin" in name:
            self.driver.switch_to.window(self.driver.current_window_handle)  # 激活当前页面
            vote_page.fa_mail("3333","4","5","dsjnfefjkajksddhjbffkjf")
            time.sleep(15)
            vote_page.exit()




if __name__=="__main__":
    unittest.main(verbosity=2)