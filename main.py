# -*- coding: utf-8 -*-
import _core
import requests
from bs4 import BeautifulSoup
uid = "1102108132"
pwd = "4756"
session = requests.session()
def login ():
	hiddenfield = BeautifulSoup(session.get( _core.POST_URL, headers = _core.headers).text)
	field = hiddenfield.select('input[type="hidden"]')
	#print field
	postData = {
		"ctl00$LoginForm1$TbLoginId" : uid,
		"ctl00$LoginForm1$TbLoginPW" : pwd,
		"ctl00$LoginForm1$BtLogin" : "登入"
	}
	for i in field:
		if i['name'] == '__VIEWSTATE' or i['name'] == '__EVENTVALIDATION' :
			postData[i['name']] = i['value']
	#Repost
	response = BeautifulSoup(session.post( _core.POST_URL, data = postData, headers = _core.headers).text)
	return session

def search ( session ) :
	selectfield = BeautifulSoup(session.get( _core.ACTIVE_URL, headers = _core.headers).text).select('select')
	textfield = BeautifulSoup(session.get( _core.ACTIVE_URL, headers = _core.headers).text).select('input[type=text]')
	hiddenfield = BeautifulSoup(session.get( _core.ACTIVE_URL, headers = _core.headers).text).select('input[type=hidden]')
	postData = {}
	rawdata = ['ContentPlaceHolder1_ContentPlaceHolder1_ToolkitScriptManager1_HiddenField',';;AjaxControlToolkit, Version=4.1.51116.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:zh-TW:fd384f95-1b49-47cf-9b47-2fa2a921a36a:de1feab2:f9cec9bc:a0b0f951:a67c2700:fcf0e993:f2c8e708:720a52bf:589eaa30:698129cf:fb9b4c57:ccb96cf9','__EVENTTARGET', 'ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$TabContainer1','__EVENTARGUMENT','activeTabChanged:0',]
	for i in xrange(0 ,len(rawdata), 2):
		postData[rawdata[i]] = rawdata[i+1]

	for i in selectfield:
		postData[i['name']] = ""

	for i in textfield:
		postData[i['name']] = ""

	for i in hiddenfield:
		if i.has_attr('value') :
			postData[i['name']] = i['value']
		else :
			postData[i['name']] = ""


	postData['ContentPlaceHolder1_ContentPlaceHolder1_TabContainer1_ClientState'] = '{"ActiveTabIndex":0,"TabState":[true,true,true,true,true]}'
	postData['ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$BTQuery'] = "查詢"
	postData['ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DateTimeBox1$DateFieldBox'] = "2014/02/17"
	postData['ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$DateTimeBox2$DateFieldBox'] = "2014/06/30"
	response = BeautifulSoup(session.post( _core.ACTIVE_URL, data = postData, headers = _core.headers).text)
	print response
	
	for x in postData:
		print x + "," + postData[x]

if __name__ == '__main__':
	#login()
	search(login())
