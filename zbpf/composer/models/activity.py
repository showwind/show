#coding=utf-8
import requests
from zbpf.public import composer_login
import unittest,json

class Activity():

	def __init__(self,s):
		self.s=s
		headers={
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
		}
		self.headers=headers

	def login(self,url,username,password):
		usern=composer_login.login(self.s,url,username,password)
		return usern
	
	def preview(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		data=result["data"]
		acinfo=data['activity']
		acid=acinfo['id']
		return acid
	def add_activity(self,url,data):
		body={
		"type":data[0],
		"userId":data[1],
		"userName":data[2],
		"companyName":data[3],
		"name":data[4],
		"pcImage":data[5],
		"mobileImage":data[6],
		"smallImage":data[7],
		"bigImage":data[8],
		"intro":data[9],
		"allowJoin":data[10],
		"introImage[0][introImage]":data[11],
		"prize[0][type]":data[12],
		"prize[0][prizeName]":data[13],
		"prize[0][prizeIntro]":data[14],
		"prize[0][totalPeople]":data[15],
		"activityTime[0][type]":data[12],
		"activityTime[0][signStartTime]":data[16],
		"activityTime[0][signEndTime]":data[17],
		"activityTime[0][reviewStartTime]":data[18],
		"activityTime[0][announceAwardsTime]":data[19],
		"reviewStandard":data[20],
		"activityStartTime":data[21],
		"activityEndTime":data[22],
		"auditState":data[23]
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		print (result)
		return result['status']
	
	def edit_activity(self,url,name,activityid):
		body={
		"type":1,
		"userId":58,
		"userName":"susiku",
		"companyName":"中新金桥",
		"name":name,
		"pcImage":"/data/activityImage/banner/2018-07-04/1530676245901.jpg",
		"mobileImage":"/data/activityImage/banner/2018-07-04/thumb_1530676245901.jpg",
		"smallImage":"/data/activityImage/small/2018-07-04/thumb_1530676247165.jpg",
		"bigImage":"/data/activityImage/small/2018-07-04/1530676247165.jpg",
		"intro":"测试简历",
		"introImage[0][id]":818, #动态数据
		"introImage[0][activityId]":activityid,
		"introImage[0][introImage]":"/data/activityImage/intro/2018-07-04/thumb_1530676249927.jpg",
		"allowJoin":1,
		"prize[0][id]":931, #动态数据
		"prize[0][activityId]":activityid,
		"prize[0][prizeName]":"一等奖",
		"prize[0][prizeIntro]":"一等奖介绍",
		"prize[0][totalPeople]":10,
		"prize[0][winners]":0,
		"prize[0][type]":"风景",
		"activityTime[0][announceAwardsTime]":1548345600000,
		"activityTime[0][reviewStartTime]":1546012800000,
		"activityTime[0][signEndTime]":1545667200000,
		"activityTime[0][signStartTime]":1529856000000,
		"activityTime[0][type]":"风景",
		"reviewStandard":"大赛简介",
		"activityStartTime":1529856000000,
		"activityEndTime":1548691200000,
		#"questionAnswerDetail":
		"id":activityid,
		"auditState":4,
		"status":1,
		"activityId":activityid
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return result['status']
	
	def delete_activity(self,url,acid):
		json={"activityId":acid}
		r=self.s.post(url,json=json,headers=self.headers,verify=False)
		result=r.json()
		return result['status']
	
	def activity_index(self,url,userid):
		body={
		"page":1,
		"pageSize":10,
		"condition[type]":0,
		"condition[auditState]":0,
		"condition[status]":0,
		"userId":userid}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		data=result['data']
		rows=data['rows']
		total=data['total']
		if int(total)==0:
			return result['status']
		else:
			data1=rows[0]['userId']
			return data1
	def review_activity(self,url,activityid,allow):
		body={
		"activityId":activityid,
		"allow":allow
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def get_all_activity(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		return result['status']

	def get_info_admin(self,url):
		r=self.s.get(url,headers=self.headers,verify=False)
		result=r.json()
		data=result['data']
		activity=data['activity']
		acid=activity['id']
		return acid

	def school_list(self,url):
		body={
		"area":0,
		"pageSize":10,
		"page":1
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return  result['status']

	def get_reason(self,url,activityid):
		body={
		"activityId":activityid
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		return  result['status']

	def update_state(self,url,activityid,state):
		body={
		"activityId":activityid,
		"state":state
		}
		r=self.s.post(url,data=body,headers=self.headers,verify=False)
		result=r.json()
		#print (result)
		return  result['status']

if __name__=="__main__":
	'''
	#测试登录接口
	url="http://crowdtest.jqweike.com/v1/admin/site/login"
	s=requests.session()
	username="susiku"
	password="123456"
	Login(s).login(url,username,password)
	'''

