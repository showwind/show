#coding=utf-8
import unittest,requests
from zbpf.composer.models.school import School
from zbpf.public.composer_csv import getCsv

class TestSchool(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.school=School(s)
		self.base_url="http://crowdtest.jqweike.com"
		self.filename="E:/test/zbpf/composer/test_data/school.csv"

	def test_area_school(self):
		#获取省列表(超级管理员)
		url=self.base_url+"/v1/admin/area/province?random=0.7704160640963464"
		aid=self.school.province_list(url)
		self.assertEqual(aid,200)

	def test_school_list(self):
		data=[]
		area=getCsv(1,1,self.filename)
		pagesize=getCsv(3,1,self.filename)
		page=getCsv(4,1,self.filename)
		data.append(area)
		data.append(pagesize)
		data.append(page)
		url=self.base_url+"/v1/admin/activity/school-list"
		sid=self.school.school_list(url,data)
		self.assertEqual(sid,200)

if __name__ == '__main__':
	unittest.main(warnings='ignore')
