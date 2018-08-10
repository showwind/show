#coding=utf-8
import requests
from zbpf.public import composer_login
import unittest,json

class News():
	def __init__(self,s):
		self.s=s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def login(self,url,username,password):
		usern=composer_login.login(self.s,url,username,password)
		return usern

	def get_news(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		data=result['data']
		return data['id']

	def add_news(self,url,data):
		body={
		"title":data[0],
		"activityId":data[1],
		"newsSummary":data[2],
		"userId":data[7],
		"username":data[6],
		"coverPath":data[4],
		"mainBody":data[5],
		"name":data[3],
		"headImage":data[8],
		"status":data[9],
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	
	def modify_news(self,url,data):
		body={
		"title":data[0],
		"activityId":data[1],
		"newsSummary":data[2],
		"userId":data[7],
		"username":data[6],
		"coverPath":data[4],
		"mainBody":data[5],
		"name":data[3],
		"newsId":data[8],
		"headImage":data[9],
		"status":data[10],
		"publishTime":data[11],
		"id":data[8]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def view_news(self,url,data):
		body={
		"page":data[0],
		"pageSize":data[1],
		"condition[activityId]":data[2],
		"condition[userId]":data[3]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def delete_news(self,url,newsid):
		body={
		"newsId[0]":newsid
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']