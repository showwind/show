#coding=utf-8
import requests

def login(s,url,username,password):
	'''登录接口'''
	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
	}
	body={
	"username":username,
	"password":password
	}
	r=s.post(url,data=body,headers=headers,verify=False)
	result=r.json()
	data=result['data']
	userinfo=data['user']
	print (userinfo)
	return userinfo['username']