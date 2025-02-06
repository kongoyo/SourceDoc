import requests
from bs4 import BeautifulSoup
import json
import random

url = "https://www.ibm.com/docs/zh/announcements/power-system-s814-server?region=AP"

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    # ... 其他 User-Agent
]

headers = {'User-Agent': random.choice(user_agents)}

response = requests.get(url, headers=headers)

eos_lines = [line for line in response.text.splitlines() if "eos" in line]

for line in eos_lines:
    print(line)  # 每行自動換行




    
# soup = BeautifulSoup(response.text, 'html.parser')
# 
# # 找到所有表格
# tables = soup.find_all('table')
# 
# print(tables)
# 
# 選擇要解析的表格 (根據表格的id或其他屬性來判斷)
# target_table = tables[0]  # 假設第一個表格是我們要的

# data = []
# for row in target_table.find_all('tr'):
#     cols = row.find_all('td')
#     if len(cols) >= 2:  # 確保至少有兩個欄位 (規格名稱和規格值)
#         data.append({
#             '規格名稱': cols[0].text.strip(),
#             '規格值': cols[1].text.strip()
#         })
# 
# with open('ibm_s814_specs.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
# 
# print("資料已成功存為 JSON 格式: ibm_s814_specs.json")