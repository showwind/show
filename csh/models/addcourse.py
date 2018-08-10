#coding=utf-8
import requests
import unittest,json

class AddCourse():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def add_course(self,url,data):
		body={
		"courseName":data[1],
		"parentName":data[2],
		"parentNumber":data[3],
		"cateName":data[4],
		"cateNumber":data[5],
		"softNumber":data[6],
		"softName":data[7],
		"softVersion":data[8],
		"price":data[9],
		"intro":data[10],
		"cover":data[11],
		"level":data[12],
		"token":data[0]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def create_chapter(self,url,data):
		body={
		"token":data[0],
		"chapterName":data[1],
		"courseId":data[2],
		"type":data[3],
		"parentId":data[4]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def delete_chapter(self,url,data):
		body={
		"token":data[2],
		"chapterId":data[0],
		"parentId":data[1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def add_intro(self,url,data):
		body={
		"intro":data[0],
		"token":data[1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def add_view(self,url,data):
		body={
		"videoName":data[0],
		"videoPath":data[1],
		"videoType":data[2],
		"chapterId":data[3],
		"token":data[4]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def update_info(self,url,data):
		body={
		"intro":data[1],
		"token":data[0]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def add_question(self,url,data):
		body={
		"chapterId":data[1],
		"content":data[2],
		"questionType":data[3],
		"scene":data[4],
		"answers[0][content]":data[5],
		"answers[0][options]":data[6],
		"answers[0][status]":data[7],
		"token":data[0],
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def delete_question(self,url,data):
		body={
		"token":data[0]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def create_resource(self,url,data):
		body={
		"token":data[0],
		"resourceName":data[1],
		"path":data[2],
		"fileType":data[3],
		"chapterId":data[4]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def delete_resource(self,url,token):
		body={
		"token":token
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def section_view(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	
	def update_course(self,url,data):
		body={
		"chapterIds[0]":data[3],
		"courseId":data[1],
		"status":data[2],
		"token":data[0]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def course_detail(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def question_detail(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def chapter_info(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']