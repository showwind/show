#coding=utf-8
from zbpf.public import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage.Action):
	username_loc=(By.CSS_SELECTOR,"#app > div > div > form > div:nth-child(1) > div > div > input")
	password_loc=(By.CSS_SELECTOR,"#app > div > div > form > div:nth-child(2) > div > div > input")
	submit_loc=(By.CSS_SELECTOR,"#app > div > div > form > div:nth-child(3) > div > div > div.ivu-col.ivu-col-span-6 > button")
	span_loc=(By.CSS_SELECTOR,"#app > div > div.bg-common-header > div > div.tr.ivu-col.ivu-col-span-12 > ul > li:nth-child(2) > div > div.ivu-dropdown-rel > a > span")
	def open(self):
		self._open(self.base_url,self.pagetitle)

	def input_username(self,username):
		self.find_element(*self.username_loc).clear()
		self.find_element(*self.username_loc).send_keys(username)

	def input_password(self,password):
		self.find_element(*self.password_loc).clear()
		self.find_element(*self.password_loc).send_keys(password)

	def click_submit(self):
		self.find_element(*self.submit_loc).click()

	def show_span(self):
		return self.find_element(*self.span_loc).text
