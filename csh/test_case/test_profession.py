#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.profession import Profession

class TestProfession(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.profession=Profession(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/profession.csv"

	def test_category_profession_list(self):
		#职业列表
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/category/profession"+"?token="+token
		ac=self.profession.category_profession_list(url)
		self.assertEqual(ac,200)
	
	def test_profession_list(self):
		#技能课程关联
		token=getCsv(0,1,self.filename)
		number=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/frontend/category/profession"+"?number="+number+"&token="+token
		ac=self.profession.profession_list(url)
		self.assertEqual(ac,200)

	def test_jobs_list(self):
		#招聘信息
		token=getCsv(0,1,self.filename)
		name=getCsv(2,1,self.filename)
		url=self.base_url+"/v1/frontend/jobs"+"?profession="+name+"&page=1&per-page=3&token="+token
		ac=self.profession.jobs_list(url)
		self.assertEqual(ac,200)

	def test_relate_source(self):
		number=getCsv(3,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/profession/relateSource"+"?number="+str(number)+"&token="+token
		ac=self.profession.relate_source(url)
		self.assertEqual(ac,200)

	def test_relate_salary(self):
		profession=getCsv(4,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/salary"+"?profession="+profession+"&token="+token
		ac=self.profession.relate_salary(url)
		self.assertEqual(ac,200)
if __name__ == '__main__':
	unittest.main(warnings='ignore')