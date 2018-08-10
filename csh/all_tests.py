#coding=utf-8
import unittest 
import HTMLTestRunner
import os,time
case_dir='E:\\test\\csh\\test_case' 
def creatsuitel(): 
	testcase=unittest.TestSuite() 
	discover=unittest.defaultTestLoader.discover(case_dir, 
		pattern ='test_*.py', 
		top_level_dir=None)
	for test_suite in discover: 
		for test_case in test_suite: 
			testcase.addTest(test_case) #testcase.addTests()报错failtest
	#print (testcase)
	return testcase

#定义个报告存放路径，支持相对路径 
if __name__=="__main__":
	now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
	filename = 'E:\\test\\csh\\report\\result.html'  
	fp = open(filename,'wb')
	runner =HTMLTestRunner.HTMLTestRunner( 
		stream=fp, 
		title=u'测试报告', 
		description=u'用例执行情况：')
	runner.run(creatsuitel())
	fp.close()