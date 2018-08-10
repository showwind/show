#coding=utf-8
import unittest
import time
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
def add_case(case_path,rule):
	testunit=unittest.TestSuite()
	discover=unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
	for test_suite in discover:
		for test_case in test_suite:
			testunit.add_Tests(test_case)
			print (testunit)
	return testunit
def run_case(all_case,report_path):
	now=time.strftime("%Y_%m_%d%H_%M_%S")
	report_abspath=os.path.join(report_path,now+'result.html')
	fp=open(report_abspath,"wb")
	runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"测试情况")
	runner.run(all_case)
	fp.close()
def get_report_file(report_path):
	u'''获取最新报告'''
	lists=os.listdir(report_path)
	lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
	print (u'最新测试生成的报告：'+lists[-1])
	report_file=os.path.join(report_path,lists[-1])
	return report_file
def send_mail(sender,psw,receiver,smtpserver,report_file):
	u'''发送最新的测试报告内容'''
	with open(report_file,"rb") as f:
		mail_body=f.read()
	msg=MIMEMultipart()
	body=MIMEText(mail_body,_subtype='html',_charset='utf-8')
	msg['Subject'] = u"自动化测试报告"
	msg["from"] = sender
	msg["to"] = psw
	att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
	att["Content-Type"] = "application/octet-stream"
	att["Content-Disposition"] = 'attachment; filename= "report.html"'
	msg.attach(att)
	smtp = smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(sender, psw)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()
	print ('test report email has send out !')
if __name__ == "__main__":
	case_path = ""
	rule="test*.py"
	all_case=add_case(case_path,rule)
	report_path=""
	run_case(all_case,report_path)
	report_file=get_report_file(report_path)
	sender=""
	psw=""
	# 收件人多个时，中间用逗号隔开,如'a@xx.com,b@xx.com'
	receiver=""
	smtp_server = 'smtp.xxx.com'
	send_mail(sender, psw, receiver, smtp_server, report_file)
