#coding=UTF8

import time
import re
import collections
import requests
import uniout
from lxml import etree
import json


##################################################
# Settings
##################################################

ACTIVE_URL="http://ep.kuas.edu.tw/EPortfolio/Activity/ActivitySystem.aspx"

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
headers['Accept'] = "zh-tw,en-us;q=0.7,en;q=0.3"
headers['Accept-Encoding'] = "gzip, deflate"
headers['Referer'] = "http://ep.kuas.edu.tw/EPortfolio/EPDefaultPage.aspx"
headers['Connection'] = "keep-alive"

def Search():
	try:
		session = requests.session()
		response = session.get(ACTIVE_URL , headers = headers)
	except Exception, e:
		raise e

	payload = collections.OrderedDict()

	raw_data = ['__EVENTTARGET', 'ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$TabContainer1$OnLinePanel$APCOnLine$lbShowAll',
				'ContentPlaceHolder1_ContentPlaceHolder1_TabContainer1_ClientState','{"ActiveTabIndex":2,"TabEnabledState":[true,true,true,true],"TabWasLoadedOnceState":[false,false,true,false]}']

	for x in xrange(0,len(raw_data),2):
		payload[raw_data[x]] = raw_data[x+1]
		
	root = etree.HTML(response.content)
	for i in root.xpath("//input"):
		if i.attrib['name'] == '__VIEWSTATE':
			payload['__VIEWSTATE'] = i.attrib['value']
		if i.attrib['name'] == '__EVENTVALIDATION':
			payload['__EVENTVALIDATION'] = i.attrib['value']
	
	
	# RePost Data
	response = session.post(ACTIVE_URL , data = payload, headers = headers)

	root = etree.HTML(response.text)

        for i in root.xpath("//a[starts-with(@id, 'ContentPlaceHolder1_ContentPlaceHolder1_TabContainer1_PopularPanel_gvPopular_LBact_name_')]"):
        	print i.text
        for i in root.xpath("//a[starts-with(@id, 'ContentPlaceHolder1_ContentPlaceHolder1_TabContainer1_OnLinePanel_gvOnLine_LBact_name_')]"):
       	     print i.text
       	for i in root.xpath("//input[starts-with(@id, 'ContentPlaceHolder1_ContentPlaceHolder1_TabContainer1_OnLinePanel_gvOnLine_HFact_id_')]"):
			print i.attrib['value']

	return 
if __name__ == '__main__':
	Search()

