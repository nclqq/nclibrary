from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger


logger=Logger(logger="VotePage").getlog()

#继承BasePage类
class VotePage(BasePage):
        #登录
        username_input_search_loc = (By.NAME, "username") #用户名
        pwd__input_search_loc = (By.NAME, "password") #密码
        login_click_button_search_loc=(By.XPATH,"//button") #登录按钮

        #判断登录
        isornot_login=(By.CSS_SELECTOR,".vwmy a")

        #发起投票
        morenbankuai_btn_search_loc = (By.CSS_SELECTOR, "tr h2 a") #默认板块

        fatie_img_search_loc = (By.ID, "newspecial") # 发帖按钮
        vote_link_search_loc = (By.LINK_TEXT, "发起投票")  # 发起投票

        votitle_input_search_loc=(By.ID,"subject") #发起投票的标题
        voFirst_input_search_loc=(By.CSS_SELECTOR,".mbm p:nth-child(1) input") #第一个
        voSecond_input_search_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(2) input")  # 第二个
        # voThird_input_search_loc = (By.CSS_SELECTOR, ".mbm p:nth-child(3) input")  # 第三个
        voText=(By.TAG_NAME, "body") #查找iframe中的元素
        send_vote_btn=(By.CSS_SELECTOR,".mbm button") #发起投票按钮

        vote_one_btn=(By.CSS_SELECTOR,".pcht tr:nth-child(1) .pslt") #第一个投票按钮
        # vote_two_btn = (By.CSS_SELECTOR, ".pcht tr:nth-child(3) .pslt")  # 第二个投票按钮
        vote_submit_btn = (By.CSS_SELECTOR, ".pcht tr:nth-child(5) button")  # 提交投票按钮

        #投票各个选项的名称和比例
        vote_first_name=(By.CSS_SELECTOR,".pcht tr:nth-child(1) .pvt label") #第一个名字
        vote_first_percent = (By.CSS_SELECTOR, ".pcht tr:nth-child(2) td:last-of-type")  # 第一个比例
        vote_second_name = (By.CSS_SELECTOR, ".pcht tr:nth-child(3) .pvt label")  # 第二个名字
        vote_second_percent = (By.CSS_SELECTOR, ".pcht tr:nth-child(4) td:last-of-type")  # 第二个比例
        vote_title = (By.CSS_SELECTOR, ".ts span")  #投票主题

        # 登出
        logout_click_button_search_loc = (By.LINK_TEXT, "退出")  # 退出按钮


        #登录
        def login(self,username,pwd):
            self.sendkeys(username,*self.username_input_search_loc) #输入用户名
            self.sendkeys(pwd, *self.pwd__input_search_loc) #输入密码
            self.click(*self.login_click_button_search_loc) #点击登录按钮
            logger.info("信息填写成功")
            time.sleep(4)
            return self.findelement(*self.isornot_login).text


        # 发表投票
        def fa_mail(self,title,First_Content,Second_Content,vote_text):
            self.click(*self.morenbankuai_btn_search_loc)  # 点击默认板块
            self.click(*self.fatie_img_search_loc)  # 点击发帖
            self.get_windows_img()
            self.current_window() #激活当前
            self.click(*self.vote_link_search_loc) #点击发起投票
            self.get_windows_img()
            time.sleep(3)

            self.sendkeys(title, *self.votitle_input_search_loc)  # 输入标题
            self.sendkeys(First_Content, *self.voFirst_input_search_loc)  # 输入第一个
            self.sendkeys(Second_Content, *self.voSecond_input_search_loc)  # 输入第二个
            time.sleep(3)
            self.get_frame(0) #进入iframe
            self.sendkeys(vote_text,*self.voText) #输入内容
            time.sleep(3)
            self.current_window()
            self.get_windows_img()
            self.click(*self.send_vote_btn) #点击发表投票按钮

            self.current_window()
            self.click(*self.vote_one_btn)  # 点击进行投票
            self.get_windows_img()
            time.sleep(3)
            self.click(*self.vote_submit_btn)  # 点击提交投票

            self.current_window()
            self.get_windows_img()

            logger.info("第一个选项的名称：%s"%self.findelement(*self.vote_first_name).text)
            logger.info("第一个选项的比例：%s"%self.findelement(*self.vote_first_percent).text)
            logger.info("第二个选项的名称：%s"%self.findelement(*self.vote_second_name).text)
            logger.info("第二个选项的比例：%s"%self.findelement(*self.vote_second_percent).text)
            logger.info("投票的主题：%s"%self.findelement(*self.vote_title).text)

            time.sleep(10)


        def exit(self):
            self.click(*self.logout_click_button_search_loc)  # #退出用户




