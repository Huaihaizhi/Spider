import requests
from bs4 import BeautifulSoup
from PIL import Image
import time
import urllib
import json

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
url='https://www.zhihu.com/#signin'
session=requests.session()
soup=BeautifulSoup(session.get(url,headers=headers).text,'lxml')
xsrf=soup.find_all('input',type="hidden")[0]['value']
print(xsrf)
number=input('输入账号：')
passwd=input('输入密码：')
t = str(int(time.time()*1000))
captcha_url='https://www.zhihu.com/captcha.gif?r='+t+'&type=login&lang=cn'
r=session.get(captcha_url,headers=headers)
print(r)
with open('captcha.jpg','wb') as f:
	f.write(r.content)
im=Image.open('captcha.jpg')
im.show()
im.close()
num=input('请输入有几个汉字颠倒：')
l=[]
dic=dict()
dic["img_size"]=[200,44]
if int(num)==1:
	n=input('请输入第几个汉字颠倒：')
	list=[21*int(n)+int(n),21.6094]
	l.append(list)
	#click1=session.post('https://zhihu-web-analytics.zhihu.com/api/v1/logs/batch',data={},headers=headers)
	dic["input_points"]=l
	dic=json.dumps(dic)
	postdata={
		'_xsrf':xsrf,
		'password':passwd,
		'captcha':dic,
		'captcha_type':'cn',
		'phone_num':number
	}
if int(num)==2:
	n=input('请输入第1个颠倒的汉字的顺序：')
	l.append([21*int(n)+int(n),21.6094])
	#click1=session.post('https://zhihu-web-analytics.zhihu.com/api/v1/logs/batch',data={},headers=headers)
	n=input('请输入第2个颠倒的汉字的顺序：')
	l.append([21*int(n)+int(n),21.6094])
	#click1=session.post('https://zhihu-web-analytics.zhihu.com/api/v1/logs/batch',data={},headers=headers)
	dic["input_points"]=l
	dic=json.dumps(dic)
	postdata={
		'_xsrf':xsrf,
		'password':passwd,
		'captcha':dic,
		'captcha_type':'cn',
		'phone_num':number
		}

# postdata=urllib.parse.urlencode(postdata).encode()
print(postdata)
res=session.post('https://www.zhihu.com/login/phone_num',data=postdata,headers=headers)
print(res.text)		
r = session.get('http://www.zhihu.com/',headers=headers)  
print(r.text) 

# {"img_size":[200,44],"input_points":l}
# https://www.zhihu.com/captcha.gif?r=1507957379288&type=login&lang=cn
# t = str(int(time.time()*1000))
# https://zhihu-web-analytics.zhihu.com/api/v1/logs/batch
# https://zhihu-web-analytics.zhihu.com/api/v1/logs/batch
# https://zhihu-web-analytics.zhihu.com/api/v1/logs/batch