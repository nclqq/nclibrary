from testsuites.base_testcase import BaseTestCase
from pageobjects.discuz_manageCenter_create import CreatManagePage
import unittest
from framework.logger import Logger


logger=Logger(logger="DiscuzManageCreate").getlog()

class DiscuzManageCreate(BaseTestCase):

    def test_two(self):
        manage_page = CreatManagePage(self.driver)
        name = manage_page.login("admin", "admin")
        # print(name)
        logger.info("管理员登录成功")
        if "admin" in name:
            self.driver.switch_to.window(self.driver.current_window_handle)  # 激活当前页面
            manage_page.del_mail()
            logger.info("删除帖子成功")
            # your_admin = input("请输入您的密码：")
            # your_newbankuiaName = input("请输入新版块名称：")
            manage_page.create_newbankuai("admin","your")
            logger.info("添加新版块成功")

            nameTwo = manage_page.login("ncc", "nccncc")
            logger.info("普通用户登录成功")
            if "ncc" in nameTwo:
                self.driver.switch_to.window(self.driver.current_window_handle)  # 激活当前页面
                # your_title = input("请输入您要发表的帖子标题：")
                # your_text = input("请输入您要发表的帖子内容：")
                manage_page.sendmail("177","555vgdfghjjknjgyuh")
                logger.info("帖子发表成功")
                # your_replay = input("请输入您要回复的内容：")
                manage_page.re_mail(self.driver,"your_replay")
                logger.info("回复帖子成功")
                manage_page.exit()
                logger.info("退出成功")





if __name__=="__main__":
    unittest.main(verbosity=2)