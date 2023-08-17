import json

import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

# 定義參數
option = ''  # 查詢選項
product_key = ''  # 產品名稱
url = ''  # IBM Document網址
query_url = ''  # IBM Product網址

# 選擇輸入方式
while option == '':
    print("查詢IBM設備相關日期")
    option = input("輸入搜尋方式 (1.<XXXX-XXX> 2.<XXXX-XX>): ")
    if option == "1":
        # 輸入要查詢的機型
        model = input("格式 XXXX-XXX: ")
        while not re.findall("\d\d\d\d-\w\w\w", model):
            model = input("錯誤，請重新輸入。格式 XXXX-XXX: ")
        # 把機型轉換成數字格式
        query_url = (
                "https://www.ibm.com/docs/api/v1/search/announcements?query="
                + model
                + "&type=salesManual&start=0&limit=1"
        )
        query_content = requests.get(query_url)
        query_data = json.loads(query_content.text)
        product_key = query_data["topics"][0]["product"]["key"]
    elif option == "2":
        product_key = input("格式 XXXX-XX: ")
        while not re.findall('\d\d\d\d-\d\d', product_key):
            product_key = input("錯誤，請重新輸入。格式 XXXX-XX: ")
        product_key = "M" + product_key
    else:
        print('輸入錯誤，請重新輸入!')

print("設備訊息 MXXXX-XX): ", product_key)

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

# 顯示設備完整名稱
device_name = soup.h1.get_text()
print(device_name)

# 顯示日期表格

table_content = pd.read_html(url)
print(table_content[0])

# 列印參考網址
print(" " * 100)
print("=" * 100)
print("Query URL: ", query_url)
print("Product URL: ", url)