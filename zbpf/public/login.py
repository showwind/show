def user_login(self,username,password):
	self.driver.maximize_window()
	self.driver.find_element_by_css_selector("#app > div > div > form > div:nth-child(1) > div > div > input").send_keys(username)
	self.driver.find_element_by_css_selector("#app > div > div > form > div:nth-child(2) > div > div > input").send_keys(password)
	self.driver.find_element_by_css_selector("#app > div > div > form > div:nth-child(3) > div > div > div.ivu-col.ivu-col-span-6 > button").click()
	
def user_logout():
	self.driver.find_element_by_link_text(u"退出系统").click()
	print (u"退出成功")
	self.driver.quit()

def Admin_user_login(self,username,password):
	self.driver.maximize_window()
	self.driver.find_element_by_css_selector("#app > div > div > form > div:nth-child(1) > div > div > input").send_keys(username)
	self.driver.find_element_by_css_selector("#app > div > div > form > div:nth-child(2) > div > div > input").send_keys(password)
	self.driver.find_element_by_css_selector("#app > div > div > form > div:nth-child(3) > div > div > div.ivu-col.ivu-col-span-6 > button").click()