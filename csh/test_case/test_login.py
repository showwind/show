#coding=utf-8
import requests
from csh.public import composer_login
import unittest

class Test():

	def __init__(self,s):
		self.s=s

	def login(self,url,username,password):
		usern=composer_login.login(s,url,username,password)
		assert username,usern

if __name__=="__main__":
	url="http://cshapidemo.jqweike.com/v1/admin/index/login"
	s=requests.session()
	username="lijie"
	password="123456"
	Test(s).login(url,username,password)




