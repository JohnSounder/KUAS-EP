#-*- coding=utf-8 -*-
import _core
import requests
import collections
from bs4 import BeautifulSoup
from lxml import etree
session = requests.session()
uid = "1102108132"
pwd = "4756"
def login():
	hiddenfield = BeautifulSoup(session.get( _core.POST_URL, headers = _core.headers).text).select('input[type="hidden"]')
	postData = {
		"ctl00$LoginForm1$TbLoginId" : uid,
		"ctl00$LoginForm1$TbLoginPW" : pwd,
		"ctl00$LoginForm1$BtLogin" : "登入"
	}
	for i in hiddenfield:
		if i['name'] == '__VIEWSTATE' or i['name'] == '__EVENTVALIDATION' :
			postData[i['name']] = i['value']
	response = BeautifulSoup(session.post( _core.POST_URL, data = postData, headers = _core.headers).text)
	return session

def search( session ):
	session = requests.session()
	hidden = BeautifulSoup(session.get( _core.ACTIVE_URL, headers = _core.headers).content).select('input[type=hidden]')

	payload = collections.OrderedDict()
	raw_data = ['ContentPlaceHolder1_ContentPlaceHolder1_ToolkitScriptManager1_HiddenField',';;AjaxControlToolkit, Version=4.1.51116.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:zh-TW:fd384f95-1b49-47cf-9b47-2fa2a921a36a:de1feab2:f9cec9bc:a0b0f951:a67c2700:fcf0e993:f2c8e708:720a52bf:589eaa30:698129cf:fb9b4c57:ccb96cf9','__EVENTTARGET', 'ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$TabContainer1$OnLinePanel$APCOnLine$lbShowAll','__EVENTARGUMENT','','ContentPlaceHolder1_ContentPlaceHolder1_TabContainer1_ClientState','{"ActiveTabIndex":2,"TabState":[true,true,true,true]}']

	for x in xrange(0,len(raw_data),2):
		payload[raw_data[x]] = raw_data[x+1]
	for i in hidden:
		if i['name'] == '__VIEWSTATE' or i['name'] == '__EVENTVALIDATION':
			payload[i['name']] = i['value']
	#Change Tab
	AllActive = session.post( _core.ACTIVE_URL, data = payload, headers = _core.headers)
	print AllActive.text
	bs = BeautifulSoup(AllActive.text)
	print bs
	#for x in payload:
		#print x + "," + payload[x]

if __name__ == '__main__':
	search(login())