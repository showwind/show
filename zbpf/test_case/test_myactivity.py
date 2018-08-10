#coding=utf-8
from zbpf.ElementPages import ActivityPage
import unittest,time 
from zbpf.public import login
from selenium import webdriver

class ActivityCase(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.implicitly_wait(10)
		cls.username="susiku"
		cls.password="123456"
		cls.login_url="http://zbpf.jqweike.com/#/login"
		cls.index_url="http://zbpf.jqweike.com/#/wrap/index"
		cls.driver.get(cls.login_url)
		login.user_login(cls,cls.username,cls.password)
	'''
	def test_add_activity(self):
		#添加活动
		add_activity=ActivityPage.MyActivity(self.driver,self.index_url,u"桥帮主")
		add_activity.click_submenu()
		add_activity.click_list_activity()
		add_activity.click_add()
		add_activity.select_org(1)
		time.sleep(2)
		activityname=u"测试活动2"
		add_activity.input_name(activityname)
		add_activity.input_banner("E:\\test\\zbpf\\2-3.jpg")
		time.sleep(2)
		add_activity.input_cover("E:\\test\\zbpf\\3-5.jpg")
		time.sleep(2)
		add_activity.input_info(u"测试简历")
		add_activity.input_small("E:\\test\\zbpf\\3-6.jpg")
		time.sleep(2)
		add_activity.input_category(u"风景")
		add_activity.input_prizename(u"一等奖")
		add_activity.input_prizeinfo(u"一等奖介绍")
		add_activity.input_num(10)
		add_activity.click_tab2()
		add_activity.click_category(0)
		add_activity.input_starttime("2018-6-25")
		time.sleep(1)
		add_activity.input_endtime("2018-12-25")
		time.sleep(1)
		add_activity.input_reviewtime("2018-12-29")
		time.sleep(1)
		add_activity.input_prizetime("2019-1-25")
		time.sleep(1)
		add_activity.click_tab3()
		add_activity.input_activity_info(u"大赛简介")
		add_activity.input_activitytime("2018-6-25","2019-1-29")
		time.sleep(2)
		add_activity.click_tab3()
		time.sleep(2)
		try:
			add_activity.click_save()
		except:
			self.driver.get_screenshot_as_file("E:\\test\\zbpf\\screenshot\\activity\\add1.jpg")
		time.sleep(2)
		activity_name=add_activity.list_name_text(0)
		self.assertEqual(activityname,activity_name)

	def test_edit(self):
		#编辑活动
		edit_activity=ActivityPage.MyActivity(self.driver,self.index_url,u"桥帮主")
		edit_activity.click_submenu()
		edit_activity.click_list_activity()
		time.sleep(3)
		edit_activity.click_edit_button(1) #根list_name_text()保持一致
		activityname=u"test名称"
		time.sleep(3) #等待返回数据
		try:
			edit_activity.input_edit_activity_name(activityname)
			edit_activity.click_save()
		except:
			self.driver.get_screenshot_as_file("E:\\test\\zbpf\\screenshot\\activity\\edit1.jpg")
		time.sleep(2)
		activity_name=edit_activity.list_name_text(1)
		self.assertEqual(activityname,activity_name)

	def test_school_option(self):
		#选择参赛机构
		add_activity=ActivityPage.MyActivity(self.driver,self.index_url,u"桥帮主")
		add_activity.click_submenu()
		add_activity.click_list_activity()
		add_activity.click_add()
		t=0
		if t!=0:
			add_activity.select_org(t)
		else:
			add_activity.click_org()
			time.sleep(2)
			add_activity.click_org_list(2,2)
			time.sleep(2)
			add_activity.click_org_button()
		time.sleep(2)

	def test_school_delete(self):
		#删除选择的参赛机构
		add_activity=ActivityPage.MyActivity(self.driver,self.index_url,u"桥帮主")
		add_activity.click_submenu()
		add_activity.click_list_activity()
		add_activity.click_add()
		t=0
		if t!=0:
			add_activity.select_org(t)
		else:
			add_activity.click_org()
			time.sleep(2)
			add_activity.click_org_list(2,2)
			time.sleep(2)
			add_activity.click_org_button()
		time.sleep(2)
		add_activity.click_org()
		add_activity.click_delete_org()
		time.sleep(1)
		add_activity.click_org_button()
		time.sleep(2)

	def test_delete(self):
		#删除活动
		delete_activity=ActivityPage.MyActivity(self.driver,self.index_url,u"桥帮主")
		delete_activity.click_submenu()
		delete_activity.click_list_activity()
		time.sleep(3)
		activityname=delete_activity.list_name_text(0)
		delete_activity.click_delete_button(0) #根list_name_text()保持一致
		time.sleep(2)
		try:
			delete_activity.click_error()
			#delete_activity.click_confirm()
			time.sleep(1)
			activity_name=delete_activity.list_name_text(0)
		except:
			self.driver.get_screenshot_as_file("E:\\test\\zbpf\\screenshot\\activity\\delete1.jpg")
		#self.assertNotEqual(activityname,activity_name)
		self.assertEqual(activityname,activity_name)
	'''
	def test_set_prize(self):
		prize_activity=ActivityPage.MyActivity(self.driver,self.index_url,u"桥帮主")
		prize_activity.click_submenu()
		prize_activity.click_list_activity()
		time.sleep(5)
		prize_activity.click_prize_button(1)
		time.sleep(2)
		prize_t=prize_activity.prize_text(1)
		prize_activity.click_set_prize(1)
		time.sleep(2)
		prize_activity.click_prize()
		time.sleep(3)
		prize_activity.click_close_button()
		#print (prize_activity.prize_text(1))#没做好
		time.sleep(2)
	
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

if __name__=="__main__":
	unittest.main()

