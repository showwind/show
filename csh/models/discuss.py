#coding=utf-8
import requests
import unittest,json

class Discuss():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def discuss_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def create_discuss(self,url,data):
		body={
		"token":data[0],
		"courseId":data[1],
		"content":data[2],
		"classId":data[3],
		"type":data[4]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def comment_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def create_comment(self,url,data):
		body={
		"token":data[0],
		"courseId":data[1],
		"content":data[2]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']