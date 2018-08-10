#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.adminclasses import AdminClasses

class TestAdminClasses(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.adminclasses=AdminClasses(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/adminclasses.csv"
		
	def test_course_list(self):
		#班级列表
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/admin/classes"+"?token="+token
		ac=self.adminclasses.classes_list(url)
		self.assertEqual(ac,200)
	
	def test_classes_view(self):
		#班级详情
		token=getCsv(0,1,self.filename)
		classid=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/admin/classes/view/"+classid+"?token="+token
		ac=self.adminclasses.classes_view(url)
		self.assertEqual(ac,200)
		
	def test_classes_onself(self):
		#班级上(下)架
		token=getCsv(0,1,self.filename)
		classid=getCsv(2,1,self.filename)
		data=[]
		data.append(token)
		data.append(classid)
		url=self.base_url+"/v1/admin/classes/onShelf"
		ac=self.adminclasses.classes_onself(url,data)
		self.assertEqual(ac,200)
	
	def test_student_list(self):
		token=getCsv(0,1,self.filename)
		keyword=getCsv(3,1,self.filename)
		url=self.base_url+"/v1/admin/user/student"+"?token="+token+"&keyword="+keyword
		ac=self.adminclasses.student_list(url)
		self.assertEqual(ac,200)
	
	def test_add_student(self):
		#给班级添加学生
		token=getCsv(0,1,self.filename)
		classid=getCsv(4,1,self.filename)
		userid=getCsv(5,1,self.filename)
		data=[]
		data.append(token)
		data.append(classid)
		data.append(userid)
		url=self.base_url+"/v1/admin/classes/addStudent"
		self.adminclasses.add_student(url,data)
		
	def test_delete_student(self):
		#删除班级学生
		token=getCsv(0,1,self.filename)
		sid=getCsv(6,1,self.filename)
		data=[]
		data.append(token)
		url=self.base_url+"/v1/admin/classStudent/delete/"+sid
		self.adminclasses.delete_student(url,data)
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')