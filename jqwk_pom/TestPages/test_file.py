#coding=utf-8
from jqwk_pom.ElePages import FilesPage
from  jqwk_pom.public import login
import unittest,time
from selenium import webdriver

class CaseFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.username ="luhong"
        cls.password ="111111"

    def test_test(self):
        u'''资料'''
        self.driver.get(FilesPage.user_url)
        login.user_login(self,self.username,self.password)
        user_test=FilesPage.FilePage(self.driver,FilesPage.user_url,u"金桥微课 - Index")
        user_test.click_close()
        user_test.click_list()
        user_test.click_files()
        user_test.click_file()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__=="__main__":
    unittest.main()
