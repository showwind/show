#coding=utf-8
from jqwk_pom.ElePages import CoursePage
from jqwk_pom.public import adminlogin
from selenium import webdriver
import unittest,time

user_url="http://www.jqwk.com/academic.php"
class CaseEditCourse(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver=webdriver.Chrome()
		cls.driver.implicitly_wait(10)
		#cls.username="admin11"
		#cls.password="111111"
	def test_editcourse(self):
		u'''编辑课程'''
		self.driver.get(CoursePage.admin_url)
		adminlogin.adminlogin(self)
		edit_course=CoursePage.EditCourse(self.driver,user_url,u"教务管理平台")
		edit_course.click_teachding()
		edit_course.click_courses()
		edit_course.click_course()
		time.sleep(1)
		edit_course.input_period("14")
		time.sleep(1)
		edit_course.input_credit("1")
		time.sleep(1)
		edit_course.input_video("10")
		time.sleep(1)
		edit_course.input_task("10")
		time.sleep(1)
		edit_course.input_test("20")
		edit_course.input_exam("60")
		edit_course.click_over()
		assert edit_course.p_period(),"14"
		time.sleep(5)
	'''
	def test_zdeletecourse(self):
		course_url="http://www.jqwk.com/academic/teaching/course"
		del_course=CoursePage.DeleteCourse(self.driver,course_url,u"教务管理平台")
		assert del_course.p_name(),u"excel课程"
		del_course.click_delcourse()
		del_course.click_submit()
		
	'''
	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
if __name__=="__main__":
	unittest.main()
