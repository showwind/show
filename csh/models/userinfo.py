#coding=utf-8
import requests
import unittest,json

class UserInfo():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def get_userrelate(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def user_sendemailcode(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def user_sendmobilecode(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def bindmobile(self,url,data):
		body={
		"token":data[0],
		"email":data[1],
		"captcha":data[2]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def reset_password(self,url,data):
		body={
		"token":data[0],
		"oldPassword":data[1],
		"newPassword":data[2],
		"rePassword":data[3]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']
	
	def update_userinfo(self,url,data):
		body={
		"token":data[0],
		"job":data[1],
		"subject":data[2],
		"imagePath":data[3],
		"username":data[4],
		"agencyId":data[5]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def update_userimage(self,url,data):
		body={
		"token":data[0],
		"bigImage":data[1],
		"middleImage":data[2],
		"smallImage":data[3]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']
	def user_behavior(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']
