#coding=utf-8
import requests
import unittest,json

class Note():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def note_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def add_note(self,url,data):
		body={
		"token":data[0],
		"content":data[1],
		"courseId":data[2],
		"chapterId":data[3],
		"chapterName":data[4]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def delete_note(self,url,token):
		body={
		"token":token
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def update_note(self,url,token,content):
		body={
		"token":token,
		"content":content
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
