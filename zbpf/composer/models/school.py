#coding=utf-8
from zbpf.public import composer_login
import unittest,json

class School():
	def __init__(self,s):
		self.s=s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers
	
	def login(self,url,username,password):
		usern=composer_login.login(self.s,url,username,password)
		return usern

	def province_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def school_list(self,url,data):
		body={
		"area":data[0],
		"pageSize":data[1],
		"page":data[2]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

