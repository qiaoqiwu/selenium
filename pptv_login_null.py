#/usr/env/bin python3
# coding = utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

#不输入用户名密码，直接登录
def login_null(self):
    driver = self.driver
    driver.maximize_window()
    user_name = ""
    pass_word = ""
    try:
        driver.find_element_by_link_text("登录").click()
        driver.switch_to_frame("iframe")
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[5]/input").click()
        text_usr = driver.find_element_by_class_name("list-name").find_element_by_class_name("tip").text
        text_pass = driver.find_element_by_class_name("list-pass").find_element_by_class_name("tip").text

        if text_usr.strip() == '':
            print("用户名输入为空，没有提示")
        else:
            print("用户名输入为空，提示：%s" % text_usr)
        if text_pass.strip() == '':
            print("密码输入为空，没有提示")
        else:
            print("密码输入为空，提示：%s" % text_pass)
    except NoSuchElementException as e:
        print("NoSuchElementException",e)
