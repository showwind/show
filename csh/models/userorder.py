#coding=utf-8
import requests
import unittest,json

class UserOrder():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def userorder_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def order_income(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']
	def order_detail(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def order_class(self,url,data):
		body={
		"token":data[0],
		"courseId":data[1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def order_course(self,url,data):
		body={
		"token":data[0],
		"courseId":data[1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']
	def order_cancel(self,url,data):
		body={
		"token":data[0],
		"orderId":data[1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def order_success(self,url,data):
		body={
		"token":data[0],
		"orderId":data[1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']
