#/usr/env/bin python3
# coding = utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

#输入错误的用户名
def login_wrong_un(self):
    driver = self.driver
    driver.maximize_window()
    user_name = "wqqtest001pptv1234"
    pass_word = "bangbus"
    try:
        driver.find_element_by_link_text("登录").click()
        driver.switch_to_frame("iframe")
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[1]/input").clear()
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[1]/input").send_keys(user_name)
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[2]/input").clear()
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[2]/input").send_keys(pass_word)
        driver.find_element_by_xpath(".//*[@id='loginform']/ul/li[5]/input").click()
        time.sleep(5)
        '''
        text = driver.find_element_by_class_name("username").text
        if text.strip() == '':
            print("登录失败！登录账号：%s" % text)
        else:
            print("登录成功！登录账号：%s" % text)
    
        text_usr = driver.find_element_by_class_name("list-name").find_element_by_class_name("tip").text
        
        if text_usr.strip() == '':
            print("用户名输入错误，没有提示")
        elif:
            print("用户名输入错误，提示：%s" % text_usr)
'''
        text_pass = driver.find_element_by_class_name("list-pass").find_element_by_class_name("tip").text
        if text_pass.strip() == '':
            print("账号输入错误，没有提示")
        else:
            print("账号输入错误，提示：%s" % text_pass)

    except NoSuchElementException as e:
        print("NoSuchElementException",e)
