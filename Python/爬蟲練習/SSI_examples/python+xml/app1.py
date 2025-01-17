import pandas as pd
import requests
import io

# 使用 requests 模組下載
url = "https://www.ibm.com/support/pages/sites/default/files/product-lifecycle/ibm_product_lifecycle_list.csv"
response = requests.get(url)

# 檢查狀態碼
if response.status_code == 200:
    # 成功下載，將內容轉換為 DataFrame
    data = pd.read_csv(io.StringIO(response.content.decode('utf-8'))) 

    # 提取所需的欄位並儲存
    filtered_data = data[data['IBM Product'].str.contains('IBM Power |Key lifecycle', case=False) | (data['IBM Product'] == 'IBM MQ')]
    sorted_data = filtered_data.sort_values(by='GA', ascending=False)
    selected_columns = sorted_data[['IBM Product', 'VRM', 'PID', 'MTM', 'GA', 'EOS']]

    selected_columns.to_excel('IBM_Product_Lifecycle.xlsx', index=False)

else:
    print(f"下載失敗，HTTP狀態碼：{response.status_code}")