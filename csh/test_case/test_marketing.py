#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.marketing import Marketing

class TestMarketing(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.marketing=Marketing(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/marketing.csv"
	
	def test_marketing_list(self):
		#价格营销位列表
		url=self.base_url+"/v1/admin/marketing"
		ac=self.marketing.marketing_list(url)
		self.assertEqual(ac,200)
		
	def test_create_marketing(self):
		#添加价格营销
		token=getCsv(0,1,self.filename)
		markettitle=getCsv(1,1,self.filename)
		markettype=getCsv(2,1,self.filename)
		starttime=getCsv(3,1,self.filename)
		endtime=getCsv(4,1,self.filename)
		courseids=getCsv(5,1,self.filename)
		userid=getCsv(6,1,self.filename)
		username=getCsv(7,1,self.filename)
		marketprice=getCsv(8,1,self.filename)
		discount=getCsv(9,1,self.filename)
		integral=getCsv(10,1,self.filename)
		data=[]
		data.append(token)
		data.append(markettitle)
		data.append(markettype)
		data.append(starttime)
		data.append(endtime)
		data.append(courseids)
		data.append(userid)
		data.append(username)
		data.append(marketprice)
		data.append(discount)
		data.append(integral)
		url=self.base_url+"/v1/admin/marketing/create"
		self.marketing.create_marketing(url,data)
	
	def test_delete_marketing(self):
		#删除价格营销
		mid=getCsv(11,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/admin/marketing/delete/"+mid
		self.marketing.delete_marketing(url,token)
	
	def test_update_marketing(self):
		#修改价格营销
		token=getCsv(0,1,self.filename)
		mid=getCsv(12,1,self.filename)
		markettitle=getCsv(1,1,self.filename)
		markettype=getCsv(2,1,self.filename)
		starttime=getCsv(3,1,self.filename)
		endtime=getCsv(4,1,self.filename)
		courseids=getCsv(5,1,self.filename)
		userid=getCsv(6,1,self.filename)
		username=getCsv(7,1,self.filename)
		marketprice=getCsv(13,1,self.filename)
		discount=getCsv(9,1,self.filename)
		integral=getCsv(10,1,self.filename)
		data=[]
		data.append(token)
		data.append(markettitle)
		data.append(markettype)
		data.append(starttime)
		data.append(endtime)
		data.append(courseids)
		data.append(userid)
		data.append(username)
		data.append(marketprice)
		data.append(discount)
		data.append(integral)
		url=self.base_url+"/v1/admin/marketing/update/"+mid
		self.marketing.create_marketing(url,data)
	
	def test_marketing_view(self):
		#价格营销详情
		token=getCsv(0,1,self.filename)
		vid=getCsv(14,1,self.filename)
		url=self.base_url+"/v1/admin/marketing/view/"+vid+"?token="+token
		self.marketing.marketing_view(url)
if __name__ == '__main__':
	unittest.main(warnings='ignore')