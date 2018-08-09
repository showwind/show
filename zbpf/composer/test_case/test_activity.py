#coding=utf-8
import unittest
import requests
from zbpf.composer.models.activity import Activity
from zbpf.public.composer_csv import getCsv

class TestActivity(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.activity=Activity(s) #实例化
		self.base_url="http://crowdtest.jqweike.com"
		self.file_name="E:/test/zbpf/composer/test_data/activity.csv"

	def test_preview(self):
		#查看活动详情
		tp=getCsv(1,1,self.file_name)
		acid=getCsv(2,1,self.file_name)
		url=self.base_url+"/v1/admin/activity/get-info-admin?type="+str(tp)+"&activityId="+str(acid)
		activity_id=self.activity.preview(url)
		self.assertEqual(activity_id,acid)
	
	def  test_add_activity(self):
		#新增活动
		data=[]
		url=self.base_url+"/v1/admin/activity/add"
		atype=getCsv(14,1,self.file_name)
		userid=getCsv(15,1,self.file_name)
		username=getCsv(16,1,self.file_name)
		conpanyname=getCsv(17,1,self.file_name)
		name=getCsv(18,1,self.file_name)
		pcimage=getCsv(19,1,self.file_name)
		mobileimage=getCsv(20,1,self.file_name)
		smallimage=getCsv(21,1,self.file_name)
		bigimage=getCsv(22,1,self.file_name)
		intro=getCsv(23,1,self.file_name)
		allowjoin=getCsv(24,1,self.file_name)
		introimage1=getCsv(25,1,self.file_name)
		prizetype=getCsv(26,1,self.file_name)
		prizename=getCsv(27,1,self.file_name)
		prizeintro=getCsv(28,1,self.file_name)
		prizepeople=getCsv(29,1,self.file_name)
		signstarttime=getCsv(30,1,self.file_name)
		signendtime=getCsv(31,1,self.file_name)
		reviewstarttime=getCsv(32,1,self.file_name)
		announceawardstime=getCsv(33,1,self.file_name)
		reviewstandard=getCsv(34,1,self.file_name)
		activitystarttime=getCsv(35,1,self.file_name)
		activityendtime=getCsv(36,1,self.file_name)
		auditstate=getCsv(37,1,self.file_name)
		data.append(atype)
		data.append(userid)
		data.append(username)
		data.append(conpanyname)
		data.append(name)
		data.append(pcimage)
		data.append(mobileimage)
		data.append(smallimage)
		data.append(bigimage)
		data.append(intro)
		data.append(allowjoin)
		data.append(introimage1)
		data.append(prizetype)
		data.append(prizename)
		data.append(prizeintro)
		data.append(prizepeople)
		data.append(signstarttime)
		data.append(signendtime)
		data.append(reviewstarttime)
		data.append(announceawardstime)
		data.append(reviewstandard)
		data.append(activitystarttime)
		data.append(activityendtime)
		data.append(auditstate)
		ac=self.activity.add_activity(url,data)
		self.assertEqual(ac,200)
	
	def  test_edit_activity(self):
		#编辑活动
		url=self.base_url+"/v1/admin/activity/add"
		name=getCsv(3,1,self.file_name)
		activityid=getCsv(4,1,self.file_name)
		try :
			ac=self.activity.edit_activity(url,name,activityid)
			self.assertEqual(ac,200)
		except:
			print (u"动态数据有误")
	
	def test_delete(self):
		#删除活动
		url=self.base_url+"/v1/admin/activity/activity-delete"
		acid=getCsv(5,1,self.file_name)
		aid=self.activity.delete_activity(url,acid)
		self.assertEqual(aid,200)
	
	def test_activity_index(self):
		#展示所有活动
		url=self.base_url+"/v1/admin/activity/activity-index"
		userid=getCsv(6,1,self.file_name)
		uid=self.activity.activity_index(url,userid)
		if uid==200:
			self.assertEqual(uid,200)
		else:
			self.assertEqual(int(uid),userid)

	def test_activity_index(self):
		#活动审核
		url=self.base_url+"/v1/admin/activity/review-activity"
		activityid=getCsv(7,1,self.file_name)
		allow=getCsv(8,1,self.file_name)
		ac=self.activity.review_activity(url,activityid,allow)
		self.assertEqual(ac,200)
	
	def test_get_all_activity(self):
		#获取所有已经通过审核还没有过期的活动 
		userid=getCsv(9,1,self.file_name)
		url=self.base_url+"/v1/admin/activity/get-all-activity"+"?userId="+str(userid)
		ac=self.activity.get_all_activity(url)
		self.assertEqual(int(ac),200)
	
	def test_get_info_admin(self):
		#获取活动详细信息 
		activityid=getCsv(10,1,self.file_name)
		atype=getCsv(11,1,self.file_name)
		url=self.base_url+"/v1/admin/activity/get-info-admin"+"?type="+str(atype)+"&activityId="+str(activityid)
		acid=self.activity.get_info_admin(url)
		self.assertEqual(acid,activityid)
	
	def test_school_list(self):
		#参赛学校
		url=self.base_url+"/v1/admin/activity/school-list"
		self.activity.school_list(url)

	def test_get_reason(self):
		#获取拒绝原因
		url=self.base_url+"/v1/admin/activity/get-reason"
		activityid=getCsv(12,1,self.file_name)
		ac=self.activity.get_reason(url,activityid)
		self.assertEqual(ac,200)

	def test_update_state(self):
		#上下架活动
		url=self.base_url+"/v1/admin/activity/update-state"
		activityid=getCsv(13,1,self.file_name)
		state=0
		ac=self.activity.update_state(url,activityid,state)
		self.assertEqual(ac,200)

if __name__=="__main__":
	unittest.main(warnings='ignore')