#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.usercourse import UserCourse

class TestUserCourse(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.usercourse=UserCourse(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/usercourse.csv"
	
	def test_course_list(self):
		#课程列表
		url=self.base_url+"/v1/frontend/course"
		ac=self.usercourse.course_list(url)
		self.assertEqual(ac,200)

	def test_course_detail(self):
		#课程详情
		cid=getCsv(1,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/course/view"+"?id="+cid+"&expand=isCollect,learnProgress,isJoinCourse,firstSection"+"&token="+token
		ac=self.usercourse.course_detail(url)
		self.assertEqual(ac,200)
		
	def test_user_course(self):
		#课程学习列表
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/user-course"+"?expand=learnProgress&orderBy=createTime&sort=DESC&per-page=5"+"&token="+token
		ac=self.usercourse.user_course(url)
		self.assertEqual(ac,200)

	def test_user_course_collection(self):
		#用户收藏列表
		token=getCsv(0,1,self.filename)
		atype=getCsv(2,1,self.filename)
		url=self.base_url+"/v1/frontend/user-course"+"?type="+atype+"&per-page=5&orderBy=createTime&sort=DESC"+"&token="+token
		ac=self.usercourse.user_course_collection(url)
		self.assertEqual(ac,200)
	
	def test_course_learn(self):
		#用户加入学习
		courseid=getCsv(3,1,self.filename)
		token=getCsv(0,1,self.filename)
		data=[]
		data.append(token)
		data.append(courseid)
		url=self.base_url+"/v1/frontend/course/learn"
		ac=self.usercourse.course_learn(url,data)
		self.assertEqual(ac,200)
		
	def test_teacher_course(self):
		#获取登录教师所创建课程
		status=getCsv(4,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/course/getManageCourses"+"?status="+status+"&token="+token
		ac=self.usercourse.teacher_course(url)
		self.assertEqual(ac,200)

	def test_knowledge_cloud(self):
		#知识云
		courseid=getCsv(5,1,self.filename)
		url=self.base_url+"/v1/frontend/course/getKnowledgeCloud"+"?courseId="+courseid
		ac=self.usercourse.knowledge_cloud(url)
		self.assertEqual(ac,200)

	def test_market_hot(self):
		#热门促销
		url=self.base_url+"/v1/frontend/market/hot"
		ac=self.usercourse.market_hot(url)
		self.assertEqual(ac,200)
	
	def test_get_chaptersource(self):
		#获取章节资料
		courseid=getCsv(6,1,self.filename)
		url=self.base_url+"/v1/frontend/chapter/relateSource"+"?courseId="+courseid
		ac=self.usercourse.get_chaptersource(url)
		self.assertEqual(ac,200)
	
	def test_course_recommend(self):
		#课程推荐
		courseid=getCsv(7,1,self.filename)
		url=self.base_url+"/v1/frontend/course/recommend"+"?courseId="+courseid
		ac=self.usercourse.course_recommend(url)
		self.assertEqual(ac,200)
	
	def test_course_updateshelf(self):
		#课程上下架
		courseid=getCsv(8,1,self.filename)
		onshelf=getCsv(9,1,self.filename)
		token=getCsv(0,1,self.filename)
		data=[]
		data.append(token)
		data.append(courseid)
		data.append(onshelf)
		url=self.base_url+"/v1/frontend/course/updateShelf"
		ac=self.usercourse.course_updateshelf(url,data)
		self.assertEqual(ac,200)
	
	def test_delete_course(self):
		#课程删除
		token=getCsv(0,1,self.filename)
		courseid=getCsv(10,1,self.filename)
		data=[]
		data.append(token)
		data.append(courseid)
		url=self.base_url+"/v1/frontend/course/deleteCourse"
		#self.usercourse.delete_course(url,data)
	
	def test_course_teacher(self):
		#获取课程师资介绍
		courseid=getCsv(11,1,self.filename)
		url=self.base_url+"/v1/frontend/user/getCourseTeacher"+"?courseId="+courseid
		self.usercourse.course_teacher(url)
	
	def test_manage_classes(self):
		#我管理的课程
		status=getCsv(12,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/course/getManageCourses"+"?status="+status+"&token="+token
		ac=self.usercourse.teacher_course(url)
		self.assertEqual(ac,200)
		
	def test_study_progress(self):
		#用户学习进度
		token=getCsv(0,1,self.filename)
		sourceid=getCsv(13,1,self.filename)
		learnlength=getCsv(14,1,self.filename)
		classid=getCsv(15,1,self.filename)
		data=[]
		data.append(token)
		data.append(sourceid)
		data.append(learnlength)
		data.append(classid)
		url=self.base_url+"/v1/frontend/progress"
		self.usercourse.study_progress(url,data)
	
	def test_section_view(self):
		#视频详情
		token=getCsv(0,1,self.filename)
		sid=getCsv(16,1,self.filename)
		#print (token)
		url=self.base_url+"/v1/frontend/section/view"+"?id="+sid+"&expand=video,learnProgress&token="+str(token)
		self.usercourse.section_view(url)

if __name__ == '__main__':
	unittest.main(warnings='ignore')