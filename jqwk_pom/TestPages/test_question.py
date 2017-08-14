#coding=utf-8
from jqwk_pom.ElePages import AnswerPage
from jqwk_pom.public import  login
from selenium import webdriver
import time,unittest

class CaseAnswer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.username="luhong"
        cls.password="111111"
    def test_question(self):
        self.driver.get(AnswerPage.user_url)
        login.user_login(self,self.username,self.password)
        add_question=AnswerPage.StudentAnswer(self.driver,AnswerPage.user_url,u"金桥微课 - Index")
        add_question.click_close()
        add_question.click_list()
        add_question.input_textarea("hello world!")
        add_question.click_submit()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()
