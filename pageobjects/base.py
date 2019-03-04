from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import os
import time


#创建一个logger实例
logger=Logger(logger="BasePage").getlog()

class BasePage(object):

    def __init__(self,driver):
        self.driver=driver

    #后退
    def back(self):
        self.driver.back()
        logger.info("点击后退按钮")

    #前进
    def forward(self):
        self.driver.forward()
        logger.info("点击前进按钮.")


    # 浏览器启驱动中有了open_browser和quit_browser()这里可以省略也可以存在，
    # 浏览器驱动中的方法在setup中调用，调用之后就不在调用，若之后在basetest中
    # 还想调用open_browser的话，可以调用这里的

    # 打开url站点
    def open_url(self,url):
        self.driver.get(url)

    #关闭并停止浏览器服务
    def quit_browser(self):
        self.driver.quit()

    def get_frame(self,j):
        self.driver.switch_to.frame(j)

    # def into_frame(self,*loc):
    #     self.driver.switch_to.frame(*loc)

    #获取当前窗口
    def current_window(self):
        current_window=self.driver.current_window_handle
        self.driver.switch_to.window(current_window)

    #获取句柄
    def get_handlers(self,i):
        # main_window=self.driver.current_window_handle
        # self.driver.switch_to.window(main_window)
        self.driver.switch_to.window(self.driver.window_handles[i])

    #点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭当前窗口")
        except Exception as e:
            logger.error("关闭窗口失败因为 %s"%e)

    #查找元素
    #一个*表示会把一个参数形成一个元组，两个**则会把接收到的参数存入一个字典
    #下面的loc表示元组中的一个值
    def findelement(self,*loc):
        try:
            #next_page=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR , ".page_no:last-of-type")))
            # element = element.find_element(By.ID, ‘foo’)
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到元素 %s"%loc)
        except:
            logger.error("%s 不能找到 %s 元素"%(self,loc))

    #保存图片
    def get_windows_img(self):

        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("获取截图并保存到 /screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.error("获取截图失败因为 %s"%e)

    #输入
    def sendkeys(self,text,*loc):
        el=self.findelement(*loc) #调用本类中的方法
        el.clear()
        try:
            el.send_keys(text)
            logger.info("文本框中写入：%s"%text)
        except Exception as e:
            logger.error("文本框写入失败因为 %s"%e)
            self.get_windows_img()

    #清除文本框
    def clear(self,*loc):
        el=self.findelement(*loc) #调用本类中的方法
        try:
            el.clear()
            logger.info("在写入之前清空文本框")
        except Exception as e:
            logger.error("清空文本框失败因为 %s" % e)
            self.get_windows_img()

    #点击元素
    def click(self,*loc):
        el=self.findelement(*loc) #调用本类中的方法
        try:
            el.click()
        except Exception as e:
            print(e)


