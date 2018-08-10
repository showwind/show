#coding=utf-8
import unittest,requests
from zbpf.composer.models.image import Image
from zbpf.public.composer_csv import getCsv

class TestImage(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.image=Image(s)
		self.base_url="http://crowdtest.jqweike.com"
		self.filename="E:/test/zbpf/composer/test_data/image.csv"
		self.filename1="E:/test/zbpf/composer/test_data/filepath.csv"
		
	def test_save_activity_banner_image(self):
		#上传banner图
		data=[]
		file=getCsv(1,1,self.filename)
		request=getCsv(2,1,self.filename)
		toCropImgX=getCsv(3,1,self.filename)
		toCropImgY=getCsv(4,1,self.filename)
		toCropImgW=getCsv(5,1,self.filename)
		toCropImgH=getCsv(6,1,self.filename)
		maxWidth=getCsv(7,1,self.filename)
		maxHeight=getCsv(8,1,self.filename)
		minWidth=getCsv(9,1,self.filename)
		comprose=getCsv(10,1,self.filename)
		filepath=getCsv(0,1,self.filename1)
		data.append(file)
		data.append(request)
		data.append(toCropImgX)
		data.append(toCropImgY)
		data.append(toCropImgW)
		data.append(toCropImgH)
		data.append(maxWidth)
		data.append(maxHeight)
		data.append(minWidth)
		data.append(comprose)
		data.append(filepath)
		url=self.base_url+"/v1/admin/image/save-activity-banner-image"
		ac=self.image.save_activity_banner_image(url,data)
		self.assertEqual(int(ac),200)
		
	def test_save_activity_small_image(self):
		#上传活动图片列表
		data=[]
		file=getCsv(11,1,self.filename)
		request=getCsv(12,1,self.filename)
		toCropImgX=getCsv(13,1,self.filename)
		toCropImgY=getCsv(14,1,self.filename)
		toCropImgW=getCsv(15,1,self.filename)
		toCropImgH=getCsv(16,1,self.filename)
		maxWidth=getCsv(17,1,self.filename)
		maxHeight=getCsv(18,1,self.filename)
		minWidth=getCsv(19,1,self.filename)
		comprose=getCsv(20,1,self.filename)
		filepath=getCsv(1,1,self.filename1)
		data.append(file)
		data.append(request)
		data.append(toCropImgX)
		data.append(toCropImgY)
		data.append(toCropImgW)
		data.append(toCropImgH)
		data.append(maxWidth)
		data.append(maxHeight)
		data.append(minWidth)
		data.append(comprose)
		data.append(filepath)
		url=self.base_url+"/v1/admin/image/save-activity-small-image"
		ac=self.image.save_activity_small_image(url,data)
		self.assertEqual(int(ac),200)
		
	def test_save_activity_intro_image(self):
		#保存介绍图片
		data=[]
		file=getCsv(21,1,self.filename)
		request=getCsv(22,1,self.filename)
		toCropImgX=getCsv(23,1,self.filename)
		toCropImgY=getCsv(24,1,self.filename)
		toCropImgW=getCsv(25,1,self.filename)
		toCropImgH=getCsv(26,1,self.filename)
		maxWidth=getCsv(27,1,self.filename)
		maxHeight=getCsv(28,1,self.filename)
		minWidth=getCsv(29,1,self.filename)
		comprose=getCsv(30,1,self.filename)
		filepath=getCsv(2,1,self.filename1)
		data.append(file)
		data.append(request)
		data.append(toCropImgX)
		data.append(toCropImgY)
		data.append(toCropImgW)
		data.append(toCropImgH)
		data.append(maxWidth)
		data.append(maxHeight)
		data.append(minWidth)
		data.append(comprose)
		data.append(filepath)
		url=self.base_url+"/v1/admin/image/save-activity-intro-image"
		ac=self.image.save_activity_intro_image(url,data)
		self.assertEqual(int(ac),200)
	
	def test_save_news_cover_image(self):
		#上传新闻封面
		data=[]
		file=getCsv(21,1,self.filename)
		request=getCsv(22,1,self.filename)
		toCropImgX=getCsv(23,1,self.filename)
		toCropImgY=getCsv(24,1,self.filename)
		toCropImgW=getCsv(25,1,self.filename)
		toCropImgH=getCsv(26,1,self.filename)
		maxWidth=getCsv(27,1,self.filename)
		maxHeight=getCsv(28,1,self.filename)
		minWidth=getCsv(29,1,self.filename)
		comprose=getCsv(30,1,self.filename)
		filepath=getCsv(2,1,self.filename1)
		data.append(file)
		data.append(request)
		data.append(toCropImgX)
		data.append(toCropImgY)
		data.append(toCropImgW)
		data.append(toCropImgH)
		data.append(maxWidth)
		data.append(maxHeight)
		data.append(minWidth)
		data.append(comprose)
		data.append(filepath)
		url=self.base_url+"/v1/admin/image/save-news-cover-image"
		ac=self.image.save_news_cover_image(url,data)
		self.assertEqual(int(ac),200)
	
	def test_upload_cover_image(self):
		#上传作品封面图片
		data=[]
		workid=getCsv(41,1,self.filename)
		coverpath=getCsv(42,1,self.filename)
		data.append(workid)
		data.append(coverpath)
		url=self.base_url+"/v1/admin/works/upload-cover-image"
		ac=self.image.upload_cover_image(url,data)
		self.assertEqual(ac,200)
	
if __name__ == '__main__':
	unittest.main(warnings='ignore')