#coding=utf-8
import requests
import unittest,json

class Classes():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def class_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def user_class(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	def join_class(self,url,classid,token):
		body={
		"classId":classid,
		"token":token
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def view_class(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def recommend_classes(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def update_classes(self,url,status,token):
		body={
		"status":status,
		"token":token
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']