# -*- coding: utf-8 -*-
import scrapy
from tencent_spider.items import TencentSpiderItem



class TencentspiderSpider(scrapy.Spider):
    name = 'tencentspider'
    allowed_domains = ['tencent.com']
    url='http://hr.tencent.com/position.php?&start='
    offset=0
    start_urls = [url+str(offset)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="odd"] | //tr[@class="even"]'):
        	item=TencentSpiderItem()
        	position_name=each.xpath('./td[1]/a/text()').extract()
        	position_link=each.xpath('./td[1]/a/@href').extract()
        	if each.xpath('./td[2]/text()').extract():
        		position_cate=each.xpath('./td[2]/text()').extract()
        	else:
        		position_cate=['']
        	position_number=each.xpath('./td[3]/text()').extract()
        	position_location=each.xpath('./td[4]/text()').extract()
        	position_time=each.xpath('./td[5]/text()').extract()

        	item['position_name']=position_name[0]
        	item['position_link']=position_link[0]
        	item['position_cate']=position_cate[0]
        	item['position_number']=position_number[0]
        	item['position_location']=position_location[0]
        	item['position_time']=position_time[0]

        	yield item

        if self.offset<2370:
        	self.offset+=10
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)