#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.parse import urlencode
from requests.exceptions import RequestException
import requests
from bs4 import BeautifulSoup
import json
import re
from hashlib import md5
import os

def get_page_index(offset,keyword):
    header={
        'offset':offset,
        'format':'json',
        'keyword':keyword,
        'autoload':'true',
        'count':'20',
        'cur_tab':3
    }
    url='https://www.toutiao.com/search_content/?'+urlencode(header)
    try:
        res=requests.get(url)
        if res.status_code==200:
            return res.text
        return None
    except RequestException:
        print('请求索引页失败!')
        return None

def parse_page_index(html):
    data=json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')
            
def get_page_detail(url):
    try:
        res=requests.get(url)
        if res.status_code==200:
            return res.text
        return None
    except RequestException:
        print('请求详情页出错!')
        return None
    
def parse_page_detail(html,url):
    soup=BeautifulSoup(html,'html.parser')
    title=soup.select('title')[0].get_text()
    print(title)
    rex=re.compile('var gallery = (.*?);',re.S)
    image=re.search(rex,html)
    if image:
        data=json.loads(image.group(1))
        if data and 'sub_images' in data.keys():
            sub_images=data.get('sub_images')
            images=[item.get('url') for item in sub_images]
            for image in images:
                download_images(image)
            return {
                'title':title,
                'url':url,
                'images':images
            }
        
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
    
    
def main(offset):
    html=get_page_index(offset,'街拍')
    for url in parse_page_index(html):
        html=get_page_detail(url)
        if html:
            result=parse_page_detail(html,url)
            print(result)
if __name__=='__main__':
    for i in range(5):
    	main(i*20)