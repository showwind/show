#coding=utf-8
import unittest
import time
from selenium import webdriver
from bs4 import BeautifulSoup

url="http://bjtudemo.jqweike.com/"
username='15102213@bjtu.edu.cn'
password='15102213@bjtu.edu.cn'
class GetUrl(unittest.TestCase):
	def setUp(self):
		self.dr=webdriver.Chrome()
		self.dr.get(url)
	def tearDown(self):
		self.dr.quit()
	def login(self):
		self.dr.maximize_window()
		#self.dr.find_element_by_link_text(u"登录").click()
		print (self.dr.title)
		self.dr.find_element_by_id("username").clear()
		self.dr.find_element_by_id("username").send_keys(username)
		self.dr.find_element_by_id("password").clear()
		self.dr.find_element_by_id("password").send_keys(password)
		self.dr.find_element_by_css_selector("#login-form > button").click()
	def _gethtmlcontent(self):
		content=self.dr.page_source
		return content
	def _geturl(self,pagesource):		

		result=dict()
		soup=BeautifulSoup(pagesource,"lxml")
		eles=soup.find_all("a")
		flag=0
		for ele in eles:
			if "#" in ele.get('href',''): #if "#" in ele['href']
				continue
			tmp=ele.string
			if tmp is not None and '@' not in tmp:
				flag+=1
				#ele_url=ele['href'].split('?')[0]
				ele_url=ele.get('href','')
				result[tmp]=ele_url
		return result

	def  _writetotxt(self,contents):
		print (u'写入开始')
		with open('.\\report\\urlcontent.txt','w') as f: #注意路径
			for title,value in contents.items():
				f.write('{0}==>{1}\n'.format(title,value))
		print (u'写入完毕')
	def test_run(self):
		'''爬取页面a标签'''
		self.login()
		pagesources=self._gethtmlcontent()
		result=self._geturl(pagesources)
		self._writetotxt(result)
if __name__=='__main__':
	unittest.main()