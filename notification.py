# -*- coding: utf-8 -*-

import os
import json
import time
import smtplib
import subprocess

from jinja2 import Environment, FileSystemLoader

import main

from email.mime.text import MIMEText

MAILING_LIST = ["1102108116@kuas.edu.tw", "grapherd@gmail.com"]
JSON_FILE = "activity.json"
OLD_JSON_FILE = "old_activity.json"
STATUS_TYPE = {u"報名截止": 0, u"人數已滿": 0, u"報名": 1, u"報名尚未開始": 2}

today = time.strftime("%Y/%m/%d")

def day_compare(a, b):
    a_year, a_month, a_day = list(map(lambda x: int(x), a.split("/")))
    b_year, b_month, b_day = list(map(lambda x: int(x), b.split("/")))

    return a_year >= b_year and a_month >= b_month and a_day >= b_day


def filter_compare(result):
    filter_result = {}

    for i in result:
        item = result[i]
        if (day_compare(item['date'], today) and day_compare(item['end_sign_up_date'], today) 
                and STATUS_TYPE[item['status']]):
            filter_result[int(i)] = item

    return filter_result
            

def send_mail(result, old_result=None):
    result_id = set(result)

    user = "grado123123@hotmail.com.tw"
    pwd = ""
    smtpserver = smtplib.SMTP("smtp.live.com")
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(user, pwd)

    env = Environment()
    env.loader = FileSystemLoader('.')

    template = env.get_template("notification.template")


    msg = MIMEText(template.render(result=result, old_result=old_result).encode('utf-8'), "html")
    msg['Subject'] = u"%s - EP 講座快訊" % (today)
    msg['From'] = "1102108133@kuas.edu.tw"
    msg['To'] = "grapherd@gmail.com"

    smtpserver.sendmail("1102108133@kuas.edu.tw", MAILING_LIST, msg.as_string())
    smtpserver.quit()

    print("End sending mail")


def prepare_send_mail():
    if os.path.isfile(OLD_JSON_FILE):
        print("Update news")
        result = json.loads(open(JSON_FILE, "r").read())
        result = filter_compare(result)  

        old_result = json.loads(open(OLD_JSON_FILE, "r").read())

        send_mail(result, old_result)

    else:
        print("Init news")
        result = json.loads(open(JSON_FILE, "r").read())
        result = filter_compare(result)  

        send_mail(result)

        


if __name__ == "__main__":
    prepare_send_mail()
