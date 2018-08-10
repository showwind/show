#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.admincourse import AdminCourse

class TestAdminCourse(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.admincourse=AdminCourse(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/admincourse.csv"

	def test_course_list(self):
		#课程列表
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/admin/course"+"?token="+token
		ac=self.admincourse.course_list(url)
		self.assertEqual(ac,200)

	def test_course_view(self):
		#课程详情
		token=getCsv(0,1,self.filename)
		courseid=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/admin/course/view/"+courseid+"?token="+token
		ac=self.admincourse.course_view(url)
		self.assertEqual(ac,200)
	
	def test_chapter_sourcecount(self):
		#课程详情-文件
		token=getCsv(0,1,self.filename)
		courseid=getCsv(2,1,self.filename)
		url=self.base_url+"/v1/admin/chapter/sourceCount"+"?courseId="+courseid+"&token="+token
		self.admincourse.chapter_sourcecount(url)
	
	def test_admin_discuss(self):
		#课程评论
		token=getCsv(0,1,self.filename)
		courseid=getCsv(2,1,self.filename)
		url=self.base_url+"/v1/admin/discuss"+"?token="+token
		self.admincourse.admin_discuss(url)
	
	def test_user_teacher(self):
		#老师用户
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/admin/user/teacher"+"?token="+token+"&pageSize=10&page=1&keyword=&searchType=username"
		self.admincourse.user_teacher(url)

	def test_user_student(self):
		#学生用户
		token=getCsv(0,1,self.filename)
		keyword=getCsv(4,1,self.filename)
		url=self.base_url+"/v1/admin/user"+"?token="+token+"&page=1&pageSize=10&keyword="+keyword+"&searchType=username&rangeStart=&rangeEnd="
		self.admincourse.user_student(url)
if __name__ == '__main__':
	unittest.main(warnings='ignore')