#coding=utf-8
import unittest
import requests
from zbpf.composer.models.adminuser import AdminUser
from zbpf.public.composer_csv import getCsv

class TestAdminUser(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.adminuser=AdminUser(s) #实例化
		self.base_url="http://crowdtest.jqweike.com"
		self.file_name="E:/test/zbpf/composer/test_data/adminuser.csv"
	
	def test_user_info(self):
		#用户详情
		userid=getCsv(1,1,self.file_name)
		url=self.base_url+"/v1/admin/user/info"+"?userId="+userid
		ac=self.adminuser.user_info(url)
		self.assertEqual(ac,200)

	def test_user_list(self):
		#用户列表
		agencyid=getCsv(2,1,self.file_name)
		url=self.base_url+"/v1/admin/user/list"+"?agencyId="+agencyid+"&keyword=&pageSize=10&page=1"
		ac=self.adminuser.user_list(url)
		self.assertEqual(ac,200)

	def test_user_research(self):
		#搜素功能
		agencyid=getCsv(2,1,self.file_name)
		keyword=getCsv(3,1,self.file_name) 
		url=self.base_url+"/v1/admin/user/list"+"?agencyId="+agencyid+"&keyword="+keyword+"&pageSize=10&page=1"
		ac=self.adminuser.user_list(url)
		self.assertEqual(ac,200)

	def test_agency_list(self):
		url=self.base_url+"/v1/admin/user/agency-list"
		ac=self.adminuser.agency_list(url)
		self.assertEqual(ac,200)
		
	def test_add_user(self):
		#新增用户
		data=[]
		username=getCsv(4,1,self.file_name)
		realname=getCsv(5,1,self.file_name)
		agencyid=getCsv(6,1,self.file_name)
		password=getCsv(7,1,self.file_name)
		company=getCsv(8,1,self.file_name)
		department=getCsv(9,1,self.file_name)
		role=getCsv(10,1,self.file_name)
		data.append(username)
		data.append(realname)
		data.append(agencyid)
		data.append(password)
		data.append(company)
		data.append(department)
		data.append(role)
		url=self.base_url+"/v1/admin/user/create"
		ac=self.adminuser.add_user(url,data)
		self.assertEqual(ac,200)
	
	def test_update_user(self):
		#编辑用户
		data=[]
		username=getCsv(4,1,self.file_name)
		realname=getCsv(5,1,self.file_name)
		agencyid=getCsv(6,1,self.file_name)
		company=getCsv(8,1,self.file_name)
		department=getCsv(9,1,self.file_name)
		role=getCsv(10,1,self.file_name)
		userid=getCsv(11,1,self.file_name)
		access_token=getCsv(12,1,self.file_name)
		bigImage=getCsv(13,1,self.file_name)
		smallImage=getCsv(14,1,self.file_name)
		signTime=getCsv(15,1,self.file_name)
		data.append(username)
		data.append(realname)
		data.append(agencyid)
		data.append(company)
		data.append(department)
		data.append(role)
		data.append(userid)
		data.append(access_token)
		data.append(bigImage)
		data.append(smallImage)
		data.append(signTime)
		url=self.base_url+"/v1/admin/user/create"
		ac=self.adminuser.update_user(url,data)
		self.assertEqual(ac,200)
		
	def test_delete_user(self):
		#删除用户
		userid=getCsv(16,1,self.file_name)
		url=self.base_url+"/v1/admin/user/delete"
		ac=self.adminuser.delete_user(url,userid)
		self.assertEqual(ac,200)

	def test_role_list(self):
		#角色列表
		role=getCsv(17,1,self.file_name)
		url=self.base_url+"/v1/admin/permission/get-permission-and-role-list"
		ac=self.adminuser.role_list(url)
		self.assertEqual(ac,200)
	
	def test_get_all_roles(self):
		#获取所有角色
		url=self.base_url+"/v1/admin/permission/get-all-roles"
		ac=self.adminuser.get_all_roles(url)
		self.assertEqual(ac,200)

	def test_get_all_premission(self):
		#获取所有权限
		url=self.base_url+"/v1/admin/permission/get-all-permission"
		ac=self.adminuser.get_all_premission(url)
		self.assertEqual(ac,200)
	
	def test_reset_password(self):
		#重置密码
		userid=getCsv(18,1,self.file_name)
		url=self.base_url+"/v1/admin/user/reset-password"
		ac=self.adminuser.reset_password(url,userid)
		self.assertEqual(ac,200)
	
	def test_modify_password(self):
		#修改密码
		data=[]
		userid=getCsv(19,1,self.file_name)
		oldpass=getCsv(20,1,self.file_name)
		password=getCsv(21,1,self.file_name)
		repass=getCsv(22,1,self.file_name)
		data.append(userid)
		data.append(oldpass)
		data.append(password)
		data.append(repass)
		url=self.base_url+"/v1/admin/user/modify-password"
		ac=self.adminuser.modify_password(url,data)
		self.assertEqual(ac,200)
	
	def test_side_bar(self):
		#后台侧边栏
		userid=getCsv(23,1,self.file_name)
		url=self.base_url+"/v1/admin/permission/get-sider-bar"
		ac=self.adminuser.side_bar(url,userid)
		self.assertEqual(ac,200)
	
	def test_add_premission(self):
		#给角色分配权限
		data=[]
		role=getCsv(24,1,self.file_name)
		description=getCsv(25,1,self.file_name)
		permission=getCsv(26,1,self.file_name)
		secondPermission=getCsv(27,1,self.file_name)
		data.append(role)
		data.append(description)
		data.append(permission)
		data.append(secondPermission)
		url=self.base_url+"/v1/admin/permission/add-permissions-for-role"
		self.adminuser.add_premission(url,data)
if __name__ == '__main__':
	unittest.main(warnings='ignore')