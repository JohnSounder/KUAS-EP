#!/usr/bin/env python
# -*- coding: utf-8 -*-

#coding=UTF8

import _core


##################################################
# Settings
##################################################

username     = "Account"
password     = "Password"


def Login():
	try:
		session = requests.session()
		response = session.get(_core.POST_URL , headers = _core.headers)
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
	response = session.post(_core.POST_URL , data = payload, headers = _core.headers)
	
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

