#coding=utf-8
import unittest,time
from selenium import webdriver
from jqwk_pom.ElePages import UserPage
from jqwk_pom.public import adminlogin


class CaseAddusers(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.implicitly_wait(10)
		#self.username="admin11"
		#self.password="111111"
	def test_adduser(self):
		u'''批量导入用户'''
		self.driver.get(UserPage.user_login)
		adminlogin.adminlogin(self)
		add_users=UserPage.AddUsers(self.driver,UserPage.admin_url,u"教务管理平台")
		add_users.click_usermanager()
		add_users.click_users()
		add_users.click_addusers()
		add_users.input_file("E:\\test\\jqwk_pom\\report\\a.xlsx")
		add_users.click_btn()

	def tearDown(self):
		self.driver.quit()
if __name__=="__main__":
	unittest.main()