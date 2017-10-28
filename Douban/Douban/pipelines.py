# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class DoubanPipeline(object):
	def __init__(self):
		host=settings['MONGDB_NAME']
		port=settings['MONGDB_PORT']
		dbname=settings['MONGDB_DBNAME']
		sheetname=settings['MONGDB_SHEETNAME']

		client=pymongo.MongoClient(host,port)
		mydb=client[dbname]
		self.post=mydb[sheetname]

	def process_item(self,item,spider):
		data=dict(item)
		self.post.insert(data)
		return item