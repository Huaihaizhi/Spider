# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem



class DongguanspiderSpider(CrawlSpider):
    name = 'dongguanspider'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/huiyin?page=0']
    page_link=LinkExtractor(allow=r'page=\d+')
    page_second=LinkExtractor(allow=r'/question/\d+/\d+.shtml')
    rules=[
    Rule(page_link),
    Rule(page_second,callback='parse_item')
    ]

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse_item(self, response):
        item=DongguanItem()
        #/html/body/div[6]/div/div[1]/div[1]/strong
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item['title']=response.xpath("//div[@class='cleft']/strong[@class='tgray14']/text()").extract()[0].split('\xa0\xa0')[0].split(':')[-1]
        item['number']=response.xpath("//div[@class='cleft']/strong[@class='tgray14']/text()").extract()[0].split('\xa0\xa0')[-2].split(':')[-1]
        content=response.xpath("//div[@class='contentext']/text()").extract()
        if len(content)==0:
            content=response.xpath("//div[@class='c1 text14_2']/text()").extract()
            item['content']=''.join(content).strip()
        else:
            content=response.xpath("//div[@class='contentext']/text()").extract()
            item['content']=''.join(content).strip()
        item['url']=response.url
        yield item
