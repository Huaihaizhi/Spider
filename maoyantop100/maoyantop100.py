#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import re
from requests.exceptions import RequestException
import json
def get_html(url):
    try:
        res=requests.get(url)
        if res.status_code==200:
            return res.text
        return None
    except RequetException:
        return None
    return res
def get_wanted(html):
    rex=re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    wanted=re.findall(rex,html)
    for item in wanted:
        yield {
            'index':item[0],
            'image':item[1],
            'name':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
        }

def write_to_file(content):
    with open('D://Spider/maoyantop100/result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()
        


def main(offset):
    url='https://maoyan.com/board/4?offset='+str(offset)
    html=get_html(url)
    for item in get_wanted(html):
        print(item)
        write_to_file(item)
   

if __name__=='__main__':
    for i in range(10):
        main(i*10)
    