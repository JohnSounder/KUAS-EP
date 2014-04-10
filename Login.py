# -*- coding: utf-8 -*-

import collections

import requests

from lxml import etree

ACTIVE_URL="http://ep.kuas.edu.tw/EPortfolio/Activity/ActivitySystem.aspx"
POST_URL = "http://ep.kuas.edu.tw/EPortfolio/EPDefaultPage.aspx"

username     = "1102108131"
password     = ""

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

session = None


def Login():
    global session

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
        session = session
        return 1
    else:
        return 0


def is_login():
    return 1 if session else 0