#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.userorder import UserOrder

class TestUserOrder(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.userorder=UserOrder(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/userorder.csv"

	def test_userorder_list(self):
		#获取用户订单
		token=getCsv(0,1,self.filename)
		status=getCsv(1,1,self.filename)
		url=self.base_url+"/v1/frontend/order"+"?token="+token+"&status="+status
		ac=self.userorder.userorder_list(url)
		self.assertEqual(ac,200)
	
	def test_order_income(self):
		#收入订单
		token=getCsv(2,1,self.filename)
		url=self.base_url+"/v1/frontend/order/income"+"?token="+token
		ac=self.userorder.order_income(url)
		self.assertEqual(ac,200)
	
	def test_order_detail(self):
		#订单详情
		token=getCsv(0,1,self.filename)
		orderid=getCsv(3,1,self.filename)
		url=self.base_url+"/v1/frontend/order/view/"+orderid+"?token="+token
		ac=self.userorder.order_detail(url)
		self.assertEqual(ac,200)
	
	def test_order_class(self):
		#创建班级订单
		token=getCsv(4,1,self.filename)
		classid=getCsv(5,1,self.filename)
		data=[]
		data.append(token)
		data.append(classid)
		url=self.base_url+"/v1/frontend/order/class"
		ac=self.userorder.order_class(url,data)
		self.assertEqual(ac,200)
	
	def test_order_course(self):
		#创建课程订单
		token=getCsv(4,1,self.filename)
		courseid=getCsv(6,1,self.filename)
		data=[]
		data.append(token)
		data.append(courseid)
		url=self.base_url+"/v1/frontend/order/course"
		ac=self.userorder.order_course(url,data)
		self.assertEqual(ac,200)
	
	def test_order_cancel(self):
		#取消订单
		token=getCsv(4,1,self.filename)
		orderid=getCsv(7,1,self.filename)
		data=[]
		data.append(token)
		data.append(orderid)
		url=self.base_url+"/v1/frontend/order/cancel"
		ac=self.userorder.order_cancel(url,data)
		self.assertEqual(ac,200)
	
	def test_order_success(self):
		#支付成功
		token=getCsv(4,1,self.filename)
		orderid=getCsv(8,1,self.filename)
		data=[]
		data.append(token)
		data.append(orderid)
		url=self.base_url+"/v1/frontend/order/success"
		ac=self.userorder.order_success(url,data)
		self.assertEqual(ac,200)

if __name__ == '__main__':
	unittest.main(warnings='ignore')