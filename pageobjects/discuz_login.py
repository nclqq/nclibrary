from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import random
import time
from framework.logger import Logger

logger=Logger(logger="LoginPage").getlog()

#继承BasePage类
class LoginPage(BasePage):
        #登录
        username_input_search_loc = (By.NAME, "username") #用户名
        pwd__input_search_loc = (By.NAME, "password") #密码
        login_click_button_search_loc=(By.XPATH,"//button") #登录按钮

        #判断登录
        isornot_login=(By.CSS_SELECTOR,".vwmy a")

        #发帖
        morenbankuai_btn_search_loc = (By.CSS_SELECTOR, "tr h2 a") #默认板块
        mail_title__input_search_loc = (By.NAME, "subject") # 查找帖子主题
        mail_content__input_search_loc = (By.CSS_SELECTOR,".pt") # 查找帖子内容
        mail_click_button_search_loc = (By.CSS_SELECTOR, ".ptm button") # 发表按钮

        #回复帖子
        # repaly_list_search_loc=(By.CSS_SELECTOR,"#threadlisttableid .num a") #要回复的列表

        repaly_area_area_search_loc = (By.CSS_SELECTOR, ".area>.pt")  # 回复文本框
        replay_click_button_search_loc = (By.NAME, "replysubmit")  # 回复按钮

        #登出
        logout_click_button_search_loc = (By.LINK_TEXT, "退出")  # 退出按钮

    # 输入搜索内容，并提交
        def login(self,username,pwd):
            self.sendkeys(username,*self.username_input_search_loc) #输入用户名
            self.sendkeys(pwd, *self.pwd__input_search_loc) #输入密码
            self.get_windows_img()
            self.click(*self.login_click_button_search_loc) #点击登录按钮
            logger.info("信息填写成功")
            return self.findelement(*self.isornot_login).text

        # def is_login(self,username):
        #     if self.findelement(*self.isornot_login).text in username:
        #         return True
        #     else:
        #         return False



        def send_mail(self,mail_title,mail_content):
            time.sleep(4)
            self.click(*self.morenbankuai_btn_search_loc)  # 点击默认板块
            self.sendkeys(mail_title, *self.mail_title__input_search_loc)  # 输入帖子主题
            time.sleep(3)
            self.sendkeys(mail_content, *self.mail_content__input_search_loc)  # 输入帖子正文
            time.sleep(3)
            self.get_windows_img()
            self.click(*self.mail_click_button_search_loc)  # 点击发帖按钮
            logger.info("帖子信息填写成功")
            time.sleep(3)

        def replay_mail(self,replay_area):
            # BasePage(self.driver).back()
            self.current_window()  # 激活当前页面

            # replaylist=list(self.findelement(*self.repaly_list_search_loc))
            # pre_replay = random.choice(replaylist)  # 随机回复
            # self.click(pre_replay)  # 点击要回复的那一个

            # self.click(*self.repaly_list_search_loc)
            time.sleep(3)
            self.sendkeys(replay_area, *self.repaly_area_area_search_loc)  # 输入回复的内容
            time.sleep(3)
            self.get_windows_img()
            self.click(*self.replay_click_button_search_loc)  # 点击发帖按钮
            logger.info("回复帖子信息填写成功")
            time.sleep(3)

        def logout(self):
            time.sleep(3)
            self.click(*self.logout_click_button_search_loc)  # 点击退出按钮
            self.get_windows_img()
            logger.info("登出进行")


