import requests

url="http://www.jqwk.com/login"
headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
s=requests.session()
r=s.get(url,headers=headers,verify=False)
print (s.cookies)
c=requests.cookies.RequestsCookieJar()
c.set('name','yonghu1')
c.set('password','5f388b64ec0924c87f08304406ae2f4d')
s.cookies.update(c)
print (s.cookies)

url1="http://www.jqwk.com/myclasses/setvideotime"
body={
	"classId":"409",
	"sectionId":"11372",
	"time":"2017-07-15"
}
r2=s.post(url1,data=body,verify=False)
print (r2.content)
