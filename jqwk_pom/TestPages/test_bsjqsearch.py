#coding=utf-8
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
r=requests.get("http://www.jqwk.com/course")
jqwk=r.content
soup=BeautifulSoup(jqwk,"html.parser")
kecheng=soup.find_all(class_='col-lg-8')

for i in kecheng:
	print (i.h3.string,i.p.span.contents[1],i.p.contents[3].contents[0],i.p.contents[5].contents[0])
'''
ic=soup.find(class_='col-lg-8')
print (len(ic.contents))
for i in ic.contents:
	print (i)
print (ic.contents[0])
print (ic.contents[1])

ab=soup.find(class_='col-lg-8')
print (len(list(ab.children)))
print (len(list(ab.descendants)))
for i in ab.descendants:
	print (i)
'''
