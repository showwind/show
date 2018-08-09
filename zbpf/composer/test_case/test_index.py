#coding=utf-8
import unittest,requests
from zbpf.composer.models.userindex import UserIndex
from zbpf.public.composer_csv import getCsv

class TestUserIndex(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.userindex=UserIndex(s)
		self.base_url="http://crowdtest.jqweike.com"
		self.base_url1="http://share.jqweike.com"
		self.filename="E:/test/zbpf/composer/test_data/userindex.csv"
		self.worksname="E:/test/zbpf/composer/test_data/works.csv"
	
	def test_get_userinfo(self):
		#获取用户信息
		userid=getCsv(0,1,self.filename)
		accesstoken=getCsv(1,1,self.filename)
		url=self.base_url1+"/v1/frontend/user/get-user-info"+"?userId="+userid+"&accessToken="+accesstoken+"&token="+accesstoken
		ac=self.userindex.get_user_info(url)
	
	def test_get_picture(self):
		#首页轮播图
		userid=getCsv(0,1,self.filename)
		token=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/frontend/index/get-pictures"+"?userId="+userid+"&token="+token
		ac=self.userindex.get_picture(url)
		self.assertEqual(ac,200)

	def test_get_activity(self):
		#获取活动列表数据
		status=getCsv(2,1,self.filename)
		atype=getCsv(3,1,self.filename)
		token=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/frontend/index/get-activity"+"?status="+status+"&type="+atype+"&token="+token
		ac=self.userindex.get_activity(url)
		self.assertEqual(ac,200)

	def  test_activity_info(self):
		#活动详情
		userid=getCsv(4,1,self.filename)
		activityid=getCsv(5,1,self.filename)
		atype=getCsv(6,1,self.filename)
		token=getCsv(7,1,self.filename)
		url=self.base_url+"/v1/frontend/activity/get-info"+"?activityId="+activityid+"&type="+atype+"&userId="+userid+"&token="+token
		ac=self.userindex.get_activity_info(url)
		self.assertEqual(ac,200)
	
	def test_get_news(self):
		#获取新闻列表
		length=getCsv(8,1,self.filename)
		token=getCsv(9,1,self.filename)
		url=self.base_url+"/v1/frontend/index/get-news"+"?length="+length+"&token="+token
		ac=self.userindex.get_news(url)
		self.assertEqual(ac,200)
	
	def test_works_lists(self):
		#获取作品
		token=getCsv(1,1,self.filename)
		page=getCsv(10,1,self.filename)
		length=getCsv(11,1,self.filename)
		userid=getCsv(0,1,self.filename)
		ismine=getCsv(12,1,self.filename)
		url=self.base_url+"/v1/frontend/works/lists"+"?page="+page+"&length="+length+"&userId="+userid+"&isMine="+ismine+"&token="+token
		ac=self.userindex.get_news(url)
		self.assertEqual(ac,200)	
	
	def test_sign_up(self):
		#用户报名
		activityid=getCsv(13,1,self.filename)
		userid=getCsv(0,1,self.filename)
		token=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/frontend/activity/user-sign-up"+"?activityId="+activityid+"&userId="+userid+"&token="+token
		self.userindex.sign_up(url)
	
	def test_add_hits(self):
		#作品点赞
		userid=getCsv(0,1,self.filename)
		workid=getCsv(14,1,self.filename)
		token=getCsv(1,1,self.filename)
		data=[]
		data.append(userid)
		data.append(workid)
		data.append(token)
		url=self.base_url+"/v1/frontend/works/add-hits"
		self.userindex.add_hits(url,data)
	
	def test_get_runk(self):
		#已结束获取作品排名
		activityid=getCsv(24,1,self.filename)
		token=getCsv(25,1,self.filename)
		url=self.base_url+"/v1/frontend/works/get-rank"+"?activityId="+activityid+"&length=7&token="+token
		ac=self.userindex.get_runk(url)
		self.assertEqual(ac,200)

	def test_news_info(self):
		#新闻详情
		newsid=getCsv(15,1,self.filename)
		token=getCsv(16,1,self.filename)
		url=self.base_url+"/v1/frontend/news/get-info"+"?newsId="+newsid+"&token="+token
		ac=self.userindex.news_info(url)
		self.assertEqual(ac,200)

	def test_user_score(self):
		#用户抽奖列表
		url=self.base_url+"/v1/frontend/user-score/lists"
		ac=self.userindex.user_score(url)
		self.assertEqual(ac,200)

	def test_type_lists(self):
		activityid=getCsv(17,1,self.filename)
		token=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/frontend/works/type-lists"+"?activityId="+activityid+"&token="+token
		ac=self.userindex.type_lists(url)
		self.assertEqual(ac,200)
	
	def test_get_info(self):
		#作品详情
		workid=getCsv(18,1,self.filename)
		userid=getCsv(19,1,self.filename)
		token=getCsv(20,1,self.filename)
		url=self.base_url+"/v1/frontend/works/get-info"+"?workId="+workid+"&userId="+userid+"&token="+token
		ac=self.userindex.get_work_info(url)
		self.assertEqual(ac,200)

	def test_end_time(self):
		#活动倒计时
		activityid=getCsv(21,1,self.filename)
		token=getCsv(22,1,self.filename)
		url=self.base_url+"/v1/frontend/activity/end-time"+"?activityId="+activityid+"&token="+token
		ac=self.userindex.end_time(url)
		self.assertEqual(ac,200)
		
	def test_add_share(self):
		#作品分享
		data=[]
		workid=getCsv(23,1,self.filename)
		userid=getCsv(0,1,self.filename)
		token=getCsv(1,1,self.filename)
		data.append(workid)
		data.append(userid)
		data.append(token)
		url=self.base_url+"/v1/frontend/works/add-share"
		ac=self.userindex.add_share(url,data)
		self.assertEqual(ac,200)
	
	def test_remove_file(self):
		#删除文件
		data=[]
		userid=getCsv(0,1,self.worksname)
		activityId=getCsv(4,1,self.worksname)
		totalSize=getCsv(3,1,self.worksname)
		lastModifiedTime=getCsv(5,1,self.worksname)
		data.append(userid)
		data.append(activityId)
		data.append(totalSize)
		data.append(lastModifiedTime)
		url=self.base_url+"/v1/frontend/works/remove-file"
		ac=self.userindex.remove_file(url,data)
		self.assertEqual(ac,200)
	
	def test_work_file(self):
		#获取文件进度
		data=[]
		userid=getCsv(0,1,self.worksname)
		file=getCsv(1,1,self.worksname)
		lastModifiedDate=getCsv(2,1,self.worksname)
		totalSize=getCsv(3,1,self.worksname)
		activityId=getCsv(4,1,self.worksname)
		lastModifiedTime=getCsv(5,1,self.worksname)
		data.append(userid)
		data.append(file)
		data.append(lastModifiedDate)
		data.append(totalSize)
		data.append(activityId)
		data.append(lastModifiedTime)
		url=self.base_url+"/v1/frontend/works/file-progress"+"?activityId="+activityId+"&userId="+userid+"&clientName="+file+"&totalSize="+totalSize+"&lastModifiedTime="+lastModifiedTime
		self.userindex.work_file(url)
		url1=self.base_url+"/v1/frontend/works/work-file-upload"
		self.userindex.file_upload(url1,data)

	def test_work_file_progress(self):
		#保存文件进度
		data=[]
		userid=getCsv(0,1,self.worksname)
		activityId=getCsv(4,1,self.worksname)
		clientName=getCsv(1,1,self.worksname)
		totalSize=getCsv(3,1,self.worksname)
		uploadSize=getCsv(6,1,self.worksname)
		lastModifiedTime=getCsv(5,1,self.worksname)
		data.append(userid)
		data.append(activityId)
		data.append(clientName)
		data.append(totalSize)
		data.append(uploadSize)
		data.append(lastModifiedTime)
		url2=self.base_url+"/v1/frontend/works/save-file-progress"
		self.userindex.file_progress(url2,data)
		
	def test_work_file_zadd(self):
		#添加作品
		data=[]
		activityid=getCsv(7,1,self.worksname)
		workname=getCsv(8,1,self.worksname)
		username=getCsv(9,1,self.worksname)
		userid=getCsv(10,1,self.worksname)
		atype=getCsv(11,1,self.worksname)
		file=getCsv(12,1,self.worksname)
		tel=getCsv(13,1,self.worksname)
		departments=getCsv(14,1,self.worksname)
		studentid=getCsv(15,1,self.worksname)
		division=getCsv(16,1,self.worksname)
		lastModifiedTime=getCsv(17,1,self.worksname)
		token=getCsv(18,1,self.worksname)
		data.append(activityid)
		data.append(workname)
		data.append(username)
		data.append(userid)
		data.append(atype)
		data.append(file)
		data.append(tel)
		data.append(departments)
		data.append(studentid)
		data.append(division)
		data.append(lastModifiedTime)
		data.append(token)
		url=self.base_url+"/v1/frontend/works/add-work"
		self.userindex.add_work(url,data)

	def test_user_work(self):
		#作品回显
		activityid=getCsv(19,1,self.worksname)
		userid=getCsv(0,1,self.worksname)
		token=getCsv(18,1,self.worksname)
		url=self.base_url+"/v1/frontend/works/user-work"+"?activityId="+activityid+"&userId="+userid+"&token="+token
		ac=self.userindex.user_work(url)
		self.assertEqual(ac,200)
	
	def test_get_all_upload_files(self):
		page=getCsv(26,1,self.filename)
		userid=getCsv(27,1,self.filename)
		token=getCsv(28,1,self.filename)
		url=self.base_url+"/v1/frontend/works/get-all-upload-files"+"?page="+page+"&length=99999&userId="+userid+"&token"+token
		ac=self.userindex.get_all_upload_files(url)
		self.assertEqual(ac,200)
	
	def test_record_click(self):
		data=[]
		fileId=getCsv(29,1,self.filename)
		atype=getCsv(30,1,self.filename)
		token=getCsv(31,1,self.filename)
		data.append(fileId)
		data.append(atype)
		data.append(token)
		url=self.base_url+"/v1/frontend/works/record-click"
		self.userindex.record_click(url,data)

if __name__ == '__main__':
	unittest.main(warnings='ignore')
