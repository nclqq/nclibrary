import logging
import time
import os

#指定保存日志的文件路径，日志级别，以及调用文件将日志存入到指定的文件中
class Logger:
    def __init__(self,logger):

        #创建一个logger
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler,用于传输日志文件（用于写入日志文件）
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        # log_path=os.path.dirname(os.getcwd())+'/logs/'  项目根目录下/logs保存日志
        #os.getcwd()表示
        log_path=os.path.dirname(os.path.abspath('.'))+'/logs/'
        #如果case组织结构式/testsuit/featuremodel/xxx.py,那么得到的相对路径的父路径就是项目根目录
        log_name=log_path+rq+'.log'
        fh = logging.FileHandler(log_name)  # 输出到logs文件夹下
        fh.setLevel(logging.INFO)

        #再创建一个handler，用于输出到控制台
        ch=logging.StreamHandler() #控制台输出
        ch.setLevel(logging.INFO)

        # 设置handler(日志文件)的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def getlog(self):
        return self.logger
