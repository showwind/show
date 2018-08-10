#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.addcourse import AddCourse

class TestAddCourse(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.addcourse=AddCourse(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/addcourse.csv"
		self.filename1="E:/test/csh/test_data/addquestion.csv"
		
	def test_add_course(self):
		#添加课程第一步
		token=getCsv(0,1,self.filename)
		coursename=getCsv(1,1,self.filename)
		parentname=getCsv(2,1,self.filename)
		parentnumber=getCsv(3,1,self.filename)
		catename=getCsv(4,1,self.filename)
		catenumber=getCsv(5,1,self.filename)
		softnumber=getCsv(6,1,self.filename)
		softname=getCsv(7,1,self.filename)
		softversion=getCsv(8,1,self.filename)
		price=getCsv(9,1,self.filename)
		info=getCsv(10,1,self.filename)
		cover=getCsv(11,1,self.filename)
		level=getCsv(12,1,self.filename)
		data=[]
		data.append(token)
		data.append(coursename)
		data.append(parentname)
		data.append(parentnumber)
		data.append(catename)
		data.append(catenumber)
		data.append(softnumber)
		data.append(softname)
		data.append(softversion)
		data.append(price)
		data.append(info)
		data.append(cover)
		data.append(level)
		url=self.base_url+"/v1/frontend/course/addCourse"
		ac=self.addcourse.add_course(url,data)
		self.assertEqual(ac,200)

	def test_create_chapter(self):
		#添加章节
		token=getCsv(0,1,self.filename)
		chaptername=getCsv(13,1,self.filename)
		courseid=getCsv(14,1,self.filename)
		atype=getCsv(15,1,self.filename)
		parentid=getCsv(16,1,self.filename)
		data=[]
		data.append(token)
		data.append(chaptername)
		data.append(courseid)
		data.append(atype)
		data.append(parentid)
		url=self.base_url+"/v1/frontend/create-chapter/create"
		self.addcourse.create_chapter(url,data)

	def test_delete_chapter(self):
		#删除章小节
		token=getCsv(0,1,self.filename)
		chapterid=getCsv(17,1,self.filename)
		parentid=getCsv(18,1,self.filename)
		data=[]
		data.append(chapterid)
		data.append(parentid)
		data.append(token)
		url=self.base_url+"/v1/frontend/chapter/del"
		self.addcourse.delete_chapter(url,data)
		
	def test_add_intro(self):
		#添加课程简介
		cid=getCsv(19,1,self.filename)
		intro=getCsv(20,1,self.filename)
		token=getCsv(0,1,self.filename)
		data=[]
		data.append(intro)
		data.append(token)
		url=self.base_url+"/v1/frontend/create-chapter/update"+"?id="+cid
		ac=self.addcourse.add_intro(url,data)
		self.assertEqual(ac,200)

	def test_add_view(self):
		#上传视频
		videoname=getCsv(21,1,self.filename)
		videopath=getCsv(22,1,self.filename)
		videotype=getCsv(23,1,self.filename)
		chapterid=getCsv(24,1,self.filename)
		token=getCsv(0,1,self.filename)
		data=[]
		data.append(videoname)
		data.append(videopath)
		data.append(videotype)
		data.append(chapterid)
		data.append(token)
		url=self.base_url+"/v1/frontend/video/addVideo"
		ac=self.addcourse.add_view(url,data)
		self.assertEqual(ac,200)
		
	def test_update_info(self):
		#修改章简介
		intro=getCsv(25,1,self.filename)
		token=getCsv(0,1,self.filename)
		cid=getCsv(26,1,self.filename)
		data=[]
		data.append(token)
		data.append(intro)
		url=self.base_url+"/v1/frontend/chapter/update/"+cid
		ac=self.addcourse.update_info(url,data)
		self.assertEqual(ac,200)

	def test_chapter(self):
		#课程章节
		token=getCsv(0,1,self.filename)
		courseid=getCsv(42,1,self.filename)
		url=self.base_url+"/v1/frontend/chapter"+"?courseId="+courseid+"&expand=totalCount&token="+token
		ac=self.addcourse.chapter_info(url)
		self.assertEqual(ac,200)

	def test_delete_question(self):
		#删除试题
		cid=getCsv(27,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/question/delete/"+cid
		ac=self.addcourse.delete_question(url,token)
		self.assertEqual(ac,200)
	
	def test_add_question(self):
		#新增试题
		token=getCsv(0,1,self.filename1)
		chapterid=getCsv(1,1,self.filename1)
		content=getCsv(2,1,self.filename1)
		questiontype=getCsv(3,1,self.filename1)
		scene=getCsv(4,1,self.filename1)
		standaranswer=getCsv(5,1,self.filename1)
		answers0=getCsv(6,1,self.filename1)
		answers1=getCsv(7,1,self.filename1)
		answers2=getCsv(8,1,self.filename1)
		data=[]
		data.append(token)
		data.append(chapterid)
		data.append(content)
		data.append(questiontype)
		data.append(scene)
		data.append(answers0)
		data.append(answers1)
		data.append(answers2)
		url=self.base_url+"/v1/frontend/question/addQuestion"
		self.addcourse.add_question(url,data)
	
	def test_create_resource(self):
		#添加素材
		token=getCsv(0,1,self.filename)
		resourcename=getCsv(28,1,self.filename)
		path=getCsv(29,1,self.filename)
		filetype=getCsv(30,1,self.filename)
		chapterid=getCsv(31,1,self.filename)
		data=[]
		data.append(token)
		data.append(resourcename)
		data.append(path)
		data.append(filetype)
		data.append(chapterid)
		url=self.base_url+"/v1/frontend/resource/create"
		self.addcourse.create_resource(url,data)
	
	def test_delete_resource(self):
		#删除素材
		rid=getCsv(32,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/resource/delete"+"?id="+rid
		ac=self.addcourse.delete_resource(url,token)
		self.assertEqual(ac,200)
	
	def test_section_view(self):
		#添加课程回显数据
		vid=getCsv(33,1,self.filename)
		token=getCsv(0,1,self.filename)
		operation=getCsv(34,1,self.filename)
		expand=getCsv(35,1,self.filename)
		url=self.base_url+"/v1/frontend/section/view"+"?id="+vid+"&operation="+operation+"&expand="+expand+"&token="+token
		self.addcourse.section_view(url)
		
	def test_update_course(self):
		#保存/发布课程
		token=getCsv(0,1,self.filename)
		courseid=getCsv(36,1,self.filename)
		status=getCsv(37,1,self.filename)
		chapterid=getCsv(38,1,self.filename)
		data=[]
		data.append(token)
		data.append(courseid)
		data.append(status)
		data.append(chapterid)
		url=self.base_url+"/v1/frontend/course/updateCourseStatus"
		self.addcourse.update_course(url,data)
		
	def test_course_detail(self):
		#课程数据回显
		courseid=getCsv(39,1,self.filename)
		expand=getCsv(40,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/course/detail"+"?courseId="+courseid+"&expand="+expand+"&token="+token
		ac=self.addcourse.course_detail(url)
		self.assertEqual(ac,200)

	def test_question_detail(self):
		#单个试题数据回显
		questionid=getCsv(41,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/question/detail"+"?questionId="+questionid+"&token="+token
		self.addcourse.question_detail(url)
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')
