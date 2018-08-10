#coding=utf-8
import requests
import unittest,json

class Invite():
	def __init__(self, s):
		self.s = s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def agency_list(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def agency_schoolarea(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def edit_invite(self,url,data):
		body={
		"token":data[1],
		"isPack":data[2],
		"codeId":data[3],
		"agencyIds[0]":data[3][0],
		"agencyIds[1]":data[3][1],
		"courseIds[0]":data[4][0],
		"courseIds[1]":data[4][1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def add_invite(self,url,data):
		body={
		"token":data[1],
		"isPack":data[2],
		"checkBox[0]":data[3],
		"agencyIds[0]":data[4][0],
		"agencyIds[1]":data[4][1],
		"courseIds[0]":data[5][0],
		"courseIds[1]":data[5][1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def invite_update(self,url,data):
		body={
		"token":data[0],
		"status":data[1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']
	def invite_detail(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']
	
	def invite_lists(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def invite_getcourse(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def invite_bindcode(self,url,data):
		body={
		"token":data[0],
		"code":data[1]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def agency_lists(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def add_agency(self,url,data):
		body={
		"token":data[0],
		"phone":data[1],
		"studentId":data[2],
		"realName":data[3],
		"department":data[4],
		"agencyName":data[5],
		"primaryId":data[6],
		"type":data[7]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']