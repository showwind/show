#coding=utf-8
from jqwk_pom.ElePages import ClassesPage
from jqwk_pom.public import adminlogin
from selenium import webdriver
import unittest,time


class Caseupload(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.implicitly_wait(10)
		#cls.username="admin11"
		#cls.password="111111"
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
	def test_uploadclass(self):
		self.driver.get(ClassesPage.admin_url)
		adminlogin.adminlogin(self)
		upload_class=ClassesPage.Uploadinfo(self.driver,ClassesPage.user_url,u"教务管理平台")
		upload_class.click_teaching()
		upload_class.click_classes()
		print (upload_class.p_classname())
		upload_class.click_class()
		time.sleep(1)
		print (upload_class.p_classname())
		upload_class.click_detail()
		#print (upload_class.p_classtext())
		upload_class.click_classinfo()
		time.sleep(1)
		upload_class.click_button()
		time.sleep(5)

if __name__=="__main__":
	unittest.main()