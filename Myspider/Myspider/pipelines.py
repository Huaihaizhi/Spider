# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MyspiderPipeline(object):
#     def process_item(self, item, spider):
#         return item
import json
class myspiderPipeline(object):
	def __init__(self):
		self.filename=open('itcast.json','w')

	def process_item(self,item,spider):
		jsontext=json.dumps(dict(item))
		self.filename.write(jsontext)

	def close_spider(self):
		self.filename.close()