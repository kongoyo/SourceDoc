import html.parser
import json
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

# 輸入要查詢的機型
model = input("Device Info(Format XXXX-XXX): ")

# 把機型轉換成數字格式
query_url = (
    "https://www.ibm.com/docs/api/v1/search/announcements?query="
    + model
    + "&type=salesManual&start=0&limit=1"
)
query_content = requests.get(query_url)
query_data = json.loads(query_content.text)
product_key = query_data["topics"][0]["product"]["key"]

print("Type-Number(Format MXXXX-XX): ", product_key)

# 查詢公告日期、銷售日期、EOM日期和EOS日期
url = (
    "https://www.ibm.com/docs/api/v1/content/"
    + product_key
    + "?announcement="
    + product_key
    + "&parsebody=true&lang=en&role="
)
rsp = requests.get(url)
soup = BeautifulSoup(rsp.text, "html.parser")

# 查找設備名稱
device_name = soup.h1.get_text()
print(device_name)

# 查找表頭
table_content = pd.read_html(url)
print(table_content[0])

# 列印參考網址
print(" " * 100)
print("=" * 100)
print("Query URL: ", query_url)
print("Product URL: ", url)
