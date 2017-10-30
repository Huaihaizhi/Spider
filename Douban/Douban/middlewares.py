# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
from Douban.settings import USER_AGENTS
from Douban.settings import PROXIES


class RandomUserAgent(object):
    def process_request(self,request,spider):
        useragent=random.choice(USER_AGENTS)
        print(useragent)
