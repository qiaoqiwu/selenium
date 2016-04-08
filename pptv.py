#/usr/env/bin python3
# coding = utf-8

from selenium import webdriver
import unittest
import pptv_login

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
        pptv_login.login_fail_null(self)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
