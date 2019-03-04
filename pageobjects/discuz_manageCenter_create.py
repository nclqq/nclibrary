from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
from framework.logger import Logger
from pageobjects.discuz_login import LoginPage

logger=Logger(logger="CreatManagePage").getlog()

#继承BasePage类
class CreatManagePage(BasePage):
        #登录
        username_input_search_loc = (By.NAME, "username") #用户名
        pwd__input_search_loc = (By.NAME, "password") #密码
        login_click_button_search_loc=(By.XPATH,"//button") #登录按钮

        #判断登录
        isornot_login=(By.CSS_SELECTOR,".vwmy a")

        #删帖
        morenbankuai_btn_search_loc = (By.CSS_SELECTOR, "tr h2 a") #默认板块
        del__input_search_loc = (By.CSS_SELECTOR, ".o input") # 查找对勾
        delmail__link_search_loc = (By.LINK_TEXT,"删除") # 查找删除
        suredel_click_button_search_loc = (By.CSS_SELECTOR, ".pns #modsubmit") # 确定删除按钮

        #创建新版块
        mokuaiManage_link_search_loc=(By.LINK_TEXT,"管理中心") #管理中心，点击后要查找句柄，激活当前窗口
        pwdSecond_input_search_loc=(By.NAME,"admin_password") #输入密码
        submit_click_button_search_loc = (By.NAME, "submit")  # 提交按钮

        # 判断登录
        manage_isornot_login = (By.CLASS_NAME, "uinfo")

        luntan_click_li_search_loc = (By.LINK_TEXT, "论坛")  # 查找论坛的那一列
        addnewbankuai_link_search_loc = (By.CSS_SELECTOR, ".lastboard>a")  # 查找添加新版块
        addnewbankuai_name_link_search_loc = (By.NAME, "newforum[1][]")  # 查找添加新版块名称
        # addnewbankuai_jicheng_select_search_loc = (By.NAME, "newinherited[1][]")  # 查找添加继承指定板块
        newbankuai_submit_click_search_loc = (By.CSS_SELECTOR, ".fixsel .btn")  # 提交按钮

        luntan_out_click_search_loc = (By.LINK_TEXT, "退出")  # 查找退出按钮

        putongsendMail_a=(By.CSS_SELECTOR,"#category_1 tr:nth-last-child(2) h2 a")  #普通用户登陆后的新版块
        mail_title__input_search_loc = (By.NAME, "subject")  # 查找帖子主题
        mail_content__input_search_loc = (By.CSS_SELECTOR, ".pt")  # 查找帖子内容
        mail_click_button_search_loc = (By.CSS_SELECTOR, ".ptm button")  # 发表按钮

        # 登出
        logout_click_button_search_loc = (By.LINK_TEXT, "退出")  # 退出按钮


        # 输入搜索内容，并提交
        #登录
        def login(self,username,pwd):
            self.sendkeys(username,*self.username_input_search_loc) #输入用户名
            self.sendkeys(pwd, *self.pwd__input_search_loc) #输入密码
            self.click(*self.login_click_button_search_loc) #点击登录按钮
            logger.info("信息填写成功")
            time.sleep(4)
            return self.findelement(*self.isornot_login).text


        # 删除帖子
        def del_mail(self):
            time.sleep(4)
            self.current_window()
            self.click(*self.morenbankuai_btn_search_loc)  # 点击默认板块
            self.current_window()
            self.click(*self.del__input_search_loc)  # 选择要删除的
            self.current_window()
            self.get_windows_img()
            time.sleep(6)
            self.click(*self.delmail__link_search_loc)  # 点击删除链接
            self.get_windows_img()
            time.sleep(6)
            self.click(*self.suredel_click_button_search_loc)  # 点击确定删除按钮
            logger.info("删除帖子成功")
            time.sleep(6)

        #创建新版块
        def create_newbankuai(self,pwdTwo,newbankuaiName):
            main_window=self.driver.current_window_handle
            self.driver.switch_to.window(main_window)
            self.click(*self.mokuaiManage_link_search_loc)  # 点击管理中心
            self.get_windows_img()
            time.sleep(5)
            self.get_handlers(1)
            self.sendkeys(pwdTwo, *self.pwdSecond_input_search_loc)  # 输入密码
            self.get_windows_img()
            self.click(*self.submit_click_button_search_loc)  # 点击提交
            time.sleep(3)
            if "admin" in self.findelement(*self.manage_isornot_login).text:
                logger.info("登录管理中心成功")
                self.click(*self.luntan_click_li_search_loc)  # 点击论坛
                self.get_windows_img()
                time.sleep(3)
                self.get_frame(0)
                self.click(*self.addnewbankuai_link_search_loc)  # 点击添加新版块
                self.get_windows_img()
                time.sleep(3)
                self.clear(*self.addnewbankuai_name_link_search_loc) #清空内容
                self.sendkeys(newbankuaiName, *self.addnewbankuai_name_link_search_loc)  # 输入新版块名称
                self.get_windows_img()
                time.sleep(3)
                self.click(*self.newbankuai_submit_click_search_loc)  # 点击提交
                logger.info("添加新版块成功")
                time.sleep(6)
                self.current_window()
                self.click(*self.luntan_out_click_search_loc) #退出管理中心
                self.get_windows_img()
                self.current_window()
                self.exit()
                time.sleep(6)

        def sendmail(self,title,content):
            self.click(*self.putongsendMail_a)
            self.sendkeys(title, *self.mail_title__input_search_loc)  # 输入帖子主题
            time.sleep(3)
            self.sendkeys(content, *self.mail_content__input_search_loc)  # 输入帖子正文
            time.sleep(3)
            self.get_windows_img()
            self.click(*self.mail_click_button_search_loc)  # 点击发帖按钮
            logger.info("帖子信息填写成功")
            time.sleep(3)

        def re_mail(self,driver,replay_text):
            self.home=LoginPage(driver)
            self.home.replay_mail(replay_text)

        def exit(self):
            self.click(*self.logout_click_button_search_loc)  # #退出用户




