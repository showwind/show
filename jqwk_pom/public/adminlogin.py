#coding=utf-8
def adminlogin(self):
	driver=self.driver
	driver.maximize_window()
	driver.find_element_by_id("username").clear()
	driver.find_element_by_id("username").send_keys("admin11")
	driver.find_element_by_id("password").clear()
	driver.find_element_by_id("password").send_keys("111111")
	driver.find_element_by_css_selector("button.btn.btn-primary").click()
	print (u"登录")

def adminlogout(self):
	driver=self.driver
	driver.find_element_by_xpath("//*[@id='admin-widget']/a[2]").click()
	print (u"退出")
	driver.quit()
