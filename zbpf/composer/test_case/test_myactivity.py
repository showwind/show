#coding=utf-8
import unittest
import requests
from zbpf.composer.models.myactivity import MyActivity
from zbpf.public.composer_csv import getCsv

class TestMyActivity(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.myactivity=MyActivity(s) #实例化
		self.base_url="http://crowdtest.jqweike.com"
		self.file_name="E:/test/zbpf/composer/test_data/myactivity.csv"

	def test_a(self):		
		url=self.base_url+"/v1/admin/site/login"
		username=getCsv(0,0,self.file_name)
		password=getCsv(0,1,self.file_name)
		name=self.myactivity.login(url,username,password)
		self.assertEqual(username,name)

	def test_works_list(self):
		#参赛作品管理
		activeid=getCsv(1,1,self.file_name)
		type_a=getCsv(2,1,self.file_name)
		status=getCsv(3,1,self.file_name)
		url=self.base_url+"/v1/admin/works/list"+"?activeId="+str(activeid)+"&type="+str(type_a)+"&status="+str(status)
		try:
			acid=self.myactivity.works_list(url)
			self.assertEqual(activeid,int(acid))
		except:
			ac=self.myactivity.works_list(url)
			self.assertEqual(ac,200)
	
	def test_work_info(self):
		#查询作品详情
		workid=getCsv(4,1,self.file_name)
		status=getCsv(5,1,self.file_name)
		url=self.base_url+"/v1/admin/works/info"+"?workId="+str(workid)+"&status="+str(status)
		wid=self.myactivity.work_info(url)
		self.assertEqual(workid,wid)
	
	def test_work_audit(self):
		#审核作品
		workid=getCsv(6,1,self.file_name)
		status=getCsv(7,1,self.file_name)
		activityid=getCsv(8,1,self.file_name)
		url=self.base_url+"/v1/admin/works/audit"
		ac=self.myactivity.work_audit(url,workid,status,activityid)
		self.assertEqual(ac,200)	

	def test_active_prize(self):
		#获取活动奖项
		workid=getCsv(9,1,self.file_name)
		activeid=getCsv(10,1,self.file_name)
		url=self.base_url+"/v1/admin/works/active-prize"+"?workId="+str(workid)+"&activeId="+str(activeid)
		ac=self.myactivity.active_prize(url)
		self.assertEqual(ac,200)
	
	def test_set_prize(self):
		#给作品设置奖项
		workid=getCsv(11,1,self.file_name)
		prizeid=getCsv(12,1,self.file_name)
		url=self.base_url+"/v1/admin/works/set-prize"
		ac=self.myactivity.set_prize(url,workid,prizeid)
		self.assertEqual(ac,200)

	def test_prize_list(self):
		#奖品管理
		activeid=getCsv(13,1,self.file_name)
		url=self.base_url+"/v1/admin/works/prize-list"+"?activeId="+str(activeid)
		acid=self.myactivity.prize_list(url)
		if acid==200:
			self.assertEqual(acid,200)
		else:
			self.assertEqual(acid,activeid)

	def test_work_type(self):
		#获取活动类型
		activeid=getCsv(14,1,self.file_name)
		url=self.base_url+"/v1/admin/works/work-type"+"?activeId="+str(activeid)
		dtype=self.myactivity.work_type(url)
		if dtype==200:
			self.assertEqual(dtype,200)
		else:
			self.assertIsNotNone(dtype)

if __name__=="__main__":
	unittest.main(warnings='ignore')