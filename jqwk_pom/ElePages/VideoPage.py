#coding=utf-8
from jqwk_pom.public import BasePage
from selenium.webdriver.common.by import By
import time

user_url="http://www.jqwk.com/"
class SetVideoPage(BasePage.Action):
	list_loc=(By.CSS_SELECTOR,"#tab-2 > div > div.row > div.col-lg-3 > a > img")
	setvideo_loc=(By.CSS_SELECTOR,"#myTab > ul > li:nth-child(3) > a")
	input_loc=(By.CSS_SELECTOR,"#ttaabb > ul >li.eachSectionLi >ul > li > h5 >input.Wdate")

	def click_list(self):
		self.find_elements(self.list_loc)[0].click()
	def click_setvideo(self):
		self.find_element(*self.setvideo_loc).click()
	def input_date(self,c):
		self.find_elements(self.input_loc)[1].send_keys(c)
		time.sleep(3)
class VideoOption(BasePage.Action):
	btnclose_loc=(By.CSS_SELECTOR,"button.close")
	list_loc=(By.CSS_SELECTOR,"#course-list > div > div.col-lg-3 > a > img")
	course_loc=(By.CSS_SELECTOR,"div.item> div.course-body> ul > a:nth-child(1) > li")
	video_loc=()

	def click_close(self):
		self.find_element(*self.btnclose_loc).click()
	def click_list(self):
		t=self.find_elements(self.list_loc)
		t[0].click()
	def click_course(self):
		self.find_elements(self.course_loc)[0].click()