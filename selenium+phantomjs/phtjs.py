from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


driver=webdriver.PhantomJS()
driver.get('https://www.douyu.com/directory/game/LOL')
driver.save_screenshot('aq.png')
while True:
	soup=BeautifulSoup(driver.page_source,'lxml')
	numbers=soup.find_all('span',{'class':'dy-num fr'})
	names=soup.find_all('span',{'class':'dy-name ellipsis fl'})
	for number,name in zip(numbers,names):
		print('number:'+number.get_text().strip()+',name:'+name.get_text().strip())
	if BeautifulSoup(driver.page_source,'lxml').find('shark-pager-next shark-pager-disable shark-pager-disable-next'):
		break
	driver.find_element_by_class_name('shark-pager-next').click()
	





# number:span class_="dy-num fr"
# name:span class_="dy-name ellipsis fl"
# class="shark-pager-next"