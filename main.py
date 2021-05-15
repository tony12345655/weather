#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/24 下午 06:20
# @Author : Aries
# @Site : 
# @File : main.py
# @Software: PyCharm

from data import spider
from database import upload

if __name__ == '__main__':

    print("歡迎使用天氣爬取~")
    year = input("請輸入年分(西元): ")

    # 爬蟲抓取資料
    Date, Time, StnP, SeaP, Temp, Td, RH, WS, WD, WSG, WDG, Pre, PreH, Sun, Glob, Visb, UV, Cloud = spider(year)

    # 將資料存入資料庫
    upload(year,Date, Time, StnP, SeaP, Temp, Td, RH, WS, WD, WSG, WDG, Pre, PreH, Sun, Glob, Visb, UV, Cloud)





