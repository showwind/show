#coding=utf-8
import unittest,requests
from csh.public.composer_csv import getCsv
from csh.models.note import Note

class TestNote(unittest.TestCase):
	def setUp(self):
		s=requests.session()
		self.note=Note(s)
		self.base_url="http://cshapidemo.jqweike.com"
		self.filename="E:/test/csh/test_data/note.csv"

	def test_note_list(self):
		#课程或班级笔记
		courseid=getCsv(1,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/note"+"?courseId="+courseid+"&token="+token
		ac=self.note.note_list(url)
		self.assertEqual(ac,200)

	def test_add_note(self):
		#新增笔记
		content=getCsv(2,1,self.filename)
		courseid=getCsv(1,1,self.filename)
		chapterid=getCsv(3,1,self.filename)
		chaptername=getCsv(4,1,self.filename)
		token=getCsv(0,1,self.filename)
		data=[]
		data.append(token)
		data.append(content)
		data.append(courseid)
		data.append(chapterid)
		data.append(chaptername)
		url=self.base_url+"/v1/frontend/note/create"
		ac=self.note.add_note(url,data)
		self.assertEqual(ac,200)

	def test_delete_note(self):
		#删除笔记
		noteid=getCsv(5,1,self.filename)
		token=getCsv(0,1,self.filename)
		url=self.base_url+"/v1/frontend/note/delete/"+str(noteid)
		ac=self.note.delete_note(url,token)
		self.assertEqual(ac,200)

	def test_update_note(self):
		#修改笔记
		noteid=getCsv(6,1,self.filename)
		token=getCsv(0,1,self.filename)
		content=getCsv(7,1,self.filename)
		url=self.base_url+"/v1/frontend/note/update/"+str(noteid)
		ac=self.note.update_note(url,token,content)
		self.assertEqual(ac,200)

if __name__ == '__main__':
	unittest.main(warnings='ignore')