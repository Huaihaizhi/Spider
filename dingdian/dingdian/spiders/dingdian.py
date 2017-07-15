#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from dingdian.items import DingdianItem

class Myspider(scrapy.Spider):
	name='dingdian'
	allowed_domains=['x23us.com']
	bash_url='http://www.x23us.com/class/'
	bashurl='.html'

	def start_requests(self):
		for i in range(1,11):
			url=self.bash_url+str(i)+'_1'+self.bashurl
			yield Request(url,self.parse)
		yield Request('http://www.x23us.com/quanben/1',self.parse)

	def parse(self,response):
		print(response.text)