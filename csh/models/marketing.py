#coding=utf-8
import requests
import unittest,json

class Marketing():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def marketing_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def create_marketing(self,url,data):
		body={
		"token":data[0],
		"marketTitle":data[1],
		"marketType":data[2],
		"startTime":data[3],
		"endTime":data[4],
		"courseIds":data[5],
		"userId":data[6],
		"userName":data[7],
		"marketPrice":data[8],
		"discount":data[9],
		"integral":data[10]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def delete_marketing(self,url,token):
		body={
		"token":token
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def marketing_view(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']
