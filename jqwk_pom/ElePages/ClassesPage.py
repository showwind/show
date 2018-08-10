#coding=utf-8
from  jqwk_pom.public import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

admin_url="http://www.jqwk.com/academic/login/index"
user_url="http://www.jqwk.com/academic.php"
class AddClass(BasePage.Action):
    teaching_loc=(By.CSS_SELECTOR,"#primary-nav > ul > li:nth-child(5) > a")
    classes_loc=(By.CSS_SELECTOR,"#primary-nav>ul>li:nth-child(5)>ul>li:nth-child(2)> a")
    addclass_loc=(By.CSS_SELECTOR,"#addclass")
    classname_loc=(By.CSS_SELECTOR,"#className")
    classicon_loc=(By.CSS_SELECTOR,"#page1form > div:nth-child(3) > div > img")
    getcourse_loc=(By.CSS_SELECTOR,"#page1form > div:nth-child(4) > div.col-sm-3 > button")
    searchkey_loc=(By.CSS_SELECTOR,"#searchKey")
    subsearch_loc=(By.CSS_SELECTOR,"#subSearch")
    course_loc=(By.CSS_SELECTOR,"#course")
    subchoice_loc=(By.CSS_SELECTOR,"#subChoice")
    choiceteacher_loc=(By.ID,"choiceTeacher")
    teacher_loc=(By.CSS_SELECTOR,"td > #teacher")
    assistant_loc=(By.CSS_SELECTOR,"#page1form > div:nth-child(6) > div.col-sm-3 > button")
    learnstart_loc=(By.ID,"learnStart")
    learnend_loc=(By.ID,"learnEnd")
    examtimestart_loc=(By.ID,"examTimeStart")
    examtimeend_loc=(By.ID,"examTimeEnd")
    next_loc=(By.ID,"next")
    openqa_loc=(By.XPATH,"//input[@value='1']")
    opena_loc=(By.XPATH,"//input[@value='0']")
    teacherid_loc=(By.CSS_SELECTOR,"#teacherOptions")
    issethomework_loc=(By.CSS_SELECTOR,"#isSetHomework")
    ischeckofwork_loc=(By.CSS_SELECTOR,"#isCheckOfWork")
    homeworkteacher_loc=(By.CSS_SELECTOR,"#homeworkTeacherOptions")
    searchstudent_loc=(By.ID,"searchstudent")
    student_loc=(By.CSS_SELECTOR,"div.col-sm-8 > div.col-sm-3 > button.btn.btn-mini")
    choiceall_loc=(By.ID,"choiceAll")
    subchoicestudent_loc=(By.ID,"subChoiceStudent")
    over_loc=(By.ID,"over")
    edit_loc=(By.CSS_SELECTOR,"#classlist > tr.odd > td:nth-child(1)")
    def click_teaching(self):
        self.find_element(*self.teaching_loc).click()
    def click_classes(self):
        self.find_element(*self.classes_loc).click()
    def click_addclass(self):
        self.find_element(*self.addclass_loc).click()
    def input_classname(self,c):
        self.find_element(*self.classname_loc).clear()
        self.find_element(*self.classname_loc).send_keys(c)
    def click_classicon(self):
        self.find_elements(self.classicon_loc)[1].click()
    def click_getcourse(self):
        self.find_element(*self.getcourse_loc).click()
    def input_searchkey(self,c):
        self.find_element(*self.searchkey_loc).clear()
        self.find_element(*self.searchkey_loc).send_keys(c)
    def click_subsearch(self):
        self.find_element(*self.subsearch_loc).click()
    def click_course(self):
        self.find_elements(self.course_loc)[3].click()
    def click_subchoice(self):
        self.find_element(*self.subchoice_loc).click()
    def click_choiceteacher(self):
        self.find_element(*self.choiceteacher_loc).click()
    def click_teacher(self):
        self.find_element(*self.teacher_loc).click()
    def click_assistant(self):
        self.find_element(*self.assistant_loc).click()
    def input_learnstart(self):
        js_value='document.getElementById("learnStart").value="2017/7/30"'
        self.script(js_value)
    def input_learnend(self):
        js_value='document.getElementById("learnEnd").value="2017/8/30"'
        self.script(js_value)
    def input_examtimestart(self):
        js_value='document.getElementById("examTimeStart").value="2017/7/30"'
        self.script(js_value)
    def input_examtimeend(self):
        js_value='document.getElementById("examTimeEnd").value="2017/8/30"'
        self.script(js_value)
    def click_next(self):
        self.find_element(*self.next_loc).click()
    def click_openqa(self):
        #self.find_element(*self.opena_loc).send_keys(Keys.SPACE)
        self.find_element(*self.openqa_loc).click()
        if self.find_element(*self.opena_loc).is_selected():
            print ('selected!')
        else:
            print ("not yet!")
    def click_teacherid(self,c):
        s=self.find_element(*self.teacherid_loc)
        Select(s).select_by_value(c)
    def click_issethomework(self):
        self.find_elements(self.issethomework_loc)[0].click()
    def click_ischeckofwork(self):
        self.find_elements(self.ischeckofwork_loc)[0].click()
    def click_homeworkteacher(self,c):
        s=self.find_element(*self.homeworkteacher_loc)
        Select(s).select_by_value(c)
    def input_searchstudent(self,c):
        self.find_element(*self.searchstudent_loc).clear()
        self.find_element(*self.searchstudent_loc).send_keys(c)
    def click_student(self):
        self.find_element(*self.student_loc).click()
    def click_choiceall(self):
        self.find_element(*self.choiceall_loc).click()
    def click_subchoicestudent(self):
        self.find_element(*self.subchoicestudent_loc).click()
    def click_over(self):
        self.find_element(*self.over_loc).click()
    def text_edit(self):
        return self.find_elements(self.edit_loc)[0].text

class ImportClasses(BasePage.Action):
    classes_loc=(By.CSS_SELECTOR,"#primary-nav>ul>li:nth-child(5)>ul>li:nth-child(2)> a")
    importclass_loc=(By.CSS_SELECTOR,"#page-content > div.dataTables_wrapper.form-inline > div:nth-child(1) > div:nth-child(4) > a")
    filename=(By.NAME,"file")
    submit_loc=(By.CSS_SELECTOR,"#adduserform > div > div.form-group.form-actions > div > button")
    edit_loc=(By.CSS_SELECTOR,"#classlist > tr.odd > td:nth-child(1)")
    willclass_loc=(By.CSS_SELECTOR,"#page-content > div.dataTables_wrapper.form-inline > div.row.activeBtn > button.btn.btn-success")
    def click_importclass(self):
        self.find_element(*self.importclass_loc).click()
    def input_filename(self,c):
        self.find_element(*self.filename).send_keys(c)
    def click_submit(self):
        self.find_element(*self.submit_loc).click()
    def click_classes(self):
        self.find_element(*self.classes_loc).click()
    def p_class(self):
        return self.find_elements(self.edit_loc)[0].text
    def click_class(self):
        self.find_element(*self.willclass_loc).click()

class DeleteClasses(BasePage.Action):
    teaching_loc=(By.CSS_SELECTOR,"#primary-nav > ul > li:nth-child(5) > a")
    classes_loc=(By.CSS_SELECTOR,"#primary-nav>ul>li:nth-child(5)>ul>li:nth-child(2)> a")
    willclass_loc=(By.CSS_SELECTOR,"#page-content > div.dataTables_wrapper.form-inline > div.row.activeBtn > button:nth-child(2)")
    #deleteclass_loc=(By.XPATH,"//*[@id='classlist']/tr[1]/td[6]/span[2]/img")
    deleteclass_loc=(By.CSS_SELECTOR,"#classlist > tr > td.text-center > span:nth-child(3) > img")
    comfirm_loc=(By.CSS_SELECTOR,"body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm")
    text_loc=(By.CSS_SELECTOR,"#classlist > tr > td:nth-child(1)")

    def click_teaching(self):
        self.find_element(*self.teaching_loc).click()
    def click_classes(self):
        self.find_element(*self.classes_loc).click()
    def click_willclass(self):
        self.find_element(*self.willclass_loc).click()
    def click_deleteclass(self):
        #self.find_element(*self.deleteclass_loc).click()
        self.find_elements(self.deleteclass_loc)[0].click()
    def click_comfirm(self):
        self.find_element(*self.comfirm_loc).click()
    def text_class(self):
        return self.find_elements(self.text_loc)[0].text
class EditClass(BasePage.Action):
    teaching_loc=(By.CSS_SELECTOR,"#primary-nav > ul > li:nth-child(5) > a")
    classes_loc=(By.CSS_SELECTOR,"#primary-nav>ul>li:nth-child(5)>ul>li:nth-child(2)> a")
    willclass_loc=(By.CSS_SELECTOR,"#page-content > div.dataTables_wrapper.form-inline > div.row.activeBtn > button:nth-child(2)")
    next_loc=(By.ID,"next")
    edit_loc=(By.CSS_SELECTOR,"#classlist > tr > td.text-center > span:nth-child(2) > img")
    classname_loc=(By.ID,"className")
    over_loc=(By.ID,"over")
    text_loc=(By.CSS_SELECTOR,"#classlist > tr > td:nth-child(1)")
    lndx=(By.CSS_SELECTOR,"#primary-nav > ul > li:nth-child(1) > a")
    def click_teaching(self):
        self.find_element(*self.teaching_loc).click()
    def click_classes(self):
        self.find_element(*self.classes_loc).click()
    def click_willclass(self):
        self.find_element(*self.willclass_loc).click()   
    def click_edit(self):
        self.find_elements(self.edit_loc)[0].click()
    def input_classname(self,c):
        self.find_element(*self.classname_loc).clear()
        self.find_element(*self.classname_loc).send_keys(c)
    def click_next(self):
        self.find_element(*self.next_loc).click()
    def click_over(self):
        self.find_element(*self.over_loc).click()
    def text_class(self):
        return self.find_elements(self.text_loc)[0].text
class Uploadinfo(BasePage.Action):
    teaching_loc=(By.CSS_SELECTOR,"#primary-nav > ul > li:nth-child(5) > a")
    classes_loc=(By.CSS_SELECTOR,"#primary-nav>ul>li:nth-child(5)>ul>li:nth-child(2)> a")
    class_loc=(By.CSS_SELECTOR,"div.row.activeBtn > button") #选中正在开课
    classname_loc=(By.CSS_SELECTOR,"#classlist > tr > td[ftype='name']")
    detail_loc=(By.CSS_SELECTOR,"#classlist > tr > td.text-center > a")
    classtext_loc=(By.CSS_SELECTOR,"#page-content > div.fixes-top > div > div.container > div > div.col-sm-8.col-xs-12 > div.pull-left")
    classinfo_loc=(By.CSS_SELECTOR,"#endC > li:nth-child(2)")
    button_loc=(By.CSS_SELECTOR,"#exportBigTab > button")
    showtop_loc=(By.CSS_SELECTOR,"#showTop")
    def click_teaching(self):
        self.find_element(*self.teaching_loc).click()
    def click_classes(self):
        self.find_element(*self.classes_loc).click()
    def click_class(self):
        self.find_elements(self.class_loc)[2].click()
    def p_classname(self):
        return self.find_elements(self.classname_loc)[0].text
    def click_detail(self):
        self.find_elements(self.detail_loc)[0].click()
    def p_classtext(self):
        return self.find_element(*self.classtext_loc).text
    def click_classinfo(self):
        self.find_element(*self.classinfo_loc).click()
    def click_button(self):
        try:
            self.find_element(*self.button_loc).click()
        except:
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.get_screenshot_as_file('%s.jpg' % nowTime)       
    def click_showtop(self):
        self.find_element(*self.showtop_loc).click()
        
class UploadClass(BasePage.Action):
    teaching_loc=(By.CSS_SELECTOR,"#primary-nav > ul > li:nth-child(3) > a")
    asset_loc=(By.CSS_SELECTOR,"#primary-nav>ul>li:nth-child(3)>ul>li:qwwnth-child(2)> a")
    input_loc=(By.CSS_SELECTOR,"input.btn.btn-primary")

    def click_teaching(self):
        self.find_element(*self.teaching_loc).click()
    def click_classes(self):
        self.find_element(*self.asset_loc).click()
    def click_input(self):
        self.find_element(*self.input_loc).click()













