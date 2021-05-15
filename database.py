#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/24 下午 06:41
# @Author : Aries
# @Site : 
# @File : database.py
# @Software: PyCharm

import pymssql
from tqdm import tqdm

def upload(year,Date, Time, StnP, SeaP, Temp, Td, RH, WS, WD, WSG, WDG, Pre, PreH, Sun, Glob, Visb, UV, Cloud):
    print("開始連接資料庫......")
    # 連接資料庫
    conn = pymssql.connect(
        host='',
        user='',
        password='',
        database=''
    )

    print("開始建立資料表......")
    cursor = conn.cursor()
    cursor.execute(f"""
    IF OBJECT_ID('weather_{year}', 'U') IS NOT NULL
        DROP TABLE weather_{year}
    CREATE TABLE weather_{year} (
        編號 INT IDENTITY(1,1),
        年 VARCHAR(100),
        月 VARCHAR(100),
        日 VARCHAR(100),
        時 VARCHAR(100),
        測站氣壓 VARCHAR(100),
        海平面氣壓 VARCHAR(100),
        氣溫 VARCHAR(100),
        露點溫度 VARCHAR(100),
        相對溼度 VARCHAR(100),
        風速 VARCHAR(100),
        風向 VARCHAR(100),
        最大風陣 VARCHAR(100),
        最大風陣風向 VARCHAR(100),
        降水量 VARCHAR(100),
        降水時數 VARCHAR(100),
        日照時數 VARCHAR(100),
        全天空日射量 VARCHAR(100),
        能見度 VARCHAR(100),
        紫外線指數 VARCHAR(100),
        總雲量 VARCHAR(100),
        PRIMARY KEY(編號)
        )
    """)
    conn.commit()

    print("開始上傳資料......")
    # 將資料傳入資料庫
    for i in tqdm(range(0,len(Date))):
        if StnP[i] == '...' and SeaP[i] == '...' and Temp[i] == '...' and Td[i] == '...' and RH[i] == '...' and WS[i] == '...':
            break
        cursor.executemany(f"INSERT INTO weather_{year} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",[(year,Date[i].split("-")[0],Date[i].split("-")[1],Time[i],StnP[i],SeaP[i],Temp[i],Td[i],RH[i],WS[i],WD[i],WSG[i],WDG[i],Pre[i],PreH[i],Sun[i],Glob[i],Visb[i],UV[i],Cloud[i])])
        conn.commit()
    print("資料已上傳完成~~~")
