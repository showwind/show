#coding=utf-8
from jqwk_pom.public import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

user_url="http://www.jqwk.com/"
class StudentAnswer(BasePage.Action):
	close_loc=(By.CSS_SELECTOR,"button.close")
	list_loc=(By.LINK_TEXT,u"答疑")
	textarea_loc=(By.CSS_SELECTOR,"textarea.textarea")
	submit_loc=(By.CSS_SELECTOR,"button.btn.btn-success.askQuestions")
	comfirm_loc=(By.CSS_SELECTOR,"body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm")
	def click_close(self):
		self.find_element(*self.close_loc).click()
	def click_list(self):
		self.find_elements(self.list_loc)[1].click()

	def input_textarea(self,c):
		self.find_element(*self.textarea_loc).send_keys(c)

	def click_submit(self):
		self.find_element(*self.submit_loc).click()

class TeacherAnswer(BasePage.Action):
	list_loc=(By.CSS_SELECTOR,"#tab-2 > div > div.row > div.col-lg-3 > a > img")
	answer_loc=(By.CSS_SELECTOR,"#myTab > ul > li:nth-child(5) > a")
	count_loc=(By.CSS_SELECTOR,"#innerDiv > div.col-md-3 > div > div > span")
	textarea_loc=(By.CSS_SELECTOR,"#myTextarea")
	submit_loc=(By.CSS_SELECTOR,"#chat_body > div.reply > button")

	def click_list(self):
		self.find_elements(self.list_loc)[1].click()
	def click_answer(self):
		self.find_element(*self.answer_loc).click()
	def click_count(self):
		self.find_elements(self.count_loc)[0].click()
	def input_textarea(self,c):
		self.find_element(*self.textarea_loc).send_keys(c)
	def click_submit(self):
		self.find_element(*self.submit_loc).click()

