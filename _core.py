import time
import re
import collections
import requests
import uniout
from lxml import etree
import json

CONST_VALUE_TEST = 10

MAIN_URL = "http://ep.kuas.edu.tw/"
POST_URL = "http://ep.kuas.edu.tw/EPortfolio/EPDefaultPage.aspx"
ACTIVE_URL="http://ep.kuas.edu.tw/EPortfolio/Activity/ActivitySystem.aspx"


headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
headers['Accept'] = "zh-tw,en-us;q=0.7,en;q=0.3"
headers['Accept-Encoding'] = "gzip, deflate"
headers['Referer'] = "http://ep.kuas.edu.tw/EPortfolio/EPDefaultPage.aspx"
headers['Connection'] = "keep-alive"