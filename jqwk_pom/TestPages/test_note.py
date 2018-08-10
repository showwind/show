#coding=utf-8
import unittest,time
from selenium import webdriver
from jqwk_pom.ElePages import NotePage
from jqwk_pom.public import  login
import  HTMLTestRunner

class Casenote(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.username ="luhong"
        cls.password ="111111"
    def test_addnote(self):
        u'''添加笔记'''
        self.driver.get(NotePage.note_url)
        login.user_login(self,self.username,self.password)
        add_note=NotePage.NotePage(self.driver,NotePage.note_url,u"金桥微课 - Index")
        add_note.click_close()
        add_note.click_list()
        add_note.click_course()
        add_note.click_note()
        add_note.type_note("123456")
        add_note.click_submit()
    #@unittest.skipUnless(...,u"为False的时候跳过")
    def test_updatenote(self):
        u'''编辑笔记'''
        update_note=NotePage.UpdateNote(self.driver,NotePage.note_url,u"金桥微课 - Index")
        update_note.click_upuser()
        update_note.click_uplist()
        update_note.click_upnote()
        update_note.click_upnotelist()
        update_note.type_upnotecontent("yiqiwanba")
        update_note.click_submit()
        update_note.click_upnote()
        t=update_note.note_t()
        assert t,"yiqiwanba"
    #@unittest.skipUnless(...,u"为False的时候跳过")
    def test_zdeletenote(self):
        u'''删除笔记'''
        delete_note=NotePage.DeleteNote(self.driver,NotePage.note_url,u"金桥微课 - Index")
        delete_note.click_deluser()
        delete_note.click_dellist()
        delete_note.click_note()
        delete_note.click_delnote()
        delete_note.click_del()
        time.sleep(2)
        t=delete_note.note_del()
        #self.assertNotEqual(self,t,"yiqiwanba")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()
    '''
    testunit=unittest.TestSuite()
    testunit.addTest(Casenote("test_addnote"))
    testunit.addTest(Casenote("test_updatenote"))
    testunit.addTest(Casenote("test_zdeletenote"))
    fp=file('D:\\test\\jqwk_pom\\report\\result.html','wb')
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,
                                          title=u'测试报告',
                                          description=u'用例执行情况：')
    #运行测试用例
    runner.run(testunit)
    fp.close()
    '''




