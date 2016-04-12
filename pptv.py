#/usr/env/bin python3
# coding = utf-8

from selenium import webdriver
import unittest
import pptv_login,pptv_login_null,pptv_login_wrong_pw,pptv_login_wrong_un
import HTMLTestRunner
import time
import send_report

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.pptv.com"
        self.accept_next_alert = True
        self.verificationErrors = []
    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)     
        pptv_login.login(self)
    def test_login_null(self):
        driver = self.driver
        driver.get(self.base_url)
        pptv_login_null.login_null(self)
    def test_login_wrong_un(self):
        driver = self.driver
        driver.get(self.base_url)
        pptv_login_wrong_un.login_wrong_un(self)
    def test_login_wrong_pw(self):
        driver = self.driver
        driver.get(self.base_url)
        pptv_login_wrong_pw.login_wrong_pw(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
    #unittest.main()
    testunit = unittest.TestSuite()

    testunit.addTest(Login("test_login"))
    testunit.addTest(Login("test_login_null"))
    testunit.addTest(Login("test_login_wrong_un"))
    testunit.addTest(Login("test_login_wrong_pw"))

    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    filename = "D:\\" + now + "-" + "result.html"
    fp = open(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = u'pptv首页自动化登录测试报告',
        description = u'用例执行情况：'
        )
    runner.run(testunit)
    fp.close()
    send_report.sendreport()
