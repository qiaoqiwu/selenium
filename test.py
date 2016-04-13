from selenium import webdriver
import unittest
import time
import pptv_login_by_ap

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.pptv.com"
        self.accept_next_alert = True
        self.verificationErrors = []
    def test_login_wrong_pw(self):
        driver = self.driver
        driver.get(self.base_url)
        pptv_login_by_ap.login_by_ap(self)
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
