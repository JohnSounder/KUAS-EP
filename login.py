#!/usr/bin/env python
# -*- coding: utf-8 -*-

#coding=UTF8

import time
import re
import collections
import requests
import uniout

from lxml import etree



##################################################
# Settings
##################################################


MAIN_URL = "http://ep.kuas.edu.tw/"
POST_URL = "http://ep.kuas.edu.tw/EPortfolio/EPDefaultPage.aspx"
ACTIVE_URL="http://ep.kuas.edu.tw/EPortfolio/Activity/ActivitySystem.aspx"

username     = "1102108131"
password     = "6019"

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
headers['Accept'] = "zh-tw,en-us;q=0.7,en;q=0.3"
headers['Accept-Encoding'] = "gzip, deflate"
headers['Referer'] = "http://ep.kuas.edu.tw/EPortfolio/EPDefaultPage.aspx"
headers['Connection'] = "keep-alive"

def Login():
	try:
		session = requests.session()
		response = session.get(POST_URL , headers = headers)
	except Exception, e:
		raise e

	payload = collections.OrderedDict()
	raw_data = ['ctl00$LoginForm1$TbLoginId', username,
				'ctl00$LoginForm1$TbLoginPW', password,
				'ctl00$LoginForm1$BtLogin','登入']

	
	for x in xrange(0,len(raw_data),2):
		payload[raw_data[x]] = raw_data[x+1]
		
	root = etree.HTML(response.content)
	for i in root.xpath("//input"):
		if i.attrib['name'] == '__VIEWSTATE':
			payload['__VIEWSTATE'] = i.attrib['value']
		if i.attrib['name'] == '__EVENTVALIDATION':
			payload['__EVENTVALIDATION'] = i.attrib['value']
	
	
	# RePost Data
	response = session.post(POST_URL , data = payload, headers = headers)
	
	root = etree.HTML(response.text)
	result = root.xpath("//span[@id = 'LoginForm1_LbLoginName']")
	
	
	if result:
		#print u"Login Success! %s" % (result[0].text)
		#print response.request.headers['Cookie']
		return 1
	else:
		#print u"Login Falied!"
		return 0


if __name__ == '__main__':
	Login()
