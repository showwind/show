#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.discuss import Discuss

class TestDiscuss(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.discuss=Discuss(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/discuss.csv"

	def test_discuss_list(self):
		#问答/讨论列表
		classid=getCsv(1,1,self.filename)
		courseid=getCsv(2,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/discuss"+"?courseId="+courseid+"&classId="+classid+"&per-page=5&type=2&token="+token
		self.discuss.discuss_list(url)

	def test_create_discuss(self):
		#添加问答/讨论
		token=getCsv(0,1,self.filename)
		courseid=getCsv(3,1,self.filename)
		content=getCsv(4,1,self.filename)
		classid=getCsv(5,1,self.filename)
		atype=getCsv(6,1,self.filename)
		data=[]
		data.append(token)
		data.append(courseid)
		data.append(content)
		data.append(classid)
		data.append(atype)
		url=self.base_url+"/v1/frontend/discuss/create"
		self.discuss.create_discuss(url,data)

	def test_comment_list(self):
		#课程评价列表
		classid=getCsv(7,1,self.filename)
		courseid=getCsv(8,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/comment"+"?courseId="+courseid+"&classId="+classid+"&per-page=5&token="+token
		ac=self.discuss.comment_list(url)
		self.assertEqual(ac,200)

	def test_create_comment(self):
		#新增课程评价
		courseid=getCsv(9,1,self.filename)
		token=getCsv(0,1,self.filename)
		content=getCsv(10,1,self.filename)
		data=[]
		data.append(token)
		data.append(courseid)
		data.append(content)
		url=self.base_url+"/v1/frontend/comment/create"
		ac=self.discuss.create_comment(url,data)
		self.assertEqual(ac,200)

if __name__ == '__main__':
	unittest.main(warnings='ignore')