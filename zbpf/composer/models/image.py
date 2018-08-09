#coding=utf-8
from zbpf.public import composer_login
import unittest,json

class Image():
	def __init__(self,s):
		self.s=s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers
	
	def save_activity_banner_image(self,url,data):
		body={
		"file":data[0],
		"request":data[1],
		"toCropImgX":data[2],
		"toCropImgY":data[3],
		"toCropImgW":data[4],
		"toCropImgH":data[5],
		"maxWidth":data[6],
		"maxHeight":data[7],
		"minWidth":data[8],
		"comprose":data[9]
		}
		file ={'file':open(data[10],'rb')}
		r=self.s.post(url,data=body,headers=self.headers,verify=False,files=file)
		result=r.json()
		#print (result)
		return result['status']
	def save_activity_small_image(self,url,data):
		body={
		"file":data[0],
		"request":data[1],
		"toCropImgX":data[2],
		"toCropImgY":data[3],
		"toCropImgW":data[4],
		"toCropImgH":data[5],
		"maxWidth":data[6],
		"maxHeight":data[7],
		"minWidth":data[8],
		"comprose":data[9]
		}
		file ={'file':open(data[10],'rb')}
		r=self.s.post(url,data=body,headers=self.headers,verify=False,files=file)
		result=r.json()
		#print (result)
		return result['status']

	def save_activity_intro_image(self,url,data):
		body={
		"file":data[0],
		"request":data[1],
		"toCropImgX":data[2],
		"toCropImgY":data[3],
		"toCropImgW":data[4],
		"toCropImgH":data[5],
		"maxWidth":data[6],
		"maxHeight":data[7],
		"minWidth":data[8],
		"comprose":data[9]
		}
		file ={'file':open(data[10],'rb')}
		r=self.s.post(url,data=body,headers=self.headers,verify=False,files=file)
		result=r.json()
		print (result)
		return result['status']

	def save_news_cover_image(self,url,data):
		body={
		"file":data[0],
		"request":data[1],
		"toCropImgX":data[2],
		"toCropImgY":data[3],
		"toCropImgW":data[4],
		"toCropImgH":data[5],
		"maxWidth":data[6],
		"maxHeight":data[7],
		"minWidth":data[8],
		"comprose":data[9]
		}
		file ={'file':open(data[10],'rb')}
		r=self.s.post(url,data=body,headers=self.headers,verify=False,files=file)
		result=r.json()
		print (result)
		return result['status']

	def upload_cover_image(self,url,data):
		body={
		"workId":data[0],
		"coverPath":data[1],
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']