#coding=utf-8
import requests
from zbpf.public import composer_login
import unittest,json

class MyActivity():

	def __init__(self,s):
		self.s=s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def login(self,url,username,password):
		usern=composer_login.login(self.s,url,username,password)
		return usern
	
	def works_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		data=result['data']
		rows=data['rows']
		total=data['total']
		if int(total)==0:
			return result['status']
		else:
			data1=rows[0]['activityId']
			return data1
	def work_info(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		data=result['data']
		acid=data['id']
		return acid
	
	def work_audit(self,url,workid,status,activityid):
		body={
		"workId[0]":workid,
		"status":status,
		"activityId":activityid
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result['status'])
		return result['status']

	def active_prize(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def set_prize(self,url,workid,prizeid):
		body={
		"workId":workid,
		"prizeId":prizeid
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def prize_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		data=result['data']
		rows=data['rows']
		total=data['total']
		if int(total)==0:
			return result['status']
		else:
			data1=rows[0]['activityId']
			return data1
	
	def work_type(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		data=result['data']
		n=len(data)
		if n!=0:
			dtype=data[0]['type']
			return dtype
		else:
			return result['status']

if __name__=="__main__":
	'''
	#测试登录接口
	url="http://crowdtest.jqweike.com/v1/admin/site/login"
	s=requests.session()
	username="susiku"
	password="123456"
	Login(s).login(url,username,password)
	'''



