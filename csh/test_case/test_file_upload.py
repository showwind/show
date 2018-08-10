#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.file_upload import FileUpload

class TestClasses(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.fileupload=FileUpload(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/fileupload.csv"

	def test_upload_resourse(self):
		#上传资源文件 
		data=[]
		courseid=getCsv(0,1,self.filename)
		file=getCsv(1,1,self.filename)
		filepath=getCsv(2,1,self.filename)
		data.append(courseid)
		data.append(file)
		data.append(filepath)
		url=self.base_url+"/v1/frontend/file/uploadResource"
		ac=self.fileupload.upload_resourse(url,data)
		self.assertEqual(ac,200)

	def test_upload_pic(self):
		#上传图片
		data=[]
		file=getCsv(3,1,self.filename)
		filepath=getCsv(4,1,self.filename)
		data.append(file)
		data.append(filepath)
		url=self.base_url+"/v1/frontend/file/uploadPic"
		ac=self.fileupload.upload_pic(url,data)
		self.assertEqual(ac,200)
if __name__ == '__main__':
	unittest.main(warnings='ignore')