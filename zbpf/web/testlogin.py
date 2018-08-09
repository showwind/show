#coding:utf-8
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#class Login()
def login_zbpf(phone,psw):
	header={
	"Host": "softtone.jqweike.cn:8090",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
	"Accept": "application/json, text/plain, */*",
	"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
	"Accept-Encoding": "gzip, deflate",
	"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
	"Content-Length": "100",
	"Connection": "keep-alive"
	}
	body={
	"username":phone,
	"password":psw,
	"captcha":"64xw",
	"verify_hash":"k28c0ddp062bfmo56b4v418ba3",
	"isAjax":"true"
	}
	s = requests.session()
	login_url = "http://softtone.jqweike.cn:8090/v1/user/login"
	login_ret = s.post(login_url,headers=header,data=body)
	# 这里token在返回的json里，可以直接提取
	userdata=login_ret.json()
	print (userdata)
	udata=userdata["data"]
	token = userdata["access_token"]
	new_id=userdata["user_id"]
	#print (token)
	# 这是登录后发的一个post请求
	get_url = "http://zbpf.jqweike.com/frontPage/index?access_token="+str(token)+"&user_id="+str(new_id)
	#print (get_url)
	return get_url
def user_text(dr,name):
	username=WebDriverWait(dr,10).until(lambda x:x.find_element_by_css_selector("#app > div > div.pc-head > div > span"))
	user_text=username.text
	if user_text==name:
		print ("ok")
	else:
		print ("failed")
def login_all():
	for i in range(0,2):
		print (i)
		driver1=webdriver.Chrome()
		driver1.implicitly_wait(10)
		driver1.maximize_window()
		phone1="15196615488"
		psw1="111111"
		name1=u"九重花浓"
		phone2="18200385389"
		psw2="123456"
		name2="wind"
		url1=login_zbpf(phone1,psw1)
		driver1.get(url1)
		user_text(driver1,name1)
		driver2=webdriver.Chrome()
		driver2.implicitly_wait(10)
		driver2.maximize_window()
		url2=login_zbpf(phone2,psw2)
		driver2.get(url2)
		user_text(driver2,name2)
		driver1.quit()
		driver2.quit()
def login():
	driver=webdriver.Chrome()
	driver.implicitly_wait(10)
	driver.maximize_window()
	phone="18200385389"
	psw="123456"
	name="wind"
	url=login_zbpf(phone,psw)
	driver.get(url)
	user_text(driver,name)
	driver.quit()