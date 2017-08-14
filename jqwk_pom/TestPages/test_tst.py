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

    def test_tst(self):
        u'''测验'''
        self.driver.get(ExamPage.user_url)
        login.user_login(self,self.username,self.password)
        user_test=ExamPage.TestPage(self.driver,ExamPage.user_url,u"金桥微课 - Index")
        user_test.click_close()
        user_test.click_list()
        user_test.click_tst()
        user_test.click_submit()
        assert user_test.p_title(),u"《第1章 html5概述》测验"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()
