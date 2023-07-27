# -*- coding: utf-8 -*-
"""
Created on Mon May  4 01:59:51 2020

@author: Zino
dataset:https://data.gov.tw/dataset/120711

"""
import json

# 導入模組(module) 
import requests

# 1.2. 對網址get後 存在response變數中
response = requests.get("https://newhouse.591.com.tw/home/housing/search?rid=1&sid=&page=2"
                        , headers={
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
                            })

# 3. 使用json module讀取 Json 資料格式

content = response.content.decode()
jd = json.loads(content)
# 操作List 印出第一比資料
print(jd["data"]["items"][0]["address"])