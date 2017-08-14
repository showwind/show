#coding=utf-8
import unittest,time
from selenium import webdriver
from jqwk_pom.ElePages import ClassesPage
from jqwk_pom.public import  adminlogin

class_url="http://www.jqwk.com/academic/teaching/classes"
class Caseclass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        #cls.username ="admin11"
        #cls.password ="111111"

    def test_addclass(self):
        u'''新建班级'''
        self.driver.get(ClassesPage.admin_url)
        adminlogin.adminlogin(self)
        add_class=ClassesPage.AddClass(self.driver,ClassesPage.admin_url,u"教务管理平台")
        add_class.click_teaching()
        add_class.click_classes()
        add_class.click_addclass()
        add_class.input_classname(u"5班")
        add_class.click_classicon()
        add_class.click_getcourse()
        add_class.input_searchkey(" ")
        add_class.click_subsearch()
        add_class.click_course()
        add_class.click_subchoice()
        add_class.click_choiceteacher()
        add_class.input_searchkey(u"张懵")
        add_class.click_subsearch()
        add_class.click_teacher()
        add_class.click_subchoice()
        add_class.click_assistant()
        add_class.input_searchkey(u"张懵")
        add_class.click_subsearch()
        add_class.click_teacher()
        add_class.click_subchoice()
        add_class.input_learnstart()
        add_class.input_learnend()
        add_class.input_examtimestart()
        add_class.input_examtimeend()
        add_class.click_next()
        add_class.click_openqa()
        add_class.click_teacherid("10568")
        add_class.click_issethomework()#可注释变为不布置作业
        add_class.click_ischeckofwork()
        add_class.click_homeworkteacher("10568")
        add_class.click_next()
        add_class.input_searchstudent(u"郭信林")
        add_class.click_student()
        add_class.click_choiceall()
        add_class.click_subchoicestudent()
        add_class.click_over()
        assert add_class.text_edit(),u"5班"
        add_class.click_classes()
    def test_importclasses(self):
        import_classes=ClassesPage.ImportClasses(self.driver,class_url,u"教务管理平台")
        import_classes.click_importclass()
        import_classes.input_filename(r"E:\test\jqwk_pom\report\import_classes.xlsx")
        import_classes.click_submit()
        import_classes.click_classes()
        print (import_classes.p_class())
        import_classes.click_class()
        assert import_classes.p_class(),u"计算机2班PPT"
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()