#coding=utf-8 
from selenium import webdriver
import unittest, time 
from jqwk_pom.public import login 
import xml.dom.minidom
import HTMLTestRunner
#打开xml文档 
dom = xml.dom.minidom.parse('E:\\test\\jqwk_pom\\report\\login.xml') 
#得到文档元素对象 
root = dom.documentElement
class TestaLogin(unittest.TestCase):
	def setUp(self): 
		self.driver = webdriver.Chrome() 
		self.driver.implicitly_wait(10) 
		logins = root.getElementsByTagName('url') 
		self.base_url=logins[0].firstChild.data 
		self.driver.maximize_window()
		self.verificationErrors = []
#用户名、密码为空 
	def test_null(self):
		u'''账号密码为空'''
		driver = self.driver 
		driver.get(self.base_url) 
		logins = root.getElementsByTagName('null') 
	#获得null标签的username、passwrod属性值 
		username=logins[0].getAttribute("username") 
		password=logins[0].getAttribute("password") 
		prompt_info = logins[0].firstChild.data 
	#登录 
		login.user_login(self,username,password) 
	#获取断言信息进行断言 
		text=driver.find_element_by_id("msgdiv").text
		self.assertEqual(text,prompt_info)
#输入用户名、密码为空
	def test_pawd_null(self): 
		u'''密码为空'''
		driver = self.driver 
		driver.get(self.base_url) 
		logins = root.getElementsByTagName('pawd_null') 
	#获得null标签的username、passwrod属性值 
		username=logins[0].getAttribute("username") 
		password=logins[0].getAttribute("password") 
		prompt_info = logins[0].firstChild.data 
	#登录 
		login.user_login(self,username,password) 
	#获取断言信息进行断言 
		text = driver.find_element_by_id("msgdiv").text 
		self.assertEqual(text,prompt_info)
#用户名为空，只输入密码 
	def test_user_null(self): 
		u'''用户为空'''
		driver = self.driver 
		driver.get(self.base_url) 
		logins = root.getElementsByTagName('user_null') 
	#获得null标签的username、passwrod属性值 
		username=logins[0].getAttribute("username")
		password=logins[0].getAttribute("password")
		prompt_info = logins[0].firstChild.data 
	#登录 
		login.user_login(self,username,password) 
	#获取断言信息进行断言
		text = driver.find_element_by_id("msgdiv").text 
		self.assertEqual(text,prompt_info)
#用户名密码错误 
	def test_error(self): 
		u'''账号密码错误'''
		driver = self.driver 
		driver.get(self.base_url) 
		logins = root.getElementsByTagName('error')
	 #获得null标签的username、passwrod属性值 
		username=logins[0].getAttribute("username") 
		password=logins[0].getAttribute("password") 
		prompt_info = logins[0].firstChild.data 
	 #登录 
		login.user_login(self,username,password) 
	 ##获取断言信息进行断言 
		text = driver.find_element_by_id("msgdiv").text 
		self.assertEqual(text,prompt_info)
	def tearDown(self):
		self.driver.quit() 
		self.assertEqual([], self.verificationErrors)
if __name__ == "__main__": 
	unittest.main()
