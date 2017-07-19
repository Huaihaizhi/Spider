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
			novelname=td.find_all('a')[1].get_text()
			novelurl=td.find('a')['href']
			yield Request(novelurl,callback=self.get_chapterurl,meta={'name':novelname,'url':novelurl})

	def get_chapterurl(self,response):
		item=DingdianItem()
		item['name']=str(response.meta['name']).replace('\xa0','')
		item['novelurl']=response.meta['url']
		category=BeautifulSoup(response.text,'lxml').find('table').find('a').get_text()
		author=BeautifulSoup(response.text,'lxml').find('table').find_all('td')[1].get_text()
		bash_url=BeautifulSoup(response.text,'lxml').find('p',class_='btnlinks').find('a',class_='read')['href']
		name_id=str(bash_url)[-6:-1].replace('/','')
		serialstatus=BeautifulSoup(response.text).find('table').find_all('td')[2].get_text()
		serialnumber=BeautifulSoup(response.text).find('table').find_all('td')[4].get_text()
		item['category']=str(category).replace('/','')
		item['author']=str(author).replace('\xa0','')
		item['name_id']=name_id
		item['serialstatus']=str(serialstatus).replace('\xa0','')
		item['serialnumber']=str(serialnumber).replace('\xa0','')
		yield item
		yield Request(url=bash_url,callback=self.get_chapter,meta={'name_id':name_id})

	def get_chapter(self,response):
		urls=re.findall(r'<td class="L"><a href="(.*?)">(.*?)</a></td>',response.text)
		num=0
		for url in urls:
			num=num+1
			chapterurl=response.url+url[0]
			chaptername=url[1]
			yield Request(chapterurl,callback=self.get_chaptercontent,meta={'num':num,'name_id':response.meta['name_id'],'chaptername':chaptername,'chapterurl':chapterurl})

	def get_chaptercontent(self,response):
		item=DcontentItem()
		item['num']=response.meta['num']
		item['id_name']=response.meta['name_id']
		item['chaptername']=str(response.meta['chaptername']).replace('\xa0','')
		item['chapterurl']=response.meta['chapterurl']
		content=BeautifulSoup(response.text,'lxml').find('dd',id='contents').get_text()
		item['chaptercontent']=str(content).replace('\xa0','')
		return item