# coding=utf-8
from selenium.webdriver.common.by import By
from selenium import webdriver
from zbpf.public import BasePage
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

index_url="http://zbpf.jqweike.com/#/wrap/index"
class NewsPage(BasePage.Action):
	#添加新闻
	submenu_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.sidemenu > div:nth-child(2) > ul > li:nth-child(2) > div")
	news_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.sidemenu > div:nth-child(2) > ul > li:nth-child(2) > ul > li")
	add_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(1) > div:nth-child(1) > button.ivu-btn.ivu-btn-primary")
	title_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form > div:nth-child(1) > div > div > input")
	content_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form > div:nth-child(3) > div > div > textarea")
	button_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div.news-edit-common > div.pt20.ivu-row > div > form > div:nth-child(4) > div.ivu-form-item-content > div:nth-child(1) > div.g-core-image-corp-container> div.info-aside > p.btn-groups > button.btn.btn-upload")
	body_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form > div:nth-child(5) > div > div > div.wang-editor-main.wangEditor-txt")
	save_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form > div.tr.ivu-form-item > div > button.ivu-btn.ivu-btn-ghost")
	list_title_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(2) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(2)")
	
	#编辑新闻
	edit_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(2) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(6) > div > div > button.ivu-btn.ivu-btn-primary")
	select_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form > div:nth-child(2) > div.ivu-form-item-content > div > div.ivu-select-selection")
	select_list_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form > div:nth-child(2) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li")
	activity_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(2) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(4)")
	edit_button_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form > div.tr.ivu-form-item > div > button.ivu-btn.ivu-btn-ghost")

	#删除新闻
	remove_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(2) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(6) > div > div > button.ivu-btn.ivu-btn-error")
	confirm_loc=(By.CSS_SELECTOR,"body > div:nth-child(15) > div.ivu-modal-wrap > div > div > div > div > div.ivu-modal-confirm-footer > button.ivu-btn.ivu-btn-primary.ivu-btn-large")
	
	#预览新闻
	preview_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(2) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(6) > div > div > button.ivu-btn.ivu-btn-ghost")
	preview_title_loc=(By.CSS_SELECTOR,"body > div:nth-child(14) > div.ivu-modal-wrap > div > div > div.ivu-modal-body > div > div > div.content > h3")

	#所属活动
	selected_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(1) > div.pr5.ivu-col.ivu-col-span-8 > div > div.ivu-select-selection")
	list_selected_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(1) > div.pr5.ivu-col.ivu-col-span-8 > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li")
	#添加新闻方法
	def click_submenu(self):
		self.find_element(*self.submenu_loc).click()

	def click_news(self):
		self.find_element(*self.news_loc).click()
	def click_add(self):
		self.find_element(*self.add_loc).click()

	def input_title(self,t):
		self.find_element(*self.title_loc).send_keys(t)

	def input_content(self,c):
		self.find_element(*self.content_loc).send_keys(c)

	def input_cover(self,c):
		self.driver.execute_script('document.getElementsByTagName("form")[0].style.opacity=1;') #opacity=1把元素变为可见
		self.driver.find_element_by_name("file").send_keys(c)

	def click_button(self):
		self.find_element(*self.button_loc).click()
	
	def input_body(self,b):
		self.find_element(*self.body_loc).send_keys(Keys.TAB) #输入不成功，可以在输入之前先按个table键
		self.find_element(*self.body_loc).send_keys(b)
	def click_save(self):
		self.find_element(*self.save_loc).click()
	
	def title_text(self,t):
		return self.find_elements(self.list_title_loc)[t].text #显示新闻列表名称

	#编辑新闻方法
	def click_eidt(self,e):

		self.find_elements(self.edit_loc)[e].click() #根activity_text()保持一致

	def select_activity(self,s):
		print (len(self.find_elements(self.select_list_loc)))
		self.find_element(*self.select_loc).click()
		time.sleep(1) #可不要
		self.find_elements(self.select_list_loc)[s].click() #跟select_activity_text()保持一致

	def edit_save(self):
		self.find_element(*self.edit_button_loc).click()

	def activity_text(self,a):
		return self.find_elements(self.activity_loc)[a].text

	def select_activity_text(self,s):

		#print (self.find_elements(self.select_list_loc)[s].text)
		return self.find_elements(self.select_list_loc)[s].text

	#删除新闻
	def click_remove(self,r):
		self.find_elements(self.remove_loc)[r].click() #删除列表中某个

	def click_confirm(self):
		self.find_element(*self.confirm_loc).click()
	
	#预览新闻
	def click_preview(self,c):
		self.find_elements(self.preview_loc)[c].click()

	def preview_title_text(self):
		return self.find_element(*self.preview_title_loc).text

	#筛选活动
	def list_activity(self,a):
		self.find_element(*self.selected_loc).click()
		self.find_elements(self.list_selected_loc)[a].click()

	def list_select_activity_text(self,l):
		return self.find_elements(self.list_selected_loc)[l].text