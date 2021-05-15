#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/24 下午 06:26
# @Author : Aries
# @Site : 
# @File : data.py
# @Software: PyCharm

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def download(url,Time,StnP,SeaP,Temp,Td,RH,WS,WD,WSG,WDG,Pre,PreH,Sun,Glob,Visb,UV,Cloud):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    td = soup.find_all('td')
    ALL = []  # 10開始
    for i in td:
        i = i.text
        ALL.append(i)
    a = 1
    for i in range(10, 418):
        ALL[i] = ALL[i].replace('\xa0','')
        if a == 1:
            Time.append(ALL[i])
        if a == 2:
            StnP.append(ALL[i])
        if a == 3:
            SeaP.append(ALL[i])
        if a == 4:
            Temp.append(ALL[i])
        if a == 5:
            Td.append(ALL[i])
        if a == 6:
            RH.append(ALL[i])
        if a == 7:
            WS.append(ALL[i])
        if a == 8:
            WD.append(ALL[i])
        if a == 9:
            WSG.append(ALL[i])
        if a == 10:
            WDG.append(ALL[i])
        if a == 11:
            Pre.append(ALL[i])
        if a == 12:
            PreH.append(ALL[i])
        if a == 13:
            Sun.append(ALL[i])
        if a == 14:
            Glob.append(ALL[i])
        if a == 15:
            Visb.append(ALL[i])
        if a == 16:
            UV.append(ALL[i])
        if a == 17:
            Cloud.append(ALL[i])
            a = 0
        a = a + 1

def spider(year):
    Date = []
    Time = []
    StnP = []
    SeaP = []
    Temp = []
    Td = []
    RH = []
    WS = []
    WD = []
    WSG = []
    WDG = []
    Pre = []
    PreH = []
    Sun = []
    Glob = []
    Visb = []
    UV = []
    Cloud = []
    month_data = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    date_big_data = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16','17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    date_small_data = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16','17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    date_two_data = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16','17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']

    print("開始爬取資料......")
    for x in tqdm(month_data):
        month = x
        if x == '02':
            for y in date_two_data:
                date = y
                month_date = f'{month}-{date}'
                for j in range(0, 24):
                    Date.append(month_date)
                url = f'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467080&stname=%25E5%25AE%259C%25E8%2598%25AD&datepicker={year}-{month}-{date}'
                download(url,Time,StnP,SeaP,Temp,Td,RH,WS,WD,WSG,WDG,Pre,PreH,Sun,Glob,Visb,UV,Cloud)
        elif x == '01' or x == '03' or x == '05' or x == '07' or x == '08' or x == '10' or x == '12':
            for y in date_big_data:
                date = y
                month_date = f'{month}-{date}'
                for j in range(0, 24):
                    Date.append(month_date)
                url = f'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467080&stname=%25E5%25AE%259C%25E8%2598%25AD&datepicker={year}-{month}-{date}'
                download(url,Time,StnP,SeaP,Temp,Td,RH,WS,WD,WSG,WDG,Pre,PreH,Sun,Glob,Visb,UV,Cloud)
        else:
            for y in date_small_data:
                date = y
                month_date = f'{month}-{date}'
                for j in range(0, 24):
                    Date.append(month_date)
                url = f'https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=467080&stname=%25E5%25AE%259C%25E8%2598%25AD&datepicker={year}-{month}-{date}'
                download(url,Time,StnP,SeaP,Temp,Td,RH,WS,WD,WSG,WDG,Pre,PreH,Sun,Glob,Visb,UV,Cloud)

    return Date,Time,StnP,SeaP,Temp,Td,RH,WS,WD,WSG,WDG,Pre,PreH,Sun,Glob,Visb,UV,Cloud
