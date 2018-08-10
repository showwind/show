#coding=utf-8
import unittest,time
from selenium import webdriver
from jqwk_pom.ElePages import HoWorkPage 
from jqwk_pom.public import login

class CaseHomeWork(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.username ="yonghu1"
        cls.password ="111111"

    def test_addhomework(self):
        self.driver.get(HoWorkPage.user_url)
        login.user_login(self,self.username,self.password)
        add_homework=HoWorkPage.HoWorkPage(self.driver,HoWorkPage.user_url,u"金桥微课 - Index")        
        add_homework.click_list()
        add_homework.click_home()
        t=self.driver.title
        assert t,u"金桥微课 - Detail Myclasses"
        try:
            add_homework.click_ho()
            add_homework.type_workname("ceshi")
            add_homework.type_workcontent("123")
            add_homework.type_workdate('2018/08/30')
            add_homework.click_submit()
            t=add_homework.assert_homework()
            assert t,"ceshi"
        except:
            pass
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()

