from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger

logger=Logger(logger="SearchPage").getlog()


class SearchPage(BasePage):
        #登录
        username_input_search_loc = (By.NAME, "username") #用户名
        pwd__input_search_loc = (By.NAME, "password") #密码
        login_click_button_search_loc=(By.XPATH,"//button") #登录按钮

        #判断登录
        isornot_login=(By.CSS_SELECTOR,".vwmy a")

        #搜索帖子
        srchtext_input_search_loc = (By.NAME, "srchtxt") #搜索框
        srbtn__button_search_loc = (By.ID, "scbar_btn") # 搜索按钮
        srtxt_a_search_loc=(By.CSS_SELECTOR,".xs3 a") #进入搜索的帖子
        findthetitle_search_loc=(By.CSS_SELECTOR,".ts span") #标题

        #登出
        logout_click_button_search_loc = (By.LINK_TEXT, "退出")  # 退出按钮


        def login(self,username,pwd):
            self.sendkeys(username,*self.username_input_search_loc) #输入用户名
            self.sendkeys(pwd, *self.pwd__input_search_loc) #输入密码
            self.click(*self.login_click_button_search_loc) #点击登录按钮
            logger.info("信息填写成功")
            return self.findelement(*self.isornot_login).text
            time.sleep(3)


        def search_mail(self,sr_content):
            self.sendkeys(sr_content, *self.srchtext_input_search_loc)  # 输入搜索内容
            self.get_windows_img()
            time.sleep(6)
            self.click(*self.srbtn__button_search_loc)  # 点击搜索按钮
            self.get_handlers(1) #获取新窗口
            self.get_windows_img()
            self.click(*self.srtxt_a_search_loc)  # 点击进入搜索的帖子
            self.get_handlers(2)  # 激活新窗口
            time.sleep(6)
            return self.findelement(*self.findthetitle_search_loc).text
            time.sleep(3)




        def logout(self):
            time.sleep(3)
            self.click(*self.logout_click_button_search_loc)  # 点击退出按钮
            logger.info("登出进行")
