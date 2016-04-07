#/usr/env/bin python3
# coding = utf-8
from selenium import webdriver
import time

def login(self):
    driver = self.driver
    driver.maximize_window()
    driver.find_element_by_link_text("登录").click()
    driver.switch_to_frame("iframe")
    driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[1]/input").clear()
    driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[1]/input").send_keys("wqqtest001pptv")
    driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[2]/input").clear()
    driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[2]/input").send_keys("bangbus")
    driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[5]/input").click()
    time.sleep(5)
