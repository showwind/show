#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.classes import Classes

class TestClasses(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.classes=Classes(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/classes.csv"

	def test_class_list(self):
		#获取班级列表
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/classes"+"?token="+token
		ac=self.classes.class_list(url)
		self.assertEqual(ac,200)

	def test_user_class(self):
		#获取用户班级
		token=getCsv(0,1,self.filename)
		status=getCsv(1,1,self.filename)
		pagesize=getCsv(2,1,self.filename)
		url=self.base_url+"/v1/frontend/user-class"+"?status="+status+"&pageSize="+pagesize+"&token="+token
		ac=self.classes.user_class(url)
		self.assertEqual(ac,200)
		
	def test_join_class(self):
		#用户加入班级
		token=getCsv(0,1,self.filename)
		classid=getCsv(3,1,self.filename)
		url=self.base_url+"/v1/frontend/user-class/joinClass"
		self.classes.join_class(url,classid,token)

	def test_view_class(self):
		#获取班级详情
		token=getCsv(0,1,self.filename)
		classid=getCsv(4,1,self.filename)
		url=self.base_url+"/v1/frontend/classes/view"+"?id="+classid+"&expand=isJoinClass,learnProgress,firstSection"+"&token="+token
		self.classes.view_class(url)

	def test_recommend_classes(self):
		#班级详情推荐班级
		courseid=getCsv(5,1,self.filename)
		url=self.base_url+"/v1/frontend/course/recommend"+"?courseId="+courseid
		self.classes.recommend_classes(url)
		
	def test_update_classes(self):
		#修改班级状态
		status=getCsv(6,1,self.filename)
		classid=getCsv(7,1,self.filename)
		token=getCsv(8,1,self.filename)
		url=self.base_url+"/v1/frontend/classes/update/"+str(classid)
		ac=self.classes.update_classes(url,status,token)
		self.assertEqual(ac,200)
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')