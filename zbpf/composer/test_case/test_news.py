#coding=utf-8
import unittest
import requests
from zbpf.composer.models.news import News
from zbpf.public.composer_csv import getDdtCsv
from zbpf.public.composer_csv import getCsv
from ddt import ddt,data,unpack

@ddt
class TestNews(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.news=News(s)
		self.base_url="http://crowdtest.jqweike.com"
		self.file_name="E:/test/zbpf/composer/test_data/news1.csv"

	def test_a(self):
		url=self.base_url+"/v1/admin/site/login"
		username=getCsv(17,1,self.file_name)
		password=getCsv(18,1,self.file_name)
		name=self.news.login(url,username,password)
		self.assertEqual(username,name)
	
	@data(*getDdtCsv("E:\\test\\zbpf\\composer\\test_data\\news.csv"))
	@unpack
	def test_get_news(self,name,nid):
		#根据新闻id 获取新闻详情
		url=self.base_url+"/v1/admin/news/get-news-by-id"+"?newsId="+str(nid)
		n_id=self.news.get_news(url)
		self.assertEqual(n_id,nid)
	
	def test_add_news(self):
		#新增新闻
		data=[]
		data.append(getCsv(0,1,self.file_name))
		data.append(getCsv(1,1,self.file_name))
		data.append(getCsv(2,1,self.file_name))
		data.append(getCsv(3,1,self.file_name))
		data.append(getCsv(4,1,self.file_name))
		data.append(getCsv(5,1,self.file_name))
		data.append(getCsv(6,1,self.file_name))
		data.append(getCsv(7,1,self.file_name))
		data.append(getCsv(9,1,self.file_name))
		data.append(getCsv(10,1,self.file_name))
		url=self.base_url+"/v1/admin/news/news-add"
		ac=self.news.add_news(url,data)
		self.assertEqual(ac,200)
		
	def test_modify_news(self):
		#修改新闻
		data=[]
		data.append(getCsv(0,1,self.file_name))
		data.append(getCsv(1,1,self.file_name))
		data.append(getCsv(2,1,self.file_name))
		data.append(getCsv(3,1,self.file_name))
		data.append(getCsv(4,1,self.file_name))
		data.append(getCsv(5,1,self.file_name))
		data.append(getCsv(6,1,self.file_name))
		data.append(getCsv(7,1,self.file_name))
		data.append(getCsv(8,1,self.file_name))
		data.append(getCsv(9,1,self.file_name))
		data.append(getCsv(10,1,self.file_name))
		data.append(getCsv(8,1,self.file_name))
		data.append(getCsv(11,1,self.file_name))
		url=self.base_url+"/v1/admin/news/modify-news"
		ac=self.news.modify_news(url,data)
		self.assertEqual(ac,200)
		
	def test_view_news(self):
		#获取新闻列表分页
		data=[]
		page=getCsv(12,1,self.file_name)
		pagesize=getCsv(13,1,self.file_name)
		activityid=getCsv(14,1,self.file_name)
		userid=getCsv(15,1,self.file_name)
		data.append(page)
		data.append(pagesize)
		data.append(activityid)
		data.append(userid)
		url=self.base_url+"/v1/admin/news/view-news"
		ac=self.news.view_news(url,data)
		self.assertEqual(ac,200)

	def test_delete_news(self):
		#删除新闻
		newsid=getCsv(16,1,self.file_name)
		url=self.base_url+"/v1/admin/news/news-delete"
		ac=self.news.delete_news(url,newsid)
		self.assertEqual(ac,200)
	
if __name__ == '__main__':
	unittest.main(warnings='ignore')