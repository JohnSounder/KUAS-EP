#coding=UTF8

import time
import re
import collections
import requests,uniout
from lxml import etree
import json
import _core


##################################################
# Settings
##################################################

def Search():
	try:
		session = requests.session()
		response = session.get(_core.ACTIVE_URL , headers = _core.headers)
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
	response = session.post(_core.ACTIVE_URL , data = payload, headers = _core.headers)

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

