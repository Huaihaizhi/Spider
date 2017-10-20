import requests
from bs4 import BeautifulSoup
from PIL import Image
import time
import urllib

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
session=requests.session()
soup=BeautifulSoup(session.get('https://www.zhihu.com/#signin',headers=headers).text,'lxml')
xsrf=soup.find_all('input',type="hidden")[0]['value']
print(xsrf)
number=input('输入账号：')
passwd=input('输入密码：')
t = str(int(time.time()*1000))
captcha_url='https://www.zhihu.com/captcha.gif?r='+t+'&type=login&lang=en'
r=session.get(captcha_url,headers=headers)
print(r)
with open('captcha.jpg','wb') as f:
	f.write(r.content)
im=Image.open('captcha.jpg')
im.show()
im.close()
dic=input('请输入验证码：')
postdata={
		'_xsrf':xsrf,
		'email':number,
		'password':passwd,
		'captcha':dic
#		'captcha_type':'cn',
		
	}

print(postdata)
res=session.post('https://www.zhihu.com/login/email',data=postdata,headers=headers)
print(res.text)
r = session.get('http://www.zhihu.com/',headers=headers)  
print(r.text)