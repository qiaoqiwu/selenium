# coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.pptv.com")
browser.maximize_window()

browser.find_element_by_link_text("登录").click()
time.sleep(3)

browser.switch_to_frame("iframe")

browser.find_element_by_xpath("//*[@id='loginform']/ul/li[1]/input").clear()
browser.find_element_by_xpath("//*[@id='loginform']/ul/li[1]/input").send_keys("wqqtest001pptv")
browser.find_element_by_xpath("//*[@id='loginform']/ul/li[2]/input").clear()
browser.find_element_by_xpath("//*[@id='loginform']/ul/li[2]/input").send_keys("bangbus")
browser.find_element_by_xpath("//*[@id='loginform']/ul/li[5]/input").click()
#browser.find_element_by_xpath("//*[@id='loginform']/ul/li[5]/input").submit()

time.sleep(5)
browser.quit()
