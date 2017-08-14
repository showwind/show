#coding=utf-8
import unittest,time
from selenium import webdriver
from jqwk_pom.ElePages import ClassesPage
from jqwk_pom.public import  adminlogin

upuser_loc="http://www.jqwk.com/academic/teaching/classes"
class CaseOptionclass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get(ClassesPage.admin_url)
        #cls.username ="admin11"
        #cls.password ="111111"
        adminlogin.adminlogin(cls)
    def test_editclass(self):
        u'''编辑班级'''        
        edit_class=ClassesPage.EditClass(self.driver,ClassesPage.admin_url,u"教务管理平台")
        edit_class.click_teaching()
        edit_class.click_classes()
        print (edit_class.text_class())
        edit_class.click_willclass()
        time.sleep(1)
        print (edit_class.text_class())
        edit_class.click_edit()
        edit_class.input_classname(u"软工5班")
        edit_class.click_next()
        edit_class.click_next()
        edit_class.click_over()
        edit_class.click_classes()

    def test_zdeleteclass(self):
        delete_class=ClassesPage.DeleteClasses(self.driver,ClassesPage.admin_url,u"教务管理平台")
        #delete_class.click_teaching()
        #delete_class.click_classes()
        print (delete_class.text_class())
        delete_class.click_willclass()
        time.sleep(1)
        print (delete_class.text_class())
        delete_class.click_deleteclass()
        delete_class.click_comfirm()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()