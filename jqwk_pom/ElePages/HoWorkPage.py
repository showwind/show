#coding=utf-8
import sys
from jqwk_pom.public import BasePage
from selenium.webdriver.common.by import By

user_url="http://www.jqwk.com/"
class HoWorkPage(BasePage.Action):
    user_loc=(By.LINK_TEXT,u"个人中心")
    btnclose_loc=(By.CSS_SELECTOR,"button.close")
    list_loc=(By.CSS_SELECTOR,"#tab-2 > div > div.row > div.col-lg-3 > a > img")
    home_loc=(By.CSS_SELECTOR,"#_correcthowk_btn > a")
    ho_loc=(By.CSS_SELECTOR,"#boxes12 > div:nth-child(1) > div > img")
    workname_loc=(By.CSS_SELECTOR,"#hmwkname")
    workcontent_loc=(By.CSS_SELECTOR,"#hmwkcontent")
    workdate_loc=(By.CSS_SELECTOR,"#deadline")
    sub_loc=(By.CSS_SELECTOR,"#btnSubmit")
    homework_loc=(By.CSS_SELECTOR,"#boxes12 > div.col-md-3.workBox > h3")

    def click_user(self):
        self.find_element(*self.user_loc).click()

    def click_close(self):
        self.find_element(*self.btnclose_loc).click()

    def click_list(self):
        t=self.find_elements(self.list_loc)
        t[0].click()
        #self.find_element(*self.list_loc).click()

    def click_home(self):
        self.find_element(*self.home_loc).click()

    def click_ho(self):
        self.find_element(*self.ho_loc).click()

    def type_workname(self,name):
        self.find_element(*self.workname_loc).send_keys(name)

    def type_workcontent(self,content):
        self.find_element(*self.workcontent_loc).clear()
        self.find_element(*self.workcontent_loc).send_keys(content)

    def type_workdate(self,date):
        self.find_element(*self.workdate_loc).clear()
        self.find_element(*self.workdate_loc).send_keys(date)
        '''
        js_value='document.getElementById("deadline").value="2017-7-30"'
        self.script(js_value) #可不弹出提醒框
        '''

    def click_submit(self):
        self.find_element(*self.sub_loc).submit()
    def assert_homework(self):
        t=self.find_elements(self.homework_loc)[0].text
        print (t)
        return t
        
class SHomePage(BasePage.Action):
    button_loc=(By.CSS_SELECTOR,"button.close")
    list_loc=(By.CSS_SELECTOR,"#course-list > div > div.col-lg-3 > a > img")
    work_loc=(By.LINK_TEXT,u"作业")
    home_loc=(By.CSS_SELECTOR,"#showHomework > div:first-child > div:last-child>button")
    inputfile_loc=(By.CSS_SELECTOR,"#exampleInputFile")
    input_loc=(By.CSS_SELECTOR,"#viewfile")
    submit_loc=(By.CSS_SELECTOR,"#hw_form > button")
    cherk_loc=(By.CSS_SELECTOR,"#showHomework > div.col-md-3.workBox > div:nth-child(4)>button")
    comfirm_loc=(By.CSS_SELECTOR,"body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm")
    def click_message(self):   
        self.find_element(*self.button_loc).click()
    def click_course(self):
        self.find_elements(self.list_loc)[0].click()
    def click_work(self):
        self.find_element(*self.work_loc).click()
    def click_home(self):
        self.find_element(*self.home_loc).click()
    def click_comfirm(self):
        self.find_element(*self.comfirm_loc).click()
    '''
    #opacity: 0表示元素已隐藏，is_displayed()查找为false
    def send_inputfile(self,filename):
        js="document.getElementById('exampleInputFile').style.opacity=1;"
        self.script(js)
        self.find_element(*self.inputfile_loc).clear()
        self.find_element(*self.inputfile_loc).send_keys(filename)
    '''
    def click_submit(self):
        self.find_element(*self.submit_loc).click()
    def alert_home(self):
        try:
            t=self.is_alert_present()
            t.accept()
        except:
            print (u"不存在")
    def assert_cherk(self):
        t=self.find_elements(self.cherk_loc)[0].text
        return t
class THomePage(BasePage.Action):
    list_loc=(By.CSS_SELECTOR,"#tab-2 > div > div.row > div.col-lg-3 > a > img")
    home_loc=(By.CSS_SELECTOR,"#_correcthowk_btn > a")
    hm_loc=(By.CSS_SELECTOR,"#boxes12 > div.col-md-3.workBox > div.row.lastLine > div:nth-child(2) > span")
    tp_loc=(By.CSS_SELECTOR,"#willCheck > tbody > tr:nth-child(1) > td:nth-child(5) > button")
    upload_loc=(By.CSS_SELECTOR,"#checkfile")
    score_loc=(By.CSS_SELECTOR,"#score")
    teachercontent_loc=(By.CSS_SELECTOR,"#teachercontent")
    submit_loc=(By.CSS_SELECTOR,"#over")

    def click_loc(self):
        self.find_elements(self.list_loc)[1].click()
    def click_home(self):
        self.find_element(*self.home_loc).click()
    def click_hm(self):
        self.find_elements(self.hm_loc)[0].click()
    def click_tp(self):
        self.find_element(*self.tp_loc).click()
    def input_upload(self,filename):
        js = 'document.getElementById("checkfile").removeAttribute("readonly");'
        self.script(js)
        self.find_element(*self.upload_loc).send_keys(filename)
    def input_score(self,c):
        self.find_element(*self.score_loc).send_keys(c)
    def input_teachercontent(self,c):
        self.find_element(*self.teachercontent_loc).send_keys(c)
    def click_submit(self):
        self.find_element(*self.submit_loc).click()




