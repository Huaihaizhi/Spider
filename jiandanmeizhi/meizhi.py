#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
from requests.exceptions import RequestException
import json
from hashlib import md5
import os

def get_html(url):
    res=requests.get(url)
    return res.text

def parse_html(html):
    soup=BeautifulSoup(html,'html.parser')
    images_url=soup.select('p img')
    rex=re.compile('img src="(.*?)"/',re.S)
    for image in images_url:
        image_url=re.search(rex,str(image))
        if image_url:
            img_url='http:'+str(image_url.group(1))
            download_images(img_url)
        
def download_images(url):
    print('正在下载：',url)
    res=requests.get(url)
    save_images(res.content)
    
def save_images(content):
    filepath='{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(filepath):
        with open(filepath,'wb') as f:
            f.write(content)
            f.close()

    
def main(n):
    for i in range(1,n):
        url='http://jandan.net/ooxx/page-'+str(i)
        html=get_html(url)
        parse_html(html)
    
if __name__=='__main__':
	n=int(input('你想下载几页（共164页）：'))
	main(n)