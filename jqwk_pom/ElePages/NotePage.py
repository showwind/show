#coding=utf-8
from jqwk_pom.public import BasePage
from selenium.webdriver.common.by import By

note_url="http://www.jqwk.com/"
class NotePage(BasePage.Action):
    btnclose_loc=(By.CSS_SELECTOR,"button.close")
    list_loc=(By.CSS_SELECTOR,"#course-list > div > div.col-lg-3 > a > img")
    course_loc=(By.CSS_SELECTOR,"div.item> div.course-body> ul > a:nth-child(1) > li")
    note_loc=(By.CSS_SELECTOR,"#noteitem > em")
    noteconcent_loc=(By.CSS_SELECTOR,"#noteContent")
    sub_loc=(By.CSS_SELECTOR,"#submitNote")

    def click_close(self):
        self.find_element(*self.btnclose_loc).click()

    def click_list(self):
        t=self.find_elements(self.list_loc) #不能有*self的*
        t[0].click()

    def click_course(self):
        self.find_elements(self.course_loc)[0].click()

    def click_note(self):
        self.find_element(*self.note_loc).click()

    def type_note(self,c):
        self.find_element(*self.noteconcent_loc).send_keys(c)

    def click_submit(self):
        return self.find_element(*self.sub_loc).click()

class UpdateNote(BasePage.Action):
    upuser_loc=(By.LINK_TEXT,u"个人中心")
    uplist_loc=(By.CSS_SELECTOR,"#course-list > div > div.col-lg-3 > a > img")
    upnote_loc=(By.LINK_TEXT,u"笔记")
    upnotelist_loc=(By.CSS_SELECTOR,"div.row > div.col-sm-9 > div > span.pull-right > span > span:nth-child(2) > a")
    upnotecontent_loc=(By.CSS_SELECTOR,"#modnotearea")
    noteconcent_loc=(By.CSS_SELECTOR,"#noteContent")
    sub_loc=(By.CSS_SELECTOR,"#s1 > div > div > div.modal-footer > button.btn.btn-primary")
    p_loc=(By.CSS_SELECTOR," div.row > div.col-sm-9 > p:nth-child(1)")

    def click_upuser(self):
        self.find_element(*self.upuser_loc).click()

    def click_uplist(self):
        t=self.find_elements(self.uplist_loc) #不能有*self的*
        t[0].click()

    def click_upnote(self):
        self.find_element(*self.upnote_loc).click()

    def click_upnotelist(self):
        self.find_elements(self.upnotelist_loc)[0].click()

    def type_upnotecontent(self,c):
        self.find_element(*self.upnotecontent_loc).clear()
        self.find_element(*self.upnotecontent_loc).send_keys(c)

    def click_submit(self):
        return self.find_element(*self.sub_loc).click()

    def note_t(self):
        t=self.find_elements(self.p_loc)[0].text
        print (t)
        return t

class DeleteNote(BasePage.Action):
    btnclose_loc=(By.CSS_SELECTOR,"button.close")
    deluser_loc=(By.LINK_TEXT,u"个人中心")
    dellist_loc=(By.CSS_SELECTOR,"#course-list > div > div.col-lg-3 > a > img")
    note_loc=(By.LINK_TEXT,u"笔记")
    delnote_loc=(By.CSS_SELECTOR,"div.row > div.col-sm-9 > div > span.pull-right > span > span:nth-child(3) > a")
    del_loc=(By.CSS_SELECTOR,"#confirmsubmit")
    delp_loc=(By.CSS_SELECTOR," div.row > div.col-sm-9 > p:nth-child(1)")

    def click_deluser(self):
        self.find_element(*self.deluser_loc).click()

    def click_dellist(self):
        t=self.find_elements(self.dellist_loc) #不能有*self的*
        t[0].click()
    def click_note(self):
        self.find_element(*self.note_loc).click()

    def click_delnote(self):
        self.find_elements(self.delnote_loc)[0].click()

    def click_del(self):
        self.find_element(*self.del_loc).click()

    def note_del(self):
        t=self.find_elements(self.delp_loc)[0].text
        return  t
    def click_close(self):
        self.find_element(*self.btnclose_loc).click()
