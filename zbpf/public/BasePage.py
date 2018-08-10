#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
class Action(object):
	def __init__(self,selenium_driver,base_url,pagetitle):
		self.base_url=base_url
		self.driver=selenium_driver
		self.pagetitle=pagetitle

	def _open(self,url,pagetitle):
		self.driver.get(url)
		self.driver.maximize_window()
		assert self.on_page(pagetitle),u'打开网页失败%s'%url

	def find_element(self,*loc):
		try:
			WebDriverWait(self.driver,10).until(lambda driver:driver.find_element(*loc).is_displayed())
			return self.driver.find_element(*loc)
		except:
			print (u"%s页面中未找%s到元素"%(self,loc))

	def find_elements(self,*loc):
		elements=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(*loc))
		return elements

	def open(self):
		self._open(self.base_url,self.pagetitle)

	def on_page(self,pagetitle):
		return pagetitle in self.driver.title 

	def script(self,src):
		return self.driver.execute_script(src)

	def send_keys(self,loc,value,clear_first=True,click_first=True):
		try:
			loc=getattr(self,"_%s"%loc)
			if click_first:
				self.find_element(*loc).click()
			if clear_first:
				self.find_element(*loc).clear()
				self.find_element(*loc).send_keys(value)
		except AttributeError:
			print (u"%s页面中未找到%s元素"%(self,loc))
	def switch_frame(self,loc):
		return self.driver.switch_to_frame(loc)

	def is_alert_present(self,timeout=10):
		result=WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())

	def move_to_element(self,*loc):
		element=self.find_element(*loc)
		ActionChains(self.driver).move_to_element(element).perform()

	def get_attribute(self,name,*loc):
		element=self.find_element(*loc)
		return element.get_attribute(name)

	def select_by_value(self,value,*loc):
		element=self.find_element(*loc)
		Select(element).select_by_value(value)

	def is_text_in_element(self,locator,text):
		try:
			result=WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element(locator,text))
		except TimeoutException:
			print("元素没定位到："+str(locator))
			return False
		else:
			return result
	def is_selected(self,locator,timeout=10):
		result=WebDriverWait(self.driver,timeout,1).until(EC.element_located_to_be_selected(locator))

	def  is_text_in_value(self,locator,value,timeout=10):
		try:
			result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element_value(locator,value))
		except TimeoutException:
			print ("元素没定位到："+str(locator))
			return False
		else:
			return result

	def is_title(self,title,timeout=10):
		'''判断title完全等于'''
		result=WebDriverWait(self.driver,timeout,1).until(EC.title_is(title))
		return result

	def is_title_contains(self,title,timeout=10):
		result=WevDriverWait(self.driver,timeout,1).until(EC.title_contains(title))
		return result

	def is_selected_be(self,locator,selected=True,timeout=10):
		result=WebDriverWait(self.driver,timeout,1).until(EC.element_located_selection_state_to_be(locator,selected))
		return result

	def is_visibility(self,locator,timeout=10):
		result=WebDriverWait(self.driver,timeout,1).until(EC.visibility_of_element_located(locator))
		return result

	def is_invisibility(self,locator,timeout=10):
		result=WebDriverWait(self.driver,timeout,1).until(EC.invisibility_of_element_located(locator))
		return result

	def is_clickable(self,locator,timeout=10):
		result=WebDriverWait(self.driver,timeout,1).until(EC.element_to_be_clickable(locator))
		return result

	def is_located(self,locator,timeout=10):
		result=WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
		return result

	def forward(self):
		self.driver.forward()

	def close(self):
		self.driver.close()

	def quit():
		self.driver.quit()

	def get_title(self):
		return self.driver.title

	def get_text(self,locator):
		element=self.find_element(locator)
		return element.text

	def js_focus_element(self,locator):
		target=self.find_element(locator)
		self.driver.execute_script("arguments[0].scrollIntoView();",target)
	def js_scroll_top(self):
		'''滚动到顶部'''
		js="window.scrollTo(0,0)"
		self.driver.execute_script(js)

	def js_scroll_end(self):
		js="window.scrollTo(0,document.body.scrollHeight)"
		self.driver.execute_script(js)

	def select_by_index(self,locator,index):
		element=self.find_element(locator)
		Select(element).select_by_index(index)

	def select_by_text(self,locator,text):
		element=self.find_element(locator)
		Select(element).select_by_value(text)



