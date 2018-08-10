#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.search import Search

class TestSearch(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.search=Search(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/search.csv"

	def test_search_list(self):
		#课程/班级搜索
		token=getCsv(0,1,self.filename)
		searchkey=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/frontend/search/lists"+"?level=&searchKey="+searchkey+"&page=1&searchType=1&pageSize=20&token="+token
		self.search.search_list(url)

	def test_search_history(self):
		#用户搜索历史
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/user-search/history"+"?token="+token
		self.search.search_history(url)

	def test_clear_search(self):
		#清除搜索历史
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/user-search/clear"+"?token="+token
		self.search.clear_search(url)
if __name__ == '__main__':
	unittest.main(warnings='ignore')