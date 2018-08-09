#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.invite import Invite

class TestInvite(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.invite=Invite(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/invite.csv"

	def test_agency_list(self):
		#机构列表
		token=getCsv(0,1,self.filename)
		keyword=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/admin/agency/schoolLists"+"?token="+token+"&keyword="+keyword+"&per-page=10&page=1&area="
		ac=self.invite.agency_list(url)
		self.assertEqual(ac,200)
	
	def test_agency_schoolarea(self):
		#地区
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/admin/agency/schoolArea"+"?token="+token
		ac=self.invite.agency_schoolarea(url)
		self.assertEqual(ac,200)
	
	def test_edit_invite(self):
		#修改邀请码
		token=getCsv(0,1,self.filename)
		ispack=getCsv(2,1,self.filename)
		codeid=getCsv(3,1,self.filename)
		agencyids=[1,3]
		courseids=[275,280]
		data=[[]]
		data.append(token)
		data.append(ispack)
		data.append(codeid)
		data.append(agencyids)
		data.append(courseids)
		url=self.base_url+"/v1/admin/invite/edit"
		ac=self.invite.edit_invite(url,data)
		self.assertEqual(ac,200)
	
	def test_add_invite(self):
		#新增邀请码
		token=getCsv(0,1,self.filename)
		ispack=getCsv(6,1,self.filename)
		checkbox=getCsv(7,1,self.filename)
		agencyids=[1,3]
		courseids=[275,280]
		data=[[]] #二维数组
		data.append(token)
		data.append(ispack)
		data.append(checkbox)
		data.append(agencyids)
		data.append(courseids)
		url=self.base_url+"/v1/admin/invite/add"
		ac=self.invite.add_invite(url,data)
		self.assertEqual(ac,200)
	
	def test_invite_update(self):
		#修改邀请码状态
		token=getCsv(0,1,self.filename)
		status=getCsv(8,1,self.filename)
		uid=getCsv(9,1,self.filename)
		data=[]
		data.append(token)
		data.append(status)
		url=self.base_url+"/v1/admin/invite/update/"+uid
		ac=self.invite.invite_update(url,data)
		self.assertEqual(ac,200)
	
	def test_invite_detail(self):
		#邀请码详情
		token=getCsv(0,1,self.filename)
		codeid=getCsv(10,1,self.filename)
		url=self.base_url+"/v1/admin/invite/detail"+"?token="+token+"&codeId="+codeid
		ac=self.invite.invite_detail(url)
		self.assertEqual(ac,200)
	
	def test_invite_lists(self):
		#邀请码列表
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/admin/invite/lists"+"?token="+token+"&page=1&per-page=10"
		ac=self.invite.invite_lists(url)
		self.assertEqual(ac,200)
		
	def test_invite_getcourse(self):
		#前台邀请码获取课程
		token=getCsv(11,1,self.filename)
		url="http://cshapi.jqweike.com/v1/frontend/invite/getCourses"+"?token="+token
		ac=self.invite.invite_getcourse(url)
		self.assertEqual(ac,200)
	
	def test_invite_bindcode(self):
		#前台绑定邀请码
		token=getCsv(11,1,self.filename)
		code=getCsv(12,1,self.filename)
		data=[]
		data.append(token)
		data.append(code)
		url="http://cshapi.jqweike.com/v1/frontend/invite/bindCode"
		ac=self.invite.invite_bindcode(url,data)
		self.assertEqual(ac,200)
		
	def test_agency_lists(self):
		#机构列表
		token=getCsv(11,1,self.filename)
		url="http://cshapi.jqweike.com/v1/frontend/agency/lists"+"?token="+token
		ac=self.invite.agency_lists(url)
		self.assertEqual(ac,200)

	def test_add_agency(self):
		#立即荐购
		token=getCsv(11,1,self.filename)
		phone=getCsv(13,1,self.filename)
		studentid=getCsv(14,1,self.filename)
		realname=getCsv(15,1,self.filename)
		department=getCsv(16,1,self.filename)
		agencyname=getCsv(17,1,self.filename)
		primaryid=getCsv(18,1,self.filename)
		atype=getCsv(19,1,self.filename)
		data=[]
		data.append(token)
		data.append(phone)
		data.append(studentid)
		data.append(realname)
		data.append(department)
		data.append(agencyname)
		data.append(primaryid)
		data.append(atype)
		url="http://cshapi.jqweike.com/v1/frontend/agency/add"
		ac=self.invite.add_agency(url,data)
		self.assertEqual(ac,200)
if __name__ == '__main__':
	unittest.main(warnings='ignore')