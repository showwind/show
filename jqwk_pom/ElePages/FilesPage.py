#coding=utf-8
from jqwk_pom.public import BasePage
from selenium.webdriver.common.by import By

user_url="http://www.jqwk.com/"
class FilePage(BasePage.Action):
    btnclose_loc=(By.CSS_SELECTOR,"button.close")
    list_loc=(By.CSS_SELECTOR,"#course-list > div > div.col-lg-3 > a > img")
    files_loc=(By.LINK_TEXT,u"资料")
    file_loc=(By.CSS_SELECTOR,"#myItems > div.course-tree > div > div.course-body > ul > li:nth-child(1) > div >a")

    def click_close(self):
        self.find_element(*self.btnclose_loc).click()
    def click_list(self):
        self.find_elements(self.list_loc)[1].click()
    def click_files(self):
        self.find_element(*self.files_loc).click()
    def click_file(self):
        self.find_elements(self.file_loc)[1].click()
