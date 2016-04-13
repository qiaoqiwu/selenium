#/usr/env/bin python3
# coding = utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

#第三方登录，新浪微博
def login_by_wb(self):
    u"""第三方登录，新浪微博"""
    driver = self.driver
    driver.maximize_window()
    user_name = ""
    pass_word = ""
    try:
        driver.find_element_by_link_text("登录").click()
        driver.switch_to_frame("iframe")
        nowhandle = driver.current_window_handle
        driver.find_element_by_xpath("//*[@id='loginform']/ul/li[6]/div[2]/a[3]").click()

        allhandles = driver.window_handles
        for handle in allhandles:
            if handle != nowhandle:
                driver.switch_to_window(handle)
                driver.maximize_window()
                #driver.switch_to_frame("ptlogin_iframe")

                driver.find_element_by_id("userId").clear()
                driver.find_element_by_id("userId").send_keys(user_name)
                driver.find_element_by_id("passwd").clear()
                driver.find_element_by_id("passwd").send_keys(pass_word)
                driver.find_element_by_xpath(".//*[@id='outer']/div/div[2]/form/div/div[2]/div/p/a[1]").click()
                
                time.sleep(5)
                              
        driver.switch_to_window(nowhandle)

        try:
            text = driver.find_element_by_class_name("username").text
            a = True
        except:
            a = False
            
        if a == True:
            print("登录成功!  登录用户名为 : %s" % text)
        else:
            print("登录失败!")
    
    except NoSuchElementException as e:
        print("NoSuchElementException",e)
