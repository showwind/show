# coding:utf-8
from selenium import webdriver
# 加载Chrome配置
option = webdriver.ChromeOptions()
option.add_argument(r'--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data\Default')
driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(10)
driver.get("http://zbpf.jqweike.com/#/frontPage/index")