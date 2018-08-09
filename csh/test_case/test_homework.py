#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.homework import HomeWork

class TestHomework(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.homework=HomeWork(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/homework.csv"
	
	def test_homework_list(self):
		#班级作业列表
		classid=getCsv(1,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/homework"+"?classId="+classid+"&expand=isSubmit&token="+token
		ac=self.homework.homework_list(url)
		self.assertEqual(ac,200)

	def test_work_list(self):
		#教师作业提交列表
		token=getCsv(0,1,self.filename)
		status=getCsv(2,1,self.filename)
		workid=getCsv(3,1,self.filename)
		url=self.base_url+"/v1/frontend/homework/listsByWorkId"+"?workId="+workid+"&state="+status+"&token="+token
		ac=self.homework.work_list(url)
		self.assertEqual(ac,200)
		
	def test_create_homework(self):
		#添加作业
		classid=getCsv(4,1,self.filename)
		workname=getCsv(5,1,self.filename)
		require=getCsv(6,1,self.filename)
		sectionname=getCsv(7,1,self.filename)
		sectionid=getCsv(8,1,self.filename)
		endtime=getCsv(9,1,self.filename)
		token=getCsv(0,1,self.filename)
		data=[]
		data.append(token)
		data.append(classid)
		data.append(workname)
		data.append(require)
		data.append(sectionname)
		data.append(sectionid)
		data.append(endtime)
		url=self.base_url+"/v1/frontend/homework/ucreate"
		ac=self.homework.create_homework(url,data)
		self.assertEqual(ac,200)

	def test_delete_homework(self):
		#删除作业
		hwid=getCsv(10,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/homework/delete/"+hwid
		ac=self.homework.delete_homework(url,token)
		self.assertEqual(ac,200)
	
	def test_update_homework(self):
		#批改作业
		hcid=getCsv(15,1,self.filename)
		token=getCsv(0,1,self.filename)
		teachercomment=getCsv(11,1,self.filename)
		checkpath=getCsv(12,1,self.filename)
		score=getCsv(13,1,self.filename)
		state=getCsv(14,1,self.filename)
		data=[]
		data.append(token)
		data.append(teachercomment)
		data.append(checkpath)
		data.append(score)
		data.append(state)
		url=self.base_url+"/v1/frontend/submitHw/update/"+hcid
		self.homework.update_homework(url,data)
	
	def test_submit_homework(self):
		#提交作业
		token=getCsv(16,1,self.filename)
		classid=getCsv(17,1,self.filename)
		workid=getCsv(18,1,self.filename)
		content=getCsv(19,1,self.filename)
		attachment=getCsv(20,1,self.filename)
		data=[]
		data.append(token)
		data.append(classid)
		data.append(workid)
		data.append(content)
		data.append(attachment)
		url=self.base_url+"/v1/frontend/submitHw/create"
		ac=self.homework.submit_homework(url,data)
		self.assertEqual(ac,200)

	def test_homework_listbyclass(self):
		#获取班级下所有提交作品的列表
		token=getCsv(0,1,self.filename)
		classid=getCsv(21,1,self.filename)
		url=self.base_url+"/v1/frontend/homework/listsByClassId"+"?classId="+classid+"&page=1&per-page=20&token="+token
		ac=self.homework.homework_listbyclass(url)
		self.assertEqual(ac,200)

	def test_homework_listbywork(self):
		#获取作业下提交作品的列表
		token=getCsv(0,1,self.filename)
		workid=getCsv(22,1,self.filename)
		state=getCsv(23,1,self.filename)
		url=self.base_url+"/v1/frontend/homework/listsByWorkId"+"?workId="+workid+"&state="+state+"&token="+token
		ac=self.homework.homework_listbywork(url)
		self.assertEqual(ac,200)
if __name__ == '__main__':
	unittest.main(warnings='ignore')