from scrapy import cmdline

name='douban_movie -o douban_moive.csv'
cmd='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())