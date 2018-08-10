#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.userinfo import UserInfo

class TestUserInfo(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.userinfo=UserInfo(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/userinfo.csv"
	
	def test_get_userrelate(self):
		#用户学习时长
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/user/getUserRelate"+"?token="+token
		ac=self.userinfo.get_userrelate(url)
		self.assertEqual(ac,200)
	
	def test_user_sendemailcode(self):
		#发送邮箱验证码
		token=getCsv(0,1,self.filename)
		email=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/frontend/user/sendEmailCode"+"?email="+email+"&token="+token
		self.userinfo.user_sendemailcode(url)
	
	def test_user_sendmobilecode(self):
		#发送手机证码
		token=getCsv(0,1,self.filename)
		mobile=getCsv(2,1,self.filename)
		url=self.base_url+"/v1/frontend/user/sendMobileCode"+"?mobile="+mobile+"&token="+token
		self.userinfo.user_sendmobilecode(url)
		
	def test_bindmobile(self):
		#绑定手机
		token=getCsv(0,1,self.filename)
		mobile=getCsv(2,1,self.filename)
		captcha=getCsv(3,1,self.filename)
		data=[]
		data.append(token)
		data.append(mobile)
		data.append(captcha)
		url=self.base_url+"/v1/frontend/user/bindMobile"
		self.userinfo.bindmobile(url,data)
	
	def test_bindemail(self):
		#绑定手机
		token=getCsv(0,1,self.filename)
		email=getCsv(4,1,self.filename)
		captcha=getCsv(5,1,self.filename)
		data=[]
		data.append(token)
		data.append(email)
		data.append(captcha)
		url=self.base_url+"/v1/frontend/user/bindEmail"
		self.userinfo.bindmobile(url,data)
		
	def test_reset_password(self):
		#修改密码
		data=[]
		token=getCsv(0,1,self.filename)
		oldpass=getCsv(6,1,self.filename)
		password=getCsv(7,1,self.filename)
		repass=getCsv(8,1,self.filename)
		data.append(token)
		data.append(oldpass)
		data.append(password)
		data.append(repass)
		url=self.base_url+"/v1/frontend/user/resetPassword"
		ac=self.userinfo.reset_password(url,data)
		self.assertEqual(ac,200)
	
	def test_update_userinfo(self):
		data=[]
		token=getCsv(0,1,self.filename)
		job=getCsv(9,1,self.filename)
		subject=getCsv(10,1,self.filename)
		imagepath=getCsv(11,1,self.filename)
		username=getCsv(12,1,self.filename)
		agencyid=getCsv(13,1,self.filename)
		data.append(token)
		data.append(job)
		data.append(subject)
		data.append(imagepath)
		data.append(username)
		data.append(agencyid)
		url=self.base_url+"/v1/frontend/user/updateInfo"
		ac=self.userinfo.update_userinfo(url,data)
		self.assertEqual(ac,200)
	
	def test_update_userimage(self):
		#修改用户头像(没用)
		data=[]
		token=getCsv(0,1,self.filename)
		bigimage=getCsv(14,1,self.filename)
		middleimage=getCsv(15,1,self.filename)
		smallimage=getCsv(16,1,self.filename)
		data.append(token)
		data.append(bigimage)
		data.append(middleimage)
		data.append(smallimage)
		url=self.base_url+"/v1/frontend/user/updateUserImage"
		self.userinfo.update_userimage(url,data)

	def test_user_behavior(self):
		#用户动态
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/behavior"+"?token="+token
		self.userinfo.user_behavior(url)
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')
