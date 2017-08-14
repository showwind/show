#coding=utf-8
from jqwk_pom.ElePages import LoginPage
from jqwk_pom.public import logger
import unittest,time
from selenium import webdriver

class Caselogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.username ="luhong"
        cls.password ="111111"

    def test_user_login(self):
        login_page= LoginPage.LoginPage(self.driver, LoginPage.login_url, u"金桥微课-登陆")
        login_page.open()
        login_page.input_username(self.username)
        login_page.input_password(self.password)
        login_page.click_submit()
        l=logger.Logger()
        l.log().info(u"登录")
        login_page.text_in()
        assert login_page.show_span(),u"卢红"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()

