#coding=utf-8
from jqwk_pom.public import BasePage
from selenium.webdriver.common.by import By

user_url="http://www.jqwk.com/"
class TestPage(BasePage.Action):
    btnclose_loc=(By.CSS_SELECTOR,"button.close")
    list_loc=(By.LINK_TEXT,u"测验")
    test_loc=(By.CSS_SELECTOR,"div.items.col-md-3 > div > button")
    title_loc=(By.CSS_SELECTOR,"#exam_questsmodal > div > div > div.modal-header > h4")
    submitpbtn_loc=(By.ID,"submittpbtn")

    def click_close(self):
        self.find_element(*self.btnclose_loc).click()
    def click_list(self):
        self.find_elements(self.list_loc)[0].click()
    def click_tst(self):
        self.find_elements(self.test_loc)[1].click()
    def click_submit(self):
        self.find_element(*self.submitpbtn_loc).click()
    def p_title(self):
        return self.find_element(*self.title_loc).text
class ExamPage(BasePage.Action):
    btnclose_loc=(By.CSS_SELECTOR,"button.close")
    list_loc=(By.CSS_SELECTOR,"#course-list > div > div.col-lg-3 > a > img")
    exam_loc=(By.LINK_TEXT,u"考试")
    texam_loc=(By.CSS_SELECTOR,"div.text-center.row-4x > div > span:nth-child(2) > a")
    submit_loc=(By.ID,"exam_startmodal_startbtn")
    text_loc=(By.CSS_SELECTOR,"#exam_questsmodal > div > div > div.modal-header > h4")

    def click_close(self):
        self.find_element(*self.btnclose_loc).click()
    def click_list(self):
        self.find_elements(self.list_loc)[0].click()
    def click_exam(self):
        self.find_element(*self.exam_loc).click()
    def click_texam(self):
        self.find_element(*self.texam_loc).click()
    def click_submit(self):
        self.find_element(*self.submit_loc).click()
    def p_title(self):
        return self.find_element(*self.text_loc).text

