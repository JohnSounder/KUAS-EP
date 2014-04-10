# -*- coding: utf-8 -*-

import time
import smtplib
import subprocess

import main

STATUS_TYPE = {u"報名截止": 0, u"人數已滿": 0, u"報名": 1, u"報名尚未開始": 2}

today = time.strftime("%Y/%m/%d")

def day_compare(a, b):
    a_year, a_month, a_day = list(map(lambda x: int(x), a.split("/")))
    b_year, b_month, b_day = list(map(lambda x: int(x), b.split("/")))

    return a_year >= b_year and a_month >= b_month and a_day >= b_day


def filte_compare():
    result = main.Search(main.Login())


    filter_result = []
    for i in result:
        item = result[i]
        if day_compare(item['end_sign_up_date'], today) and STATUS_TYPE[item['status']]:
            filter_result.append(item)

    return filter_result
            

def send_mail(result):
    

if __name__ == "__main__":
    filte_compare()