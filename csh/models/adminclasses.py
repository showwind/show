#coding=utf-8
import requests
import unittest,json

class AdminClasses():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def classes_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def classes_view(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def classes_onself(self,url,data):
		body={
		"token":data[0],
		"classId":data[1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def student_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']
	
	def add_student(self,url,data):
		body={
		"token":data[0],
		"classId":data[1],
		"userId[0]":data[2]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def delete_student(self,url,data):
		body={
		"token":data[0]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']