#coding=utf-8

def user_login(self,username,password):
	self.driver.maximize_window()
	self.driver.find_element_by_link_text(u"登录").click()
	self.driver.find_element_by_id("username").send_keys(username)
	self.driver.find_element_by_id("password").send_keys(password)
	self.driver.find_element_by_css_selector("#login-form > button").click()
	
def  user_logout():
	self.driver.find_element_by_link_text(u"退出").click()
	print (u"退出成功")
	self.driver.quit()

def Tuser_login(self,username,password):
	self.driver.maximize_window()
	self.driver.find_element_by_link_text(u"登录").click()
	self.driver.find_element_by_id("username").send_keys(username)
	self.driver.find_element_by_id("password").send_keys(password)
	self.driver.find_element_by_css_selector("#login-form > button").click()



