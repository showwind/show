#coding=utf-8
from zbpf.ElementPages import LoginPage
from zbpf.public import logger
import unittest,time
from selenium import webdriver

class LoginCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.implicitly_wait(10)
		cls.username="susiku"
		cls.password="111111"
		cls.login_url="http://zbpf.jqweike.com/#/login"

	def test_user_login(self):
		login_page=LoginPage.LoginPage(self.driver,self.login_url,u"桥帮主")
		login_page.open()
		login_page.input_username(self.username)
		login_page.input_password(self.password)
		login_page.click_submit()
		assert login_page.show_span,u"susiku"
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
if __name__=='__main__':
	unittest.main()