#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.order import Order

class TestOrder(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.order=Order(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/order.csv"

	def test_order_list(self):
		#订单列表
		token=getCsv(0,1,self.filename)
		keyword=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/admin/order"+"?token="+token+"&pageSize=10&page=1&keyword=&searchType=orderNumber&rangeStart=&rangeEnd="
		ac=self.order.order_list(url)
		self.assertEqual(ac,200)
	
	def test_weixin_order(self):
		#查询微信订单状态
		token=getCsv(2,1,self.filename)
		orderid=getCsv(3,1,self.filename)
		url=self.base_url+"/v1/frontend/weixin/order"+"?token="+token+"&orderId="+orderid
		ac=self.order.weixin_order(url)
		self.assertEqual(ac,200)
	
	def test_weixin_unifiedorder(self):
		#微信统一下单
		token=getCsv(9,1,self.filename)
		openid=getCsv(8,1,self.filename)
		orderid=getCsv(4,1,self.filename)
		url=self.base_url+"/v1/frontend/weixin/unifiedOrder"+"?token="+token+"&openId="+openid+"&orderId="+orderid
		ac=self.order.weixin_unifiedorder(url)
		self.assertEqual(ac,200)
	
	def test_weixin_getopenid(self):
		#获取公众号用openId
		code=getCsv(7,1,self.filename)
		url=self.base_url+"/v1/frontend/weixin/getOpenId"+"?code="+code
		ac=self.order.weixin_getopenid(url)
		self.assertEqual(ac,200)

	def test_weixin_authorizeurl(self):
		#微信网页静默授权
		token=getCsv(9,1,self.filename)
		url=self.base_url+"/v1/frontend/weixin/authorizeUrl"+"?token="
		ac=self.order.weixin_authorizeurl(url)
		self.assertEqual(ac,200)

	def test_alipay_wappay(self):
		#支付宝手机支付
		token=getCsv(0,1,self.filename)
		orderid=getCsv(5,1,self.filename)
		url=self.base_url+"/v1/frontend/alipay/wapPay"+"?token="+token+"&orderId="+orderid
		self.order.alipay_wappay(url)
	
	def test_pc_alipay(self):
		#PC支付
		token=getCsv(0,1,self.filename)
		orderid=getCsv(6,1,self.filename)
		url=self.base_url+"/v1/frontend/alipay"+"?token="+token+"&orderId="+orderid
		self.order.pc_alipay(url)

if __name__ == '__main__':
	unittest.main(warnings='ignore')