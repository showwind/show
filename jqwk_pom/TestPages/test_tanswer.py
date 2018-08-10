#coding=utf-8
from jqwk_pom.ElePages import AnswerPage
from jqwk_pom.public import  login
from selenium import webdriver
import time,unittest

class CaseTAnswer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.username="yonghu1"
        cls.password="111111"
    def test_answer(self):
        self.driver.get(AnswerPage.user_url)
        login.user_login(self,self.username,self.password)
        answer_question=AnswerPage.TeacherAnswer(self.driver,AnswerPage.user_url,u"金桥微课 - Index")
        answer_question.click_list()
        answer_question.click_answer()
        answer_question.click_count()
        answer_question.input_textarea("welcome")
        answer_question.click_submit()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()
