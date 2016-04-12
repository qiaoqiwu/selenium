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
            print("login fail!")
        else:
            print("login success!login username is : %s" % text)
    
    except NoSuchElementException as e:
        print("NoSuchElementException",e)
'''
    #退出登录
    finally:
        above = driver.find_element_by_xpath(".//*[@id='login-area']/div[2]/dl/dd[1]")
        ActionChains(driver).move_to_element(above).perform()
        driver.find_element_by_xpath(".//*[@id='btn-user-logout']").click()     
'''

