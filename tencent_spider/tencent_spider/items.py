# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position_name=scrapy.Field()
    position_link=scrapy.Field()
    position_cate=scrapy.Field()
    position_number=scrapy.Field()
    position_location=scrapy.Field()
    position_time=scrapy.Field()
