#coding=utf-8
import requests
import unittest,json

class Uindex():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def category_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	
	def software_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def allsoft(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def get_activity(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def get_runkcourses(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def market_banners(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']