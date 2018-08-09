#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.market_postion import MarketPostion

class TestMarketPostion(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.marketpostion=MarketPostion(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/marketpostion.csv"
	
	def test_marketpostion_list(self):
		#价格营销位列表
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/admin/marketPosition"+"?expand=position&token="+token+"&page=1&pageSize=10&searchType=title&keyword=&rangeStart=&rangeEnd="
		ac=self.marketpostion.marketpostion_list(url)
		self.assertEqual(ac,200)
		
	def test_create_marketpostion(self):
		#添加营销位
		token=getCsv(0,1,self.filename)
		title=getCsv(1,1,self.filename)
		introduce=getCsv(2,1,self.filename)
		courseids=getCsv(3,1,self.filename)
		number=getCsv(4,1,self.filename)
		way=getCsv(5,1,self.filename)
		coverimage=getCsv(6,1,self.filename)
		detailcover=getCsv(7,1,self.filename)
		starttime=getCsv(8,1,self.filename)
		endtime=getCsv(9,1,self.filename)
		userid=getCsv(10,1,self.filename)
		username=getCsv(11,1,self.filename)
		data=[]
		data.append(token)
		data.append(title)
		data.append(introduce)
		data.append(courseids)
		data.append(number)
		data.append(way)
		data.append(coverimage)
		data.append(detailcover)
		data.append(starttime)
		data.append(endtime)
		data.append(userid)
		data.append(username)
		url=self.base_url+"/v1/admin/marketPosition/create"
		self.marketpostion.create_marketpostion(url,data)
	
	def test_update_marketpostion(self):
		token=getCsv(0,1,self.filename)
		title=getCsv(13,1,self.filename)
		introduce=getCsv(2,1,self.filename)
		courseids=getCsv(3,1,self.filename)
		number=getCsv(4,1,self.filename)
		way=getCsv(5,1,self.filename)
		coverimage=getCsv(6,1,self.filename)
		detailcover=getCsv(7,1,self.filename)
		starttime=getCsv(8,1,self.filename)
		endtime=getCsv(9,1,self.filename)
		userid=getCsv(10,1,self.filename)
		username=getCsv(11,1,self.filename)
		mid=getCsv(12,1,self.filename)
		data=[]
		data.append(token)
		data.append(title)
		data.append(introduce)
		data.append(courseids)
		data.append(number)
		data.append(way)
		data.append(coverimage)
		data.append(detailcover)
		data.append(starttime)
		data.append(endtime)
		data.append(userid)
		data.append(username)
		url=self.base_url+"/v1/admin/marketPosition/update/"+mid
		self.marketpostion.update_marketpostion(url,data)
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')