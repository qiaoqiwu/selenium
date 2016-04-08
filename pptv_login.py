#/usr/env/bin python3
# coding = utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

#正常登录
def login(self):
    driver = self.driver
    driver.maximize_window()
    user_name = "wqqtest001pptv"
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
        
        text = driver.find_element_by_class_name("username").text
        if text.strip() == '':
            print("登录失败")
        else:
            print("登录成功！登录账号：%s" % text)

    except NoSuchElementException as e:
        print("NoSuchElementException",e)

    #退出登录
    finally:
        above = driver.find_element_by_xpath(".//*[@id='login-area']/div[2]/dl/dd[1]")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='btn-user-logout']").click()
        
#不输入用户名密码，直接登录
def login_fail_null(self):
    driver = self.driver
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

#输入错误的用户名
def login_wrong_usr(self):
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
        
        text = driver.find_element_by_class_name("username").text
        if text.strip() == '':
            print("登录失败！登录账号：%s" % text)
        else:
            print("登录成功！登录账号：%s" % text)

    except NoSuchElementException as e:
        print("NoSuchElementException",e)

    finally:
        above = driver.find_element_by_xpath(".//*[@id='login-area']/div[2]/dl/dd[1]")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='btn-user-logout']").click()
