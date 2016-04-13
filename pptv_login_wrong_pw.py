#/usr/env/bin python3
# coding = utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

#输入错误的用户名
def login_wrong_pw(self):
    u"""输入错误的用户名"""
    driver = self.driver
    driver.maximize_window()
    user_name = "wqqtest001pptv"
    pass_word = "bangbus1234"
    try:
        driver.find_element_by_link_text("登录").click()
        driver.switch_to_frame("iframe")
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[1]/input").clear()
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[1]/input").send_keys(user_name)
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[2]/input").clear()
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[2]/input").send_keys(pass_word)
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[5]/input").click()
        time.sleep(5)

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
