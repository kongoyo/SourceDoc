import json

import requests
from bs4 import BeautifulSoup

model = input("Device Info(Format XXXX-XXX): ")

# 查詢數字格式的Model Type
query_url = (
    "https://www.ibm.com/docs/api/v1/search/announcements?query="
    + model
    + "&type=salesManual&start=0&limit=1"
)
query_content = requests.get(query_url)
query_data = json.loads(query_content.text)
product_key = query_data["topics"][0]["product"]["key"]

print("Type+Model: ", product_key)

# 查詢公告日期、銷售日期、EOM日期和EOS日期
url = (
    "https://www.ibm.com/docs/api/v1/content/"
    + product_key
    + "?announcement="
    + product_key
    + "&parsebody=true&lang=en&role="
)
html_content = requests.get(url)
soup = BeautifulSoup(html_content.content, "html.parser")
title_cells = soup.find_all("body")
title_label = [
    cell.find("h1", class_="topictitle1 bx--type-productive-heading-06").text.strip()
    for cell in title_cells
]

thead = soup.find("thead")
header_cells = thead.find_all("th")  # type: ignore
header_labels = [
    cell.find("div", class_="bx--table-header-label").text.strip()
    for cell in header_cells
]

tbody = soup.find("tbody")
data_rows = tbody.find_all("tr")  # type: ignore

data = []
for row in data_rows:
    cells = row.find_all("td")
    row_data = [cell.text.strip() for cell in cells]
    data.append(row_data)

# 輸出表格資訊
print(
    f"{header_labels[0]:<15} {header_labels[1]:<15} {header_labels[2]:<15} {header_labels[3]:<25} {header_labels[4]:<25}"
)
print("=" * 100)
for row in data:
    print(f"{row[0]:<15} {row[1]:<15} {row[2]:<15} {row[3]:<25} {row[4]:<25}")

print(
    "===================================================================================================="
)
print(title_label)
print("Query URL: ", query_url)
print("Product URL: ", url)
