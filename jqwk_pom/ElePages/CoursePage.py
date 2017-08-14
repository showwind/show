#coding=utf-8
from jqwk_pom.public import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

admin_url="http://www.jqwk.com/academic/login/index"
class EditCourse(BasePage.Action):
	teaching_loc=(By.CSS_SELECTOR,"#primary-nav > ul > li:nth-child(5) > a")
	courses_loc=(By.CSS_SELECTOR,"#primary-nav>ul>li:nth-child(5)>ul>li:nth-child(1)> a")
	course_loc=(By.CSS_SELECTOR,"#courselist > tr > td.text-center > span:nth-child(1) > img")
	period_loc=(By.ID,"period")
	credit_loc=(By.ID,"credit")
	video_loc=(By.ID,"video")
	task_loc=(By.ID,"task")
	test_loc=(By.ID,"test")
	exam_loc=(By.ID,"exam")
	over_loc=(By.ID,"over")
	upperiod_loc=(By.CSS_SELECTOR,"#courselist > tr > td:nth-child(3)")
	def click_teachding(self):
		self.find_element(*self.teaching_loc).click()
	def click_courses(self):
		self.find_element(*self.courses_loc).click()
	def click_course(self):
		self.find_elements(self.course_loc)[0].click()
	def input_period(self,c):
		self.find_element(*self.period_loc).clear()
		self.find_element(*self.period_loc).send_keys(c)
	def input_credit(self,c):
		self.find_element(*self.credit_loc).clear()
		self.find_element(*self.credit_loc).send_keys(c)
	def input_video(self,c):
		self.find_element(*self.video_loc).clear()
		self.find_element(*self.video_loc).send_keys(c)
	def input_task(self,c):
		self.find_element(*self.task_loc).clear()
		self.find_element(*self.task_loc).send_keys(c)
	def input_test(self,c):
		self.find_element(*self.test_loc).clear()
		self.find_element(*self.test_loc).send_keys(c)
	def input_exam(self,c):
		self.find_element(*self.exam_loc).clear()
		self.find_element(*self.exam_loc).send_keys(c)
	def click_over(self):
		self.find_element(*self.over_loc).click()
	def p_period(self):
		return self.find_elements(self.upperiod_loc)[0].text
class DeleteCourse(BasePage.Action):
	course_loc=(By.CSS_SELECTOR,"#courselist > tr > td.text-center > span:nth-child(2) > img")
	submit_loc=(By.CSS_SELECTOR,"body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm")
	def click_delcourse(self):
		self.find_elements(self.course_loc)[0].click()
	def click_submit(self):
		self.find_element(*self.submit_loc).click()