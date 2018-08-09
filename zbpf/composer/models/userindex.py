#coding=utf-8
import unittest,json

class UserIndex():
	def __init__(self,s):
		self.s=s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers
	
	def get_user_info(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']

	def get_picture(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def get_activity(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	
	def get_activity_info(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def get_news(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def sign_up(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def add_hits(self,url,data):
		body={
		"workId":data[1],
		"userId":data[0],
		"token":data[2]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def get_runk(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	
	def news_info(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def user_score(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	
	def type_lists(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def get_work_info(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	
	def end_time(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def add_share(self,url,data):
		body={
		"workId":data[0],
		"userId":data[1],
		"token":data[2]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	
	def user_work(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']

	def work_file(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def file_upload(self,url,data):
		
		body={
		"userId":data[0],
		"file":data[1],
		"lastModifiedDate":data[2],
		"totalSize":data[3],
		"activityId":data[4],
		"lastModifiedTime":data[5]
		}
		file ={'file':open('E:\\test\\zbpf\\tupian.zip','rb')}
		'''
		files={
		'userId':(None,data[0]),
		'lastModifiedDate':(None,data[2]),
		'totalSize':(None,data[3]),
		'activityId':(None,data[4]),
		"lastModifiedTime":(None,data[5]),
		'file':(data[1],open('E:\\test\\zbpf\\tupian.zip','rb'),'multipart/form-data')
		}
		'''
		r=self.s.post(url,headers=self.headers,verify=False,data=body,files=file)
		result=r.json()
		print(result)
		return result['status']
	
	def file_progress(self,url,data):
		body={
		"userId":data[0],
		"activityId":data[1],
		"clientName":data[2],
		"totalSize":data[3],
		"uploadSize":data[4],
		"lastModifiedTime":data[5]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print(result)
		return result['status']

	def remove_file(self,url,data):
		body={
		"userId":data[0],
		"activityId":data[1],
		"totalSize":data[2],
		"lastModifiedTime":data[3]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def add_work(self,url,data):
		body={
		"activityId":data[0],
		"workName":data[1],
		"username":data[2],
		"userId":data[3],
		"type":data[4],
		"file":data[5],
		"tel":data[6],
		"departments":data[7],
		"studentId":data[8],
		"division":data[9],
		"lastModifiedTime":data[10],
		"token":data[11]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print(result)
		return result['status']

	def get_all_upload_files(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def record_click(self,url,data):
		body={
		"fileId":data[0],
		"type":data[1],
		"token":data[2]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print(result)
		return result['status']