#/usr/env/bin python3
# coding = utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

#第三方登录，QQ
def login_by_qq(self):
    u"""第三方登录，QQ"""
    driver = self.driver
    driver.maximize_window()
    user_name = ""
    pass_word = ""
    try:
        driver.find_element_by_link_text("登录").click()
        driver.switch_to_frame("iframe")
        nowhandle = driver.current_window_handle
        driver.find_element_by_xpath("//*[@id='loginform']/ul/li[6]/div[2]/a[1]").click()

        allhandles = driver.window_handles
        for handle in allhandles:
            if handle != nowhandle:
                driver.switch_to_window(handle)
                driver.maximize_window()
                driver.switch_to_frame("ptlogin_iframe")

                try:
                    driver.find_element_by_class_name("//*[@id='combine_page']/div[1]/div/div[4]/a")
                    a = True
                except:
                    a = False
                if a == True:
                    driver.find_element_by_class_name("//*[@id='combine_page']/div[1]/div/div[4]/a").click()
                    alert = driver.switch_to_alert()
                    alert.accept()
                    time.sleep(5)

                    driver.find_element_by_id("switcher_plogin").click()
                    driver.find_element_by_id("u").clear()
                    driver.find_element_by_id("u").send_keys(user_name)
                    driver.find_element_by_id("p").clear()
                    driver.find_element_by_id("p").send_keys(pass_word)
                    driver.find_element_by_id("login_button").click()
                    time.sleep(5)
                    #driver.close()
                else:
                    driver.find_element_by_id("switcher_plogin").click()
                    driver.find_element_by_id("u").clear()
                    driver.find_element_by_id("u").send_keys(user_name)
                    driver.find_element_by_id("p").clear()
                    driver.find_element_by_id("p").send_keys(pass_word)
                    driver.find_element_by_id("login_button").click()
                    time.sleep(5)
                    #driver.close()
                              
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
