# -*- coding: utf-8 -*-

import requests
from lxml import etree
import login

if __name__ == '__main__':
    if login.Login():
        response = requests.get(login.ACTIVE_URL , headers = login.headers)
        root = etree.HTML(response.text)
    
        for i in root.xpath("//a[starts-with(@id, 'ContentPlaceHolder1_ContentPlaceHolder1_TabContainer1_PopularPanel_gvPopular_LBact_name_')]"):
            print i.text
      
