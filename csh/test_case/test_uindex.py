#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.uindex import Uindex

class TestUindex(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.uindex=Uindex(s)
		self.base_url="http://cshapidemo.jqweike.com"
		
	def test_category(self):
		#分类
		url=self.base_url+"/v1/frontend/category"
		ac=self.uindex.category_list(url)
		self.assertEqual(ac,200)
	
	def test_software(self):
		#应用软件
		url=self.base_url+"/v1/frontend/software"
		ac=self.uindex.software_list(url)
		self.assertEqual(ac,200)
	
	def test_allsoft(self):
		#所有软件列表
		url=self.base_url+"/v1/frontend/software/allSoft"
		ac=self.uindex.allsoft(url)
		self.assertEqual(ac,200)
		
	def test_get_activity(self):
		#获取活动
		url=self.base_url+"/v1/frontend/activity/getActivity"
		ac=self.uindex.get_activity(url)
		self.assertEqual(ac,200)

	def test_getrunkcourses(self):
		#热门排行课程
		url=self.base_url+"/v1/frontend/course/getRankCourses"
		ac=self.uindex.get_runkcourses(url)
		self.assertEqual(ac,200)

	def test_getrecommendcourse(self):
		#首页推荐课程
		url=self.base_url+"/v1/frontend/course/getRecommendCourses"
		ac=self.uindex.get_runkcourses(url)
		self.assertEqual(ac,200)
	def test_get_words(self):
		#关键字列表
		url=self.base_url+"/v1/frontend/words"
		ac=self.uindex.get_runkcourses(url)
		self.assertEqual(ac,200)
		
	def test_market_banners(self):
		#首页轮播图
		url=self.base_url+"/v1/frontend/market/banners"
		self.uindex.market_banners(url)
	
	def test_market(self):
		#首页轮播广告位
		url=self.base_url+"/v1/frontend/market"
		self.uindex.market_banners(url)

if __name__ == '__main__':
	unittest.main(warnings='ignore')