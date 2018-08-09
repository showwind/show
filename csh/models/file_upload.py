#coding=utf-8
import requests
import unittest,json

class FileUpload():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def upload_resourse(self,url,data):
		body={
		"courseId":data[0],
		"file":data[1]
		}
		file ={'file':open(data[2],'rb')}
		r=self.s.post(url,data=body,headers=self.headers,verify=False,files=file)
		result=r.json()
		#print (result)
		return result['status']

	def upload_pic(self,url,data):
		body={
		"file":data[0]
		}
		file ={'file':open(data[1],'rb')}
		r=self.s.post(url,data=body,headers=self.headers,verify=False,files=file)
		result=r.json()
		#print (result)
		return result['status']