#coding=utf-8
from jqwk_pom.ElePages import HoWorkPage
from jqwk_pom.public import login
from selenium import webdriver
import unittest,time

class Casehome(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.implicitly_wait(10)
		self.username="luhong"
		self.password="111111"
	def test_home(self):
		self.driver.get(HoWorkPage.user_url)
		login.user_login(self,self.username,self.password)
		shome_page=HoWorkPage.SHomePage(self.driver,HoWorkPage.user_url,u"金桥微课 - Index")	
		shome_page.click_message()
		shome_page.click_course()
		shome_page.click_work()
		shome_page.click_home()
		self.driver.find_element_by_id("exampleInputFile").send_keys("E:\\test\\1.png")
		#shome_page.send_inputfile("E:\\test\\1.png")
		shome_page.click_submit()
		shome_page.click_comfirm()
		time.sleep(2)
		assert shome_page.assert_cherk(),u"待批改"

	def tearDown(self):
		self.driver.quit()
if __name__=="__main__":
	unittest.main()

