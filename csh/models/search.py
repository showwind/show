#coding=utf-8
import requests
import unittest,json

class Search():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def search_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def search_history(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def clear_search(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']