#coding=utf-8
from selenium import webdriver
import time
from jqwk_pom.public import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

user_login="http://www.jqwk.com/academic/login/index"
admin_url="http://www.jqwk.com/academic.php"
class AddUser(BasePage.Action):
	u"""添加用户"""
	usermanager_loc=(By.CSS_SELECTOR,"#primary-nav > ul > li:nth-child(4) > a")
	users_loc=(By.CSS_SELECTOR,"#primary-nav>ul>li:nth-child(4)>ul>li:nth-child(2)>a")
	adduserbtn_loc=(By.CSS_SELECTOR,"#addUserBtn")
	username_loc=(By.ID,"username")
	groupid_loc=(By.ID,"groupId")
	isteacher_loc=(By.ID,"isTeacher")
	psw_loc=(By.ID,"password")
	nickName_loc=(By.ID,"nickName")
	realName_loc=(By.ID,"realName")
	email_loc=(By.ID,"email")
	stuid_loc=(By.ID,"studentId")
	department_loc=(By.ID,"department")
	phone_loc=(By.ID,"phone")
	weChat_loc=(By.ID,"weChat")
	submit_loc=(By.CSS_SELECTOR,"button.btn.btn-success")

	def click_usermanager(self):
		self.find_element(*self.usermanager_loc).click()

	def click_users(self):
		self.find_element(*self.users_loc).click()
	def click_adduserbtn(self):
		self.find_element(*self.adduserbtn_loc).click()
	def input_username(self,username):
		self.find_element(*self.username_loc).clear()
		self.find_element(*self.username_loc).send_keys(username)
	def select_groupid(self,c):
		s=self.find_element(*self.groupid_loc)
		Select(s).select_by_value(c)

	def select_isteacher(self,c):
		s=self.find_element(*self.isteacher_loc)
		Select(s).select_by_value(c)

	def input_psw(self,password):
		self.find_element(*self.psw_loc).clear()
		self.find_element(*self.psw_loc).send_keys(password)
	def input_nickname(self,nickName):
		self.find_element(*self.nickName_loc).clear()
		self.find_element(*self.nickName_loc).send_keys(nickName)
	def input_realname(self,realName):
		self.find_element(*self.realName_loc).clear()
		self.find_element(*self.realName_loc).send_keys(realName)
	def input_email(self,email):
		self.find_element(*self.email_loc).clear()
		self.find_element(*self.email_loc).send_keys(email)
	def input_stuid(self,studentId):
		self.find_element(*self.stuid_loc).clear()
		self.find_element(*self.stuid_loc).send_keys(studentId)
	def click_btn(self):
		self.find_element(*self.submit_loc).click()

class AddUsers(BasePage.Action):
	u"""批量导入用户"""
	usermanager_loc=(By.CSS_SELECTOR,"#primary-nav > ul > li:nth-child(4) > a")
	users_loc=(By.CSS_SELECTOR,"#primary-nav>ul>li:nth-child(4)>ul>li:nth-child(2)>a")
	addusers_loc=(By.CSS_SELECTOR,"#addUsers")
	file_loc=(By.NAME,"file")
	submit_loc=(By.CSS_SELECTOR,"button.btn.btn-success")

	def click_usermanager(self):
		self.find_element(*self.usermanager_loc).click()

	def click_users(self):
		self.find_element(*self.users_loc).click()
	def click_addusers(self):
		self.find_element(*self.addusers_loc).click()
	def input_file(self,c):
		self.find_element(*self.file_loc).send_keys(c)

	def click_btn(self):
		self.find_element(*self.submit_loc).click()

class UpdateUser(BasePage.Action):
	usermanager_loc=(By.CSS_SELECTOR,"#primary-nav > ul > li:nth-child(4) > a")
	users_loc=(By.CSS_SELECTOR,"#primary-nav>ul>li:nth-child(4)>ul>li:nth-child(2)>a")
	sykey_loc=(By.CSS_SELECTOR,"#scKeyword")
	search_loc=(By.CSS_SELECTOR,"#search")
	u_loc=(By.CSS_SELECTOR,"#tbody > tr > td[tt='name']")
	user_loc=(By.CSS_SELECTOR,"#tbody > tr > td:nth-child(9) > span.editor >a ")
	username_loc=(By.ID,"username")
	isteacher_loc=(By.ID,"isTeacher")
	submit_loc=(By.CSS_SELECTOR,"button.btn.btn-success")
	active_loc=(By.CSS_SELECTOR,"#nav-info > li.active > a")

	def click_usermanager(self):
		self.find_element(*self.usermanager_loc).click()
	def click_users(self):
		self.find_element(*self.users_loc).click()
	def input_sykey(self,c):
		self.find_element(*self.sykey_loc).clear()
		self.find_element(*self.sykey_loc).send_keys(c)
	def click_search(self):
		self.find_element(*self.search_loc).click()
	def userinfo_p(self):
		t=self.find_elements(self.u_loc)
		#print (t[1].text)
		return t[0].text
	def click_user(self):
		self.find_elements(self.user_loc)[1].click()
	def  update_name(self,c):
		self.find_element(*self.username_loc).clear()
		self.find_element(*self.username_loc).send_keys(c)
	def  update_isteacher(self,c):
		s=self.find_element(*self.isteacher_loc)
		Select(s).select_by_value(c)
	def click_submit(self):
		self.find_element(*self.submit_loc).click()
	def click_active(self):
		self.find_element(*self.active_loc).click()

class Updateup(BasePage.Action):
	sykey_loc=(By.CSS_SELECTOR,"#scKeyword")
	search_loc=(By.CSS_SELECTOR,"#search")
	u_loc=(By.CSS_SELECTOR,"#tbody > tr > td[tt='name']")
	user_loc=(By.CSS_SELECTOR,"#tbody > tr> td:nth-child(9) > span.update >img ")
	type_loc=(By.CSS_SELECTOR,"#Modal1 > div > div > div.modal-body > select.type11.form-control")
	submit_loc=(By.CSS_SELECTOR,"#Modal1 > div > div > div.modal-footer >button.btn.btn-primary ")
	comfirm_loc=(By.CSS_SELECTOR,"body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm")
	group_loc=(By.CSS_SELECTOR,"#tbody > tr > td:nth-child(4)")
	def input_sykey(self,c):
		self.find_element(*self.sykey_loc).clear()
		self.find_element(*self.sykey_loc).send_keys(c)
	def click_search(self):
		self.find_element(*self.search_loc).click()
	def userinfo_p(self):
		t=self.find_elements(self.u_loc)
		return t[0].text
	def click_user(self):
		t=self.find_elements(self.user_loc)
		t[1].click()
	def click_type(self,c):
		s=self.find_element(*self.type_loc)
		Select(s).select_by_value(c)
	def click_submit(self):
		self.find_element(*self.submit_loc).click()
	def click_comfirm(self):
		self.find_element(*self.comfirm_loc).click()
	def group_p(self):
		return self.find_elements(self.group_loc)[1].text

class Deleteuser(BasePage.Action):
	sykey_loc=(By.CSS_SELECTOR,"#scKeyword")
	search_loc=(By.CSS_SELECTOR,"#search")
	u_loc=(By.CSS_SELECTOR,"#tbody > tr > td[tt='name']")
	user_loc=(By.CSS_SELECTOR,"#tbody > tr > td:nth-child(9) > span.del >img ")
	del_loc=(By.CSS_SELECTOR,"body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm")
	def input_sykey(self,c):
		self.find_element(*self.sykey_loc).clear()
		self.find_element(*self.sykey_loc).send_keys(c)
	def click_search(self):
		self.find_element(*self.search_loc).click()
	def userinfo_p(self):
		t=self.find_elements(self.u_loc)
		return t[0].text
	def click_user(self):
		self.find_elements(self.user_loc)[6].click()
	def click_del(self):
		self.find_element(*self.del_loc).click()

class SearchUser(BasePage.Action):
	usermanager_loc=(By.CSS_SELECTOR,"#primary-nav > ul > li:nth-child(4) > a")
	users_loc=(By.CSS_SELECTOR,"#primary-nav>ul>li:nth-child(4)>ul>li:nth-child(2)>a")
	usergroup_loc=(By.CSS_SELECTOR,"#scUserGroup")
	department_loc=(By.CSS_SELECTOR,"#scDepartment")
	sykey_loc=(By.CSS_SELECTOR,"#scKeyword")
	search_loc=(By.CSS_SELECTOR,"#search")
	u_loc=(By.CSS_SELECTOR,"#tbody > tr > td[tt='name']")
	def input_search(self,c='',d='',e=''):
		s=self.find_element(*self.usergroup_loc)
		Select(s).select_by_value(c)
		self.find_element(*self.department_loc).clear()
		self.find_element(*self.department_loc).send_keys(d)
		self.find_element(*self.sykey_loc).clear()
		self.find_element(*self.sykey_loc).send_keys(e)
	def click_search(self):
		self.find_element(*self.search_loc).click()
	def click_usermanager(self):
		self.find_element(*self.usermanager_loc).click()
	def click_users(self):
		self.find_element(*self.users_loc).click()	
	def userinfo_p(self):
		t=self.find_elements(self.u_loc)
		return t[0].text
class RdList(BasePage.Action):
	usergroup_loc=(By.CSS_SELECTOR,"#scUserGroup")
	department_loc=(By.CSS_SELECTOR,"#scDepartment")
	sykey_loc=(By.CSS_SELECTOR,"#scKeyword")
	search_loc=(By.CSS_SELECTOR,"#search")
	name_loc=(By.CSS_SELECTOR,"#tbody > tr > td[tt='name']")
	realname_loc=(By.CSS_SELECTOR,"#tbody > tr > td[tt='realName']")
	email_loc=(By.CSS_SELECTOR,"#tbody > tr > td[tt='email']")
	renderlist_loc=(By.CSS_SELECTOR,"#pages > li.next>a")

	def input_search(self,c='',d='',e=''):
		s=self.find_element(*self.usergroup_loc)
		Select(s).select_by_value(c)
		self.find_element(*self.department_loc).clear()
		self.find_element(*self.department_loc).send_keys(d)
		self.find_element(*self.sykey_loc).clear()
		self.find_element(*self.sykey_loc).send_keys(e)

	def click_search(self):
		self.find_element(*self.search_loc).click()

	def click_renderlist(self,n):
		for i in range(0,n):
			s1=self.find_elements(self.name_loc)
			s2=self.find_elements(self.realname_loc)
			s3=self.find_elements(self.email_loc)
			for j in range(0,8):
				print (s1[j].text,s2[j].text,s3[j].text) 
			self.find_element(*self.renderlist_loc).click()
			print (u"第%s页:"%(i+1))





		