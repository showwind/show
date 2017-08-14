#coding=utf-8
from jqwk_pom.ElePages import UserPage
from jqwk_pom.public import adminlogin
import unittest,time
from selenium import webdriver

admin_url="http://www.jqwk.com/academic.php"
user_url="http://www.jqwk.com/academic/user/users/usercontrol"
class CaseUserOption(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.implicitly_wait(10)
		#cls.username ="admin11"
		#cls.password ="111111"
	def test_usereditor(self):
		u"编辑用户"
		self.driver.get(UserPage.user_login)
		adminlogin.adminlogin(self)
		user_option=UserPage.UpdateUser(self.driver,admin_url,u"教务管理平台")
		user_option.click_usermanager()
		user_option.click_users()
		print (user_option.userinfo_p())
		user_option.input_sykey(u"周")
		user_option.click_search()
		print(user_option.userinfo_p())
		user_option.click_user()
		user_option.update_name("zhoujin")
		user_option.update_isteacher("0")
		user_option.click_submit()
		#self.assertEqual(user_option.userinfo_p(),"929814527@qq.com")
		user_option.click_active()

	def test_userupdate(self):
		u'''更改用户组'''

		update_option=UserPage.Updateup(self.driver,user_url,u"教务管理平台")
		print (update_option.userinfo_p())
		update_option.input_sykey(u"王")
		update_option.click_search()
		print (update_option.userinfo_p())
		update_option.click_user()
		update_option.click_type("8")
		update_option.click_submit()
		time.sleep(2)
		update_option.click_comfirm()
		self.assertEqual(update_option.group_p(),u"中新")

	def test_userzdelete(self):
		deluser_option=UserPage.Deleteuser(self.driver,user_url,u"教务管理平台")
		print (deluser_option.userinfo_p())
		deluser_option.input_sykey(u"真")
		deluser_option.click_search()
		print (deluser_option.userinfo_p())
		deluser_option.click_user()
		deluser_option.click_del()
	
	@classmethod	
	def tearDownClass(cls):
		cls.driver.quit()
if __name__=="__main__":
	unittest.main()
		