import sys
sys.path.append("E:\Discuz")

import unittest
import os
import HTMLTestRunner

from testsuites.test_discuz_login import DiscuzLogin
from testsuites.test_discuz_manage import DiscuzManageCreate
from testsuites.test_discuz_search import DiscuzSearch
from testsuites.test_discuz_vote import DiscuzVote



#设置报告文件保存路径
current_path=os.path.dirname(os.path.realpath(__file__)) #获取当前路径（用例路径）
report_path=os.path.join(current_path,"report") #设置报告路径，并且路径名是report(报告存放路径)
if not os.path.exists(report_path):
    os.mkdir(report_path)

#构造测试套件
suite=unittest.TestSuite() #创建套件
suite.addTest(unittest.makeSuite(DiscuzLogin)) #增加home测试
suite.addTest(unittest.makeSuite(DiscuzManageCreate)) #增加two测试
suite.addTest(unittest.makeSuite(DiscuzSearch)) #增加three测试
suite.addTest(unittest.makeSuite(DiscuzVote)) #增加four测试

if __name__=="__main__":
    #打开一个文件，将result写入此file中
    html_report=report_path+r"\result.html" #（html报告文件路径）
    fp=open(html_report,"wb")
    #初始化一个htmltestrunner实例对象，用来生成报告
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例执行情况")
    runner.run(suite)