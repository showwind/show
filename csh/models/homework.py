#coding=utf-8
import requests
import unittest,json

class HomeWork():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def homework_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def work_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def create_homework(self,url,data):
		body={
		"token":data[0],
		"classId":data[1],
		"workName":data[2],
		"require":data[3],
		"sectionName":data[4],
		"sectionId":data[5],
		"endTime":data[6]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']
	def delete_homework(self,url,token):
		body={
		"token":token
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def update_homework(self,url,data):
		body={
		"token":data[0],
		"teacherComment":data[1],
		"checkPath":data[2],
		"score":data[3],
		"state":data[4]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']
	def submit_homework(self,url,data):
		body={
		"token":data[0],
		"classId":data[1],
		"workId":data[2],
		"content":data[3],
		"attachment":data[4]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def homework_listbyclass(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def homework_listbywork(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']