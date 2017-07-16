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
		max_num=BeautifulSoup(response.text,'lxml').find('div',class_='pagelink').find_all('a')[-1].get_text()
		bashurl=str(response.url)[:-7]
		for num in range(1,int(max_num)+1):
			url=bashurl+'_'+str(num)+self.bashurl
			yield Request(url,callback=self.get_name)

	def get_name(self,response):
		tds=BeautifulSoup(response.text,'lxml').find_all('tr',bgcolor='#FFFFFF')
		for td in tds:
			novelname=td.find('a').get_text()
			novelurl=td.find('a')['href']
			yield Request(novelurl,callback=self.get_chapterurl,meta={'name':novelname,'url':novelurl})

	def get_chapterurl(self,response):
		item=DingdianItem()
		item['name']=str(response.meta['name']).replace('\xa0','')
		item['novelurl']=response.meta['url']
		category=BeautifulSoup(response.text,'lxml').find('table').find('a').get_text()
		author=BeautifulSoup(response.text,'lxml').find('table').find_all('td')[2].get_text()
		
		serialstatus=BeautifulSoup(response.text).find('table').find_all('td')[5].get_text()
		serialnumber=BeautifulSoup(response.text).find('table').find_all('td')[3].get_text()
		item['category']=str(category).replace('/','')
		item['author']=str(author).replace('/','')
#		item['name_id']=name_id
		item['serialstatus']=str(serialstatus).replace('/','')
		item['serialnumber']=str(serialnumber).replace('/','')
		return item
