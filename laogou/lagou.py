#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import xlwt

def get_page(page):
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
		'Cookie':'user_trace_token=20170926204559-a572b14b-a2b8-11e7-92e6-5254005c3644; LGUID=20170926204559-a572b4f7-a2b8-11e7-92e6-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEEAAJA6103003EB1ACAB3F88CD83ED3316B524; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=bzclk.baidu.com; PRE_SITE=http%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00f7Ghk60t8km0FNkUsaBCTVu00000aFBTNb00000v6QmjM.THL0oUhY0A3qrj6srHnzPH7xpA7EgLKM0ZnqrHDdPANhrjDsnj0sP1F9P0Kd5Hm3P1RdPRwarHcLfRmdwDn4wH9DPW9aPW6dn1TknRw70ADqI1YhUyPGujY1njfLnW63P1bdFMKzUvwGujYkP6K-5y9YIZK1rBtEILILQhk9uvqdQhPEUitOIgwVgLPEIgFWuHdVgvPhgvPsI7qBmy-bINqsmsKWThnqnHTkPWD%26tpl%3Dtpl_10085_15730_11224%26l%3D1500602914%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591%2525E5%2525AE%252598%2525E7%2525BD%252591-%2525E4%2525B8%252593%2525E6%2525B3%2525A8%2525E4%2525BA%252592%2525E8%252581%252594%2525E7%2525BD%252591%2525E8%252581%25258C%2525E4%2525B8%25259A%2525E6%25259C%2525BA%2526xp%253Did%28%252522m26faf71c%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D139%26ie%3Dutf-8%26f%3D8%26srcqid%3D1347229508931914265%26tn%3D88093251_hao_pg%26wd%3Dlagou%26oq%3Dlagou%26rqlang%3Dcn%26sc%3DUWY3rj04n1cdnNqCmyqxTAThIjYkPH0vPHDkrHn4Pj0vFhnqpA7EnHc1Fh7W5Hc4PHcLPHf3rHT%26ssl_sample%3Dnormal; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F%3Futm_source%3Dm_cf_cpt_baidu_pc; _gid=GA1.2.1365288860.1506517411; _ga=GA1.2.1721284191.1506429951; LGSID=20170927210336-45fd18bb-a384-11e7-9300-5254005c3644; LGRID=20170927210529-89b307d0-a384-11e7-9300-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1506517476,1506517486,1506517508,1506517516; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1506517525; TG-TRACK-CODE=search_code; SEARCH_ID=b975e746f45047deae49733f6b4d4ef8',
		'Referer':'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
	}
	data={
		'first':'false',
		'pn':page,
		'kd':'python'
	}
	url='https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0'
	res=requests.post(url,headers=headers,data=data)
	result=res.json()
	jobs=result['content']['positionResult']['result']
	return jobs
table=xlwt.Workbook()
sheet1=table.add_sheet('lagou',cell_overwrite_ok=True)
sheet1.write(0,0,'公司id')
sheet1.write(0,1,'岗位id')
sheet1.write(0,2,'涉及领域')
sheet1.write(0,3,'文化程度')
sheet1.write(0,4,'工作经验')
sheet1.write(0,5,'工作地')
sheet1.write(0,6,'工作岗位')
sheet1.write(0,7,'公司规模')
sheet1.write(0,8,'公司简称')
sheet1.write(0,9,'工作性质')
sheet1.write(0,10,'工作区域')
sheet1.write(0,11,'公司全称')
sheet1.write(0,12,'薪水')
i=1
for page in range(1,31):
	for job in get_page(page=page):
		sheet1.write(i,0,job['companyId'])
		sheet1.write(i,1,job['positionId'])
		sheet1.write(i,2,job['industryField'])
		sheet1.write(i,3,job['education'])
		sheet1.write(i,4,job['workYear'])
		sheet1.write(i,5,job['city'])
		sheet1.write(i,6,job['positionName'])
		sheet1.write(i,7,job['companySize'])
		sheet1.write(i,8,job['companyShortName'])
		sheet1.write(i,9,job['jobNature'])
		sheet1.write(i,10,job['district'])
		sheet1.write(i,11,job['companyFullName'])
		sheet1.write(i,12,job['salary'])
		print(i)
		i+=1
table.save('lagou.xls')