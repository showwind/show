#coding=utf-8
from jqwk_pom.public import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By

user_url="http://www.jqwk.com/"
class StudentDiscuss(BasePage.Action):
	close_loc=(By.CSS_SELECTOR,"button.close")
	list_loc=(By.LINK_TEXT,u"讨论")
	theme_loc=(By.CSS_SELECTOR,"#themeTitle")
	submit_loc=(By.CSS_SELECTOR,"button.btn.btn-primary.askQuestions")
	comfirm_loc=(By.CSS_SELECTOR,"body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm")
	def click_close(self):
		self.find_element(*self.close_loc).click()
	def click_list(self):
		self.find_elements(self.list_loc)[1].click()

	def input_theme(self,c):
		self.find_element(*self.theme_loc).send_keys(c)

	def click_submit(self):
		self.find_element(*self.submit_loc).click()

class TeacherDiscuss(BasePage.Action):
	list_loc=(By.CSS_SELECTOR,"#tab-2 > div > div.row > div.col-lg-3 > a > img")
	discuss_loc=(By.CSS_SELECTOR,"#myTab > ul > li:nth-child(6) > a")
	theme_loc=(By.CSS_SELECTOR,"#myTextarea")
	submit_loc=(By.CSS_SELECTOR,"#chat_body > div.reply > button")

	def click_list(self):
		self.find_elements(self.list_loc)[1].click()
	def click_discuss(self):
		self.find_element(*self.discuss_loc).click()
	def input_theme(self,c):
		self.find_element(*self.theme_loc).send_keys(c)
	def click_submit(self):
		self.find_element(*self.submit_loc).click()

