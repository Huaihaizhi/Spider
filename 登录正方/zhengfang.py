import requests
from bs4 import BeautifulSoup
from PIL import Image

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
url='http://202.119.225.34/default2.aspx'
session=requests.session()
res=session.get(url,headers=headers)
soup=BeautifulSoup(res.text,'lxml')
viewstate=soup.find_all('input',type="hidden")[0]['value']
username=input('输入用户名：')
password=input('输入密码：')

captcha_url=soup.find_all('img',id='icode')[0]['src']
captcha_url='http://202.119.225.34/'+captcha_url
with open('captcha.jpg','wb') as f:
	f.write(session.get(captcha_url,headers=headers).content)
image=Image.open('captcha.jpg')
image.show()
image.close()
captcha=input('请输入验证码：')
postdata={
		'__VIEWSTATE':viewstate,
		'txtUserName':username,
		'Textbox1':'',
		'TextBox2':password,
		'txtSecretCode':captcha,
		'RadioButtonList1':'(unable to decode value)',
		'Button1':'',
		'lbLanguage':'',
		'hidPdrs':'',
		'hidsc':''
	}

res=session.post(url,data=postdata,headers=headers)
print(res.text)


