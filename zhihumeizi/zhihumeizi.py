#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
import re
import json
from hashlib import md5
import os
def get_url(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    html=requests.get(url,headers=headers).text
    soup=BeautifulSoup(html,'html.parser')
    url1=soup.select('link')
    return url1

def parser_detail(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }
    html=requests.get(url,headers=headers).text
    soup=BeautifulSoup(html,'html.parser')
    image=soup.select('img')
    return image
    
    
def download_images(url):
    print('正在下载：',url)
    try:
        res=requests.get(url)
        if res.status_code==200:
            save_images(res.content)
        return None
    except RequestException:
        print('下载图片出错!',url)
        return None
    
def save_images(content):
    filepath='{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(filepath):
        with open(filepath,'wb') as f:
            f.write(content)
            f.close()
    

if __name__=='__main__':
	for x in range(5): 
	    url='https://www.zhihu.com/collection/38624707?page='+str(x)
	    url2=get_url(url)
	    rex=re.compile('<link href="(.*?)" itemprop="url"/>',re.S)
	    for j in range(len(url2)):
	        url4=re.search(rex,str(url2[j]))
	        if url4:
	            url='https://www.zhihu.com'+url4.group(1)
	            image=parser_detail(url)
	            for n in range(len(image)):
	                rex1=re.compile('src="(.*?)".*?/>',re.S)
	                data=re.search(rex1,str(image[n]))
	                if data:
	                    print(data.group(1))
	                    download_images(data.group(1))