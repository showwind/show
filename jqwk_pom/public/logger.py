# coding:utf-8
import logging
import os.path
import time

class Logger(object):
	def __init__(self,log_path="logs\\"):
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		self.formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(funcName)s- %(levelname)s: %(message)s')
		self.log_path=log_path
	def log_file(self,level=logging.INFO):
		nowTime=time.strftime("%Y_%m_%d_%H_%M_%S")
		log_path=os.path.join(os.path.dirname(os.getcwd()),self.log_path)
		log_name=log_path+nowTime+'.log'
		fh=logging.FileHandler(log_name)
		fh.setLevel(level)
		fh.setFormatter(self.formatter)
		self.logger.addHandler(fh)
	def console(self, level=logging.INFO):
		ch=logging.StreamHandler()
		ch.setLevel(level)
		ch.setFormatter(self.formatter)
		self.logger.addHandler(ch)

	def log(self):
		self.log_file()
		self.console()
		return self.logger
'''
if __name__ == "__main__":
	log = Logger().log()
	log.info("打开浏览器")
	log.info("登录")
	log.warning("警告！")
	log.error("异常")
'''

