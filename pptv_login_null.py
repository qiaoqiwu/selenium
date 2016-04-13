#/usr/env/bin python3
# coding = utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

#不输入用户名密码，直接登录
def login_null(self):
    u"""输入空用户名密码"""
    driver = self.driver
    driver.maximize_window()
    user_name = ""
    pass_word = ""
    try:
        driver.find_element_by_link_text("登录").click()
        driver.switch_to_frame("iframe")
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[5]/input").click()

        #text_usr = driver.find_element_by_class_name("list-name").find_element_by_class_name("tip").text
        #text_pass = driver.find_element_by_class_name("list-pass").find_element_by_class_name("tip").text

        try:
            text_usr = driver.find_element_by_class_name("list-name").find_element_by_class_name("tip").text
            a = True
        except:
            a = False
            
        if a == True:
            print("用户名输入错误，提示：%s" % text_usr)
        else:
            print("用户名输入错误，没有提示!")

        try:
            text_pass = driver.find_element_by_class_name("list-pass").find_element_by_class_name("tip").text
            b = True
        except:
            b = False
            
        if b == True:
            print("密码输入错误，提示：%s" % text_pass)
        else:
            print("密码输入错误，没有提示!")

    except NoSuchElementException as e:
        print("NoSuchElementException",e)
