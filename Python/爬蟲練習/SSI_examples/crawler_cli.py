import requests
import pandas as pd
import datetime
import os

def fetch_csv(url, filename):
    response = requests.get(url)
    open(filename, 'wb').write(response.content)

def parse_dates(date_list, label):
    if not date_list:
        print(f"此型號尚未{label}資料!")  # 顯示錯誤訊息
        return
    for date_str in date_list:
        if isinstance(date_str, str):  # 確保 date_str 是字串
            try:
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                print(f"{label}日期是: {date}")
            except ValueError:
                print(f"無法解析{label}日期: {date_str}")
        else:
            print(f"無效的{label}日期格式: {date_str}")  # 處理非字串類型的日期

# 在程式開始時詢問用戶輸入
product_code = input("請輸入產品代碼（例如：8286-41A）: ")

# 下載 CSV 檔案
url = "https://www.ibm.com/support/pages/sites/default/files/product-lifecycle/ibm_product_lifecycle_list.csv"
fetch_csv(url, 'ibm_product_lifecycle.csv')

# 讀取 CSV 檔案
df = pd.read_csv('ibm_product_lifecycle.csv')

# 篩選包含用戶輸入的產品代碼的記錄
filtered_df = df[df['IBM Product'].str.contains(product_code)]

# 提取 EOS 和 GA 資料
eos_dates = filtered_df['EOS'].tolist()
ga_dates = filtered_df['GA'].tolist()

# 解析日期
parse_dates(eos_dates, "EOS")
parse_dates(ga_dates, "GA")

# 清除暫存的 CSV 檔案
os.remove('ibm_product_lifecycle.csv')