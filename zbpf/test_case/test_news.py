#coding=utf-8
from zbpf.ElementPages import NewsPage
import unittest,time
from zbpf.public import login
from selenium import webdriver

class NewsCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.implicitly_wait(10)
		cls.username="susiku"
		cls.password="123456"
		cls.login_url="http://zbpf.jqweike.com/#/login"
		cls.driver.get(cls.login_url)
		login.user_login(cls,cls.username,cls.password)

	def test_add_news(self):
		u'''添加新闻'''
		add_news=NewsPage.NewsPage(self.driver,NewsPage.index_url,u"桥帮主")
		add_news.click_submenu()
		add_news.click_news()
		add_news.click_add()
		add_news.input_title(u"测试1")
		add_news.input_content(u"测试摘要")
		add_news.input_cover("E:\\test\\zbpf\\3-5.jpg")
		add_news.click_button()
		time.sleep(2)
		add_news.input_body(u"测试正文")
		add_news.click_save()
		time.sleep(2)
		self.driver.refresh()
		title_text=add_news.title_text(0)
		self.assertEqual(title_text,u"测试1")

	def test_edit_news(self):
		u'''编辑新闻'''
		edit_news=NewsPage.NewsPage(self.driver,NewsPage.index_url,u"桥帮主")
		edit_news.click_submenu()
		edit_news.click_news()
		time.sleep(3)
		edit_news.click_eidt(1)
		time.sleep(3)
		edit_news.select_activity(4)      #跟select_activity_text()保持一致        
		select_activity_text=edit_news.select_activity_text(4)
		edit_news.edit_save()
		time.sleep(2)
		activity_text=edit_news.activity_text(1)	#跟click_edit()保持一致	

	def test_remove_news(self):
		u'''删除新闻'''
		remove_news=NewsPage.NewsPage(self.driver,NewsPage.index_url,u"桥帮主")
		remove_news.click_submenu()
		remove_news.click_news()
		time.sleep(3)
		a=remove_news.title_text(1) #跟click_remove保持一致
		remove_news.click_remove(1)
		remove_news.click_confirm()
		b=remove_news.title_text(1)
		self.assertNotEqual(a,b)

	def test_preview_news(self):
		u'''预览新闻'''
		preview_news=NewsPage.NewsPage(self.driver,NewsPage.index_url,u"桥帮主")
		preview_news.click_submenu()
		preview_news.click_news()
		time.sleep(3)
		a=preview_news.title_text(1)
		preview_news.click_preview(1)
		time.sleep(3)
		b=preview_news.preview_title_text()
		self.assertEqual(a,b)
	
	def test_list(self):
		u'''筛选新闻'''
		list_news=NewsPage.NewsPage(self.driver,NewsPage.index_url,u"桥帮主")
		list_news.click_submenu()
		list_news.click_news()
		time.sleep(3)
		list_news.list_activity(1) #比activity_text小一个数
		list_select_activity_text=list_news.list_select_activity_text(1)
		activity_text=list_news.activity_text(0)
		self.assertEqual(list_select_activity_text,activity_text)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		
if __name__=="__main__":
	#unittest.main()
	testunit=unittest.TestSuite()
	testunit.addTest(NewsPage("test_list"))
	filename=r'E:\\test\\zbpf\\report\\result.html'
	fp=file(filename,'wb')
	runner=HTMLTestRunner.HTMLTestRunner(stream=fp,titlr=u'新闻管理测试报告',description=u'用例执行情况')
	runner.run(testunit)