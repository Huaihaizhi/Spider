# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DongguanPipeline(object):
	def __init__(self):
		self.filename=open('dongguan.csv','w',encoding='utf-8')


	def process_item(self, item, spider):
		txt=dict(item)
		self.filename.write(str(txt)+'\n')

	def close_spider(self):
		self.filename.close()
