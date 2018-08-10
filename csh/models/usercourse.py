#coding=utf-8
import requests
import unittest,json

class UserCourse():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def course_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def course_detail(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def user_course(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def user_course_collection(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def course_learn(self,url,data):
		body={
		"token":data[0],
		"courseId":data[1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def teacher_course(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def knowledge_cloud(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def market_hot(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def get_chaptersource(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def course_recommend(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def course_updateshelf(self,url,data):
		body={
		"token":data[0],
		"courseId":data[1],
		"onShelf":data[2]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print(result)
		return result['status']

	def delete_course(self,url,data):
		body={
		"token":data[0],
		"courseId":data[1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	
	def course_teacher(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	def study_progress(self,url,data):
		body={
		"token":data[0],
		"sourceId":data[1],
		"learnLength":data[2],
		"classId":data[3]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']
	def section_view(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']