#coding=utf-8
import unittest,time
from selenium import webdriver
from jqwk_pom.ElePages import UserPage
from jqwk_pom.public import adminlogin

admin_url="http://www.jqwk.com/academic.php"
class CaseAdduser(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.implicitly_wait(10)
		#self.username="admin11"
		#self.password="111111"
	def test_adduser(self):
		u'''添加用户'''
		self.driver.get(UserPage.user_login)
		adminlogin.adminlogin(self)
		add_user=UserPage.AddUser(self.driver,UserPage.admin_url,u"教务管理平台")
		add_user.click_usermanager()
		add_user.click_users()
		add_user.click_adduserbtn()
		add_user.input_username("showwind")
		add_user.select_groupid("8")
		add_user.select_isteacher("0")
		add_user.input_psw("111111")
		add_user.input_nickname(u"周三")
		add_user.input_realname(u"周三")
		add_user.input_email("12345678@qq.com")
		add_user.input_stuid("9214567")
		add_user.click_btn()

	def tearDown(self):
		self.driver.quit()
if __name__=="__main__":
	unittest.main()