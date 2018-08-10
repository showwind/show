#coding=utf-8
import requests
import unittest,json

class MarketPostion():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def marketpostion_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def create_marketpostion(self,url,data):
		body={
		"token":data[0],
		"title":data[1],
		"introduce":data[2],
		"courseIds":data[3],
		"number":data[4],
		"way":data[5],
		"coverImage":data[6],
		"detailCover":data[7],
		"startTime":data[8],
		"endTime":data[9],
		"userId":data[10],
		"userName":data[11]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']
	def update_marketpostion(self,url,data):
		body={
		"token":data[0],
		"title":data[1],
		"introduce":data[2],
		"courseIds":data[3],
		"number":data[4],
		"way":data[5],
		"coverImage":data[6],
		"detailCover":data[7],
		"startTime":data[8],
		"endTime":data[9],
		"userId":data[10],
		"userName":data[11]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']
