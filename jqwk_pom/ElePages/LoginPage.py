#coding=utf-8
from jqwk_pom.public import BasePage
from selenium.webdriver.common.by import By

login_url = "http://www.jqwk.com/login"
class LoginPage(BasePage.Action):
    username_loc=(By.ID,"username")
    password_loc=(By.ID,"password")
    submit_loc=(By.CSS_SELECTOR,"#login-form > button")
    span_loc=(By.CSS_SELECTOR,"body > div.navbar.navbar-fixed-top > div > div.navbar-collapse.collapse > ul.nav.navbar-nav.status-nav > li:nth-child(1) > a > span.vm.offset-1x")
    def open(self):
        self._open(self.base_url,self.pagetitle)

    def input_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    def show_span(self):
        return self.find_element(*self.span_loc).text
    def text_in(self):
        text=u"卢红"
        print (self.is_text_in_element(self.span_loc,text)) 

