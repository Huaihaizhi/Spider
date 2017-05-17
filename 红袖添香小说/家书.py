#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
url='http://novel.hongxiu.com/a/1430715/13248256.html'
def get_txt(url):
    res=requests.get(url).text
    soup=BeautifulSoup(res,'html.parser')
    title=soup.select('.h1title h1')[0].text
    txt=soup.select('#htmlContent p')
    print(title)
    for txts in txt:
        print(txts.text)


for n in range(27):
    print('该章网址：',url)
    get_txt(url)
    print('\n')
    res=requests.get(url).text
    soup=BeautifulSoup(res,'html.parser')
    m=soup.select('#htmlxiazhang')[0].get('href')
    new_url=str('http://novel.hongxiu.com'+m)
    url=str('http://novel.hongxiu.com'+m)
   