# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from Myspider.items import MyspiderItem

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#aandroid']
    def parse(self, response):
        l=[]
        #with open('aq.html','w') as f:
            #f.write(response.body.decode('utf-8'))
        for each in response.xpath('//div[@class="li_txt"]'):
            item=MyspiderItem()
            name=each.xpath('./h3/text()').extract()
            title=each.xpath('./h4/text()').extract()
            info=each.xpath('./p/text()').extract()
            # print(name[0])
            # print(title[0])
            # print(info[0])
            item['name']=name[0]
            item['title']=title[0]
            item['info']=info[0]
            l.append(item)
        return l
