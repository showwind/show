#coding=utf-8
from selenium import webdriver
from zbpf.public import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


class MyActivity(BasePage.Action):
	u'''筛选活动类型'''
	submenu_activity_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.sidemenu > div:nth-child(2) > ul > li:nth-child(3) > div")
	list_activity_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.sidemenu > div:nth-child(2) > ul > li:nth-child(3) > ul > li")
	select_type_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(2) > div:nth-child(2) > div > div.ivu-select-selection")
	select_type_list_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(2) > div:nth-child(2) > div > div.ivu-select-dropdown > ul:nth-child(2) > li")
	select_type_text_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(3) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(1)")

	def click_submenu(self):
		self.find_element(*self.submenu_activity_loc).click()

	def click_list_activity(self):
		self.find_element(*self.list_activity_loc).click()

	def select_type(self):
		self.find_element(*select_type_loc).click()
		self.find_elements(self.select_type_list_loc)[1].click() #选择活动类型

	def select_type_text(self):
		return self.find_elements(self.select_type_text_loc).text

	u'''查看活动详情'''
	info_submit_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(3) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(6) > div > div > button.ivu-btn.ivu-btn-ghost")
	list_name_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(3) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(2) > div > span")
	info_name_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form > div:nth-child(4) > label")

	def click_info_submit(self):
		self.find_element(*self.info_name_loc).click()

	def info_name_text(self):
		return self.find_element(*self.info_name_loc).text

	u'''创建活动'''

	add_submit_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(2) > div:nth-child(1) > button")
	select_org_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(1) > div.ivu-form-item-content > div:nth-child(1) > div.ivu-input-group-prepend > div > div.ivu-select-selection")
	list_org_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div.ivu-input-group-prepend > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li")
	acivity_name_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(2) > div > div.ivu-input-wrapper.ivu-input-type > input")
	banner_button_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(3) > div > div.g-core-image-upload-btn.banner-upload-btn > div > div.info-aside > p:nth-child(2) > button.btn.btn-upload")
	cover_button_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(4) > div > div.g-core-image-upload-btn.banner-upload-btn > div > div.info-aside > p:nth-child(2) > button.btn.btn-upload")
	info_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(5) > div > div > textarea")
	small_button_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(6) > div > div.g-core-image-upload-btn.banner-upload-btn > div > div.info-aside > p:nth-child(2) > button.btn.btn-upload")
	category_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-main > div:nth-child(1) > div > div > div.ivu-row > div.ivu-col.ivu-col-span-4 > div > div > div > input")
	prizename_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-main > div:nth-child(1) > div > div > div.ivu-row > div.ivu-col.ivu-col-span-7 > div > div > div > input")
	prizeinfo_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-main > div:nth-child(1) > div > div > div.ivu-row > div.ivu-col.ivu-col-span-10 > div > input")
	num_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-main > div:nth-child(1) > div > div > div.ivu-row > div.pr.ivu-col.ivu-col-span-3 > div > input")
	tab2_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-header > span:nth-child(2)")
	categorya_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-main > div:nth-child(2) > div > div:nth-child(2) > div.ivu-col.ivu-col-span-4 > div > div.ivu-select-selection")
	list_category_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-main > div:nth-child(2) > div > div:nth-child(2) > div.ivu-col.ivu-col-span-4 > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li")
	starttime_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-main > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div > div.ivu-date-picker-rel > div > input")
	endtime_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-main > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(3) > div > div.ivu-date-picker-rel > div > input")
	reviewtime_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-main > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(4) > div > div.ivu-date-picker-rel > div > input")
	prizetime_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-main > div:nth-child(2) > div > div:nth-child(2) > div.pr.ivu-col.ivu-col-span-5 > div > div.ivu-date-picker-rel > div > input")
	tab3_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-header > span:nth-child(3)")
	activity_info_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(7) > div > div > div.tabs-main > div:nth-child(3) > div > div > div.ivu-input-wrapper.ivu-input-type > textarea")
	activity_starttime_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(8) > div > div > div:nth-child(1) > div > div > div.ivu-date-picker > div.ivu-date-picker-rel > div > input")
	activity_endtime_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(8) > div > div > div:nth-child(3) > div > div > div.ivu-date-picker > div.ivu-date-picker-rel > div > input")
	save_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > div > button.ivu-btn.ivu-btn-primary")
	list_text_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(3) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(2) > div > span")

	def click_add(self):
		self.find_element(*self.add_submit_loc).click()

	def select_org(self,s):
		self.find_element(*self.select_org_loc).click()
		self.find_elements(self.list_org_loc)[s].click()

	def input_name(self,n):
		self.find_element(*self.acivity_name_loc).send_keys(n)
		
	def input_banner(self,b):
		self.driver.execute_script('document.getElementsByTagName("form")[1].style.opacity=1;') #opacity=1把元素变为可见
		self.driver.find_elements_by_name("file")[0].send_keys(b)
		self.find_element(*self.banner_button_loc).click()

	def input_cover(self,c):
		self.driver.execute_script('document.getElementsByTagName("form")[2].style.opacity=1;') #opacity=1把元素变为可见
		self.driver.find_elements_by_name("file")[1].send_keys(c)
		self.find_element(*self.cover_button_loc).click()

	def input_info(self,i):
		self.find_element(*self.info_loc).send_keys(i)
	
	def input_small(self,s):
		self.driver.execute_script('document.getElementsByTagName("form")[3].style.opacity=1;') #opacity=1把元素变为可见
		self.driver.find_elements_by_name("file")[2].send_keys(s)
		self.find_element(*self.small_button_loc).click()

	def input_category(self,c):
		self.find_element(*self.category_loc).send_keys(c)

	def input_prizename(self,p):
		self.find_element(*self.prizename_loc).send_keys(p)

	def input_prizeinfo(self,p):
		self.find_element(*self.prizeinfo_loc).send_keys(p)

	def input_num(self,n):
		self.find_element(*self.num_loc).send_keys(n)

	def click_tab2(self):
		self.find_element(*self.tab2_loc).click()

	def click_category(self,c):
		self.find_element(*self.categorya_loc).click()
		self.find_elements(self.list_category_loc)[c].click()

	def input_starttime(self,s1):
		self.driver.execute_script('document.getElementsByClassName("ivu-input")[7].removeAttribute("readonly");')
		self.find_element(*self.starttime_loc).send_keys(Keys.TAB)
		self.find_element(*self.starttime_loc).send_keys(s1)
	
	def input_endtime(self,s2):
		self.driver.execute_script('document.getElementsByClassName("ivu-input")[8].removeAttribute("readonly");')
		self.find_element(*self.endtime_loc).send_keys(Keys.TAB)
		self.find_element(*self.endtime_loc).send_keys(s2) 
	
	def input_reviewtime(self,s3):
		self.driver.execute_script('document.getElementsByClassName("ivu-input")[9].removeAttribute("readonly");')
		self.find_element(*self.reviewtime_loc).send_keys(Keys.TAB)
		self.find_element(*self.reviewtime_loc).send_keys(s3)

	def input_prizetime(self,s4):
		self.driver.execute_script('document.getElementsByClassName("ivu-input")[10].removeAttribute("readonly");')
		self.find_element(*self.prizetime_loc).send_keys(Keys.TAB)
		self.find_element(*self.prizetime_loc).send_keys(s4)

	def click_tab3(self):
		self.find_element(*self.tab3_loc).click()

	def input_activity_info(self,i):
		self.find_element(*self.activity_info_loc).send_keys(i)

	def input_activitytime(self,s1,s2):
		self.driver.execute_script('document.getElementsByClassName("ivu-input")[12].removeAttribute("readonly");')
		self.find_element(*self.activity_starttime_loc).send_keys(Keys.TAB)
		self.find_element(*self.activity_starttime_loc).send_keys(s1)
		self.driver.execute_script('document.getElementsByClassName("ivu-input")[13].removeAttribute("readonly");')
		self.find_element(*self.activity_endtime_loc).send_keys(Keys.TAB)
		self.find_element(*self.activity_endtime_loc).send_keys(s2)
		self.find_element(*self.activity_endtime_loc).click()

	def click_save(self):
		self.find_element(*self.save_loc).click()
		'''
		button="$('.tr>ivu-btn').click()"
		self.driver.execute_script(button)
		'''
	def list_name_text(self,t):
		return self.find_elements(self.list_text_loc)[t].text
	
	#选择参赛机构
	org_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(1) > div > div > div.ivu-input-group-append > button")
	school_loc=(By.CSS_SELECTOR,"body > div:nth-child(15) > div.ivu-modal-wrap > div > div > div.ivu-modal-body > div > div:nth-child(2) > div.pt10.pb10.ivu-col.ivu-col-span-12 > div:nth-child(1) > div.ivu-table-wrapper > div > div.ivu-table-body > table > tbody > tr > td:nth-child(2) > div")
	page_loc=(By.CSS_SELECTOR,"body > div:nth-child(15) > div.ivu-modal-wrap > div > div > div.ivu-modal-body > div > div:nth-child(2) > div.pt10.pb10.ivu-col.ivu-col-span-12 > div.pt10.tr > ul > div > div > input[type='text']")
	org_button_loc=(By.CSS_SELECTOR,"body > div:nth-child(15) > div.ivu-modal-wrap > div > div > div.ivu-modal-footer > div > button.ivu-btn.ivu-btn-primary")

	def click_org(self):
		self.find_element(*self.org_loc).click()

	def click_org_list(self,n,p=1):
		for i in range(1,3): #p为从第一页开始依次跳转至N页
			#print ("第i页"%d)
			for i in range(0,n): #n为每页选择的数量
				q=self.find_elements(self.school_loc)[i]
				ActionChains(self.driver).double_click(q).perform()
				time.sleep(1)
			
			self.find_element(*self.page_loc).clear()
			self.find_element(*self.page_loc).send_keys(p)
			self.find_element(*self.page_loc).send_keys(Keys.ENTER)
			time.sleep(3)

	def click_org_button(self):
		self.find_element(*self.org_button_loc).click()

	#选择参赛机构批量添加
	delete_org_loc=(By.CSS_SELECTOR,"body > div:nth-child(15) > div.ivu-modal-wrap > div > div > div.ivu-modal-body > div > div:nth-child(1) > div:nth-child(2) > button.ivu-btn.ivu-btn-error")
	

	def click_delete_org(self):
		self.find_element(*self.delete_org_loc).click()

	#编辑活动
	edit_button_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(3) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(6) > div > div > button.ivu-btn.ivu-btn-primary")
	edit_activity_name_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div > div.pt20.ivu-row > div > form:nth-child(2) > div:nth-child(2) > div > div > input")
	
	def click_edit_button(self,e):
		self.find_elements(self.edit_button_loc)[e].click()

	def input_edit_activity_name(self,name):
		self.find_element(*self.edit_activity_name_loc).clear()
		time.sleep(3)
		self.find_element(*self.edit_activity_name_loc).send_keys(name)

	#删除活动
	delete_button_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(3) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(6) > div > div > button.ivu-btn.ivu-btn-error")
	confirm_loc=(By.CSS_SELECTOR,"div.v-transfer-dom > div.ivu-modal-wrap > div > div > div > div > div.ivu-modal-confirm-footer > button.ivu-btn.ivu-btn-primary.ivu-btn-large")
	error_loc=(By.CSS_SELECTOR,"div.v-transfer-dom > div.ivu-modal-wrap > div > div > div > div > div.ivu-modal-confirm-footer > button.ivu-btn.ivu-btn-text.ivu-btn-large")
	def click_delete_button(self,c):
		self.find_elements(self.delete_button_loc)[c].click()

	def click_confirm(self):
		#print (self.find_elements(self.confirm_loc)[0].text)
		self.find_elements(self.confirm_loc)[0].click()
	
	def click_error(self):
		self.find_elements(self.error_loc)[0].click()

	#作品管理
	prize_button_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div:nth-child(3) > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(6) > div > div > button.ivu-btn.ivu-btn-success")
	set_prize_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td.ivu-table-column-center > div > div > button.ivu-btn.ivu-btn-primary")
	click_prize_loc=(By.CSS_SELECTOR,"div.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > div > div > div.pb10.ivu-row > div:nth-child(1) > button > span")
	prize_text_loc=(By.CSS_SELECTOR,"#app > div > div.main > div.container > div > div.router-container > div > div > div.pt10.pb10.ivu-row > div > div.pt10.pb10.ivu-row > div > div > div.ivu-table-body > table > tbody > tr > td:nth-child(5) >div")
	close_button_loc=(By.CSS_SELECTOR,"div.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-footer > div > button > span")
	def click_prize_button(self,p):
		#print (len(self.find_elements(self.prize_button_loc)))
		self.find_elements(self.prize_button_loc)[p].click()

	def click_set_prize(self,s):
		self.find_elements(self.set_prize_loc)[s].click()

	def prize_text(self,t):
		return self.find_elements(self.prize_text_loc)[t].text

	def click_prize(self):
		#print (self.find_elements(self.click_prize_loc)[0].text)
		self.find_elements(self.click_prize_loc)[0].click()

	def click_close_button(self):
		print (self.find_elements(self.close_button_loc)[0].text)
		#self.find_elements(self.close_button_loc)[0].click()

