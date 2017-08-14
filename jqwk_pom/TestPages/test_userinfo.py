#coding=utf-8
from jqwk_pom.ElePages import UserPage
from jqwk_pom.public import adminlogin
import unittest,time
from selenium import webdriver

admin_url="http://www.jqwk.com/academic.php"
class Casesearch(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.implicitly_wait(10)
		#cls.username ="admin11"
		#cls.password ="111111"
	def test_search(self):
		u'''搜索用户'''
		self.driver.get(UserPage.user_login)
		adminlogin.adminlogin(self)
		search_user=UserPage.SearchUser(self.driver,admin_url,u"教务管理平台")
		search_user.click_usermanager()
		search_user.click_users()
		print(search_user.userinfo_p())
		search_user.input_search("8",u"数学系")
		search_user.click_search()
		self.assertNotEqual(search_user.userinfo_p(),"929814527@qq.com")
	def test_srenlist(self):
		u'''分页跳转'''
		render_list=UserPage.RdList(self.driver,admin_url,u"教务管理平台")
		render_list.input_search("0",)
		render_list.click_search()
		render_list.click_renderlist(2)

	@classmethod	
	def tearDownClass(cls):
		cls.driver.quit()
if __name__=="__main__":
	unittest.main()