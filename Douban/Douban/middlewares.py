# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64
import random
from Douban.settings import USER_AGENTS
from Douban.settings import PROXIES


class RandomUserAgent(object):
    def process_request(self,request,spider):
        useragent=random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent',useragent)


class RandomProxy(object):
    def process_request(self,request,spider):
        proxy=random.choice(PROXIES)
        if proxy['user_passwd'] is None:
            request.meta['proxy']='http://'+proxy['ip_port']
        else:
            request.meta['proxy']='http://'+proxy['ip_port']
            print(proxy['user_passwd'])
            base64_userpasswd=base64.b64encode(proxy['user_passwd'].encode('utf-8'))
            request.headers['Proxy-Authorization']='Basic '+base64_userpasswd.decode('utf-8')

