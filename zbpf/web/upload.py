#coding:utf-8
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import testlogin

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
phone="18200385389"
psw="123456"
ur=testlogin.login_zbpf(phone,psw)
driver.get(ur)
try:
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#app > div > div.index > div:nth-child(2) > div > div.rows > div:nth-child(2) > div > img")).click()
	time.sleep(2)
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#myRoute > div.once-join > button")).click()
	time.sleep(1)
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#app > div > div.apply > form > div:nth-child(2) > div > div > div.ivu-select-selection > span.ivu-select-placeholder")).click()
	time.sleep(1)
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#app > div > div.apply > form > div:nth-child(2) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(1)")).click()
	time.sleep(1)
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#app > div > div.apply > form > div:nth-child(3) > div > div > input")).send_keys("ceshi")
	time.sleep(1)
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#app > div > div.apply > form > div:nth-child(4) > div.item-left.ivu-col.ivu-col-span-12 > div > div > div.input-left.ivu-input-wrapper.ivu-input-type > input")).send_keys("show")
	time.sleep(1)
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#app > div > div.apply > form > div:nth-child(4) > div:nth-child(2) > div > div > div.input-right.ivu-input-wrapper.ivu-input-type > input")).send_keys("15196615488")
	time.sleep(1)
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#app > div > div.apply > form > div:nth-child(5) > div.item-left.ivu-col.ivu-col-span-12 > div > div > div.input-left.ivu-input-wrapper.ivu-input-type > input")).send_keys("10086")
	time.sleep(1)
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#app > div > div.apply > form > div:nth-child(5) > div.item-right.ivu-col.ivu-col-span-12 > div > div > div > input")).send_keys("english")
	time.sleep(1)
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#select_btn_1")).send_keys("E:\\test\\picture.zip")
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#btn2")).click()
	time.sleep(20)
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#app > div > div.apply > form > div:nth-child(8) > div > div > label > span.ivu-checkbox > input")).click()
	time.sleep(1)
	WebDriverWait(driver,10).until(lambda x:x.find_element_by_css_selector("#app > div > div.apply > form > div:nth-child(10) > div > button > span")).click()
	time.sleep(5)
	driver.quit()
except:
	print ("fail")


