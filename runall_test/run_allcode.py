# coding=utf-8
# coding=utf-8
from testcase.code_testcase import CODE_test
import unittest,os,time
from utils.HTMLTestRunnerCN import HTMLTestRunner
from utils.mail import SendMail
def allcase():
    suite=unittest.TestSuite()
    suite.addTests([CODE_test("test01_code"), CODE_test("test02_code"),CODE_test('test03_code'),CODE_test("test04_code"),CODE_test("test05_code"),CODE_test("test06_code"),CODE_test("test07_code"),CODE_test("test08_code"),CODE_test("test09_code"),CODE_test("test10_code"),CODE_test("test11_code"),CODE_test("test12_code"),CODE_test("test13_code"),
                    # CODE_test("test14_code"),
                    CODE_test("test15_code"),CODE_test("test16_code"),CODE_test("test17_code"),CODE_test("test18_code"),CODE_test("test19_code"),])
    return suite
now=time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))
path=os.path.abspath(os.path.dirname(os.getcwd()))+"\\report\\"
report_path=path+'codelab-接口返回结果.html'

def run_allcase():
    fp=open(report_path,'wb')
    runner=HTMLTestRunner(stream=fp,title='CODELAB接口自动化')
    runner.run(allcase())
    fp.close()
def send_mail():
    sm=SendMail(send_msg=report_path,attachment=report_path)
    sm.send_mail()
if __name__=='__main__':
    run_allcase()
    send_mail()