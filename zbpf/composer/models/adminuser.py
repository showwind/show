#coding=utf-8
import requests
from zbpf.public import composer_login
import unittest,json

class AdminUser():
	def __init__(self,s):
		self.s=s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def user_info(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def user_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def agency_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def add_user(self,url,data):
		body={
		"username":data[0],
		"realName":data[1],
		"agencyId":data[2],
		"password":data[3],
		"checkPsd":data[3],
		"company":data[4],
		"department":data[5],
		"role":data[6],
		"agency[label]":data[2],
		"departments":data[5]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def update_user(self,url,data):
		body={
		"username":data[0],
		"realName":data[1],
		"agencyId":data[2],
		"company":data[3],
		"department":data[4],
		"role":data[5],
		"departments":data[4],
		"userId":data[6],
		"access_token":data[7],
		"bigImage":data[8],
		"smallImage":data[9],
		"signTime":data[10],
		"id":data[6],
		"agency":data[3]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def delete_user(self,url,userid):
		body={
		"userId[0]":userid
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def role_list(self,url):
		body={
		"desc":0
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def get_all_roles(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def get_all_premission(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	
	def reset_password(self,url,userid):
		body={
		"userId":userid
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def modify_password(self,url,data):
		body={
		"userId":data[0],
		"oldpass":data[1],
		"password":data[2],
		"repass":data[3]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def side_bar(self,url,userid):
		body={
		"userId":userid
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def add_premission(self,url,data):
		body={
		"role":data[0],
		"description":data[1],
		"permission":"activity/activity-index,activity/get-all-activity,activity/viewAllActivity,activity/viewAllWorks",
		"secondPermission":data[3],
		}
		'''
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']
		'''