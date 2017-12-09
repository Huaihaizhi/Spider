# -*- coding:utf-8 -*-
import urllib.request 
from lxml import etree 
class jinyong(object):
    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36'}
    def request(self,url):
        req=urllib.request.Request(url,headers=self.headers)
        response=urllib.request.urlopen(req)
        content=etree.HTML(response.read())
        return content 
    def load_indexpage(self,url):
        content=self.request(url)
        book_list=content.xpath('//ul[@class="book_ul"]/li/p[@class="book_li_title"]/a')
        for item in book_list:
            full_url='http://www.jinyongwang.com'+item.xpath('./@href')[0]
            name=item.xpath('./text()')[0]
            print('正在下载'+name)
            self.load_secondpage(full_url,name)
            print('下载完毕'+name)

    def load_secondpage(self,url,name):
        content=self.request(url)
        chapter_list=content.xpath('//ul[@class="mlist"]/li/a/@href')
        for item in  chapter_list:
            full_url='http://www.jinyongwang.com'+item
            self.download(full_url,name)

    def download(self,url,name):
        content=self.request(url)
        content_list=content.xpath('//div[@class="vcon"]/p/text()')
        for item in content_list:
            self.write_to_txt(item,name)

    def write_to_txt(self,txt,name):
        filepath='{}.txt'.format(name)
        with open(filepath,'a+') as f:
            f.write('  '+txt+'\r\n')

if __name__=='__main__':
    url='http://www.jinyongwang.com/'
    jinyong=jinyong()
    jinyong.load_indexpage(url)


