#coding=utf-8
from jqwk_pom.ElePages import ExamPage
from  jqwk_pom.public import login
import unittest,time
from selenium import webdriver

class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.username ="luhong"
        cls.password ="111111"

    def test_exam(self):
        u'''考试'''
        self.driver.get(ExamPage.user_url)
        login.user_login(self,self.username,self.password)
        user_exam=ExamPage.ExamPage(self.driver,ExamPage.user_url,u"金桥微课 - Index")
        user_exam.click_close()
        user_exam.click_list()
        user_exam.click_exam()
        user_exam.click_texam()
        time.sleep(5)
        user_exam.click_submit()
        assert user_exam.p_title(),u"《excel课程》考试"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()
