# -*- coding: utf-8 -*-

import time
import re
import collections
import requests
from lxml import etree
import json
from bs4 import BeautifulSoup

##################################################
# Settings
##################################################

username     = "1102108131"
password     = ""

ACTIVE_URL="http://ep.kuas.edu.tw/EPortfolio/Activity/ActivitySystem.aspx"
POST_URL = "http://ep.kuas.edu.tw/EPortfolio/EPDefaultPage.aspx"

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
headers['Accept'] = "zh-tw,en-us;q=0.7,en;q=0.3"
headers['Accept-Encoding'] = "gzip, deflate"
headers['Referer'] = "http://ep.kuas.edu.tw/EPortfolio/EPDefaultPage.aspx"
headers['Connection'] = "keep-alive"

proxy = {
    'http':'192.168.1.82:8080',
    'https':'192.168.1.82:8080'
}

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
    response = session.post(POST_URL , data = payload)
    
    root = etree.HTML(response.text)
    result = root.xpath("//span[@id = 'LoginForm1_LbLoginName']")
    
    
    if result:
        return session
    else:
        return 0


def Search(session):
    try:
        session = requests.session()
        response = session.get(ACTIVE_URL , headers = headers)
    except Exception, e:
        raise e

    payload = collections.OrderedDict()

    raw_data = ['ContentPlaceHolder1_ContentPlaceHolder1_ToolkitScriptManager1_HiddenField',';;AjaxControlToolkit, Version=4.1.51116.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:zh-TW:fd384f95-1b49-47cf-9b47-2fa2a921a36a:de1feab2:f9cec9bc:a0b0f951:a67c2700:fcf0e993:f2c8e708:720a52bf:589eaa30:698129cf:fb9b4c57:ccb96cf9','__EVENTTARGET', 'ctl00$ctl00$ContentPlaceHolder1$ContentPlaceHolder1$TabContainer1$OnLinePanel$APCOnLine$lbShowAll','__EVENTARGUMENT','',
    'ContentPlaceHolder1_ContentPlaceHolder1_TabContainer1_ClientState','{"ActiveTabIndex":2,"TabState":[true,true,true,true]}']

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
    for i in root.xpath("//a[starts-with(@id, 'ContentPlaceHolder1_ContentPlaceHolder1_TabContainer1_OnLinePanel_gvOnLine_LBact_name_')]"):
        print i.text.encode('utf8')
    for i in root.xpath("//input[starts-with(@id, 'ContentPlaceHolder1_ContentPlaceHolder1_TabContainer1_OnLinePanel_gvOnLine_HFact_id_')]"):
        print i.attrib['value'].encode('utf8')



def main():
    
    url = "http://ep.kuas.edu.tw/EPortfolio/Activity/Activity.aspx?QS=QS&ActId="
    for x in xrange(72,4000):
        response = requests.get(url + str(x))
        bs = BeautifulSoup(response.content)
        for y in bs.findAll('span', id=re.compile("^ContentPlaceHolder1_ContentPlaceHolder1_fvActivities_Lbact_name")):
            print y.text.encode('utf8') + "*****" + str(x)

if __name__ == '__main__':
    Search(Login())