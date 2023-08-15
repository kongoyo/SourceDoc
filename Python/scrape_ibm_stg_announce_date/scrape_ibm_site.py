import requests
from bs4 import BeautifulSoup

model = input("model: ")
url = (
    "https://www.ibm.com/docs/api/v1/content/M"
    + model
    + "?announcement=M"
    + model
    + "&parsebody=true&lang=en&role="
)

html_content = requests.get(url)
# 解析HTML内容
soup = BeautifulSoup(html_content.content, "html.parser")

# 找到表头
thead = soup.find("thead")
header_cells = thead.find_all("th")
header_labels = [
    cell.find("div", class_="bx--table-header-label").text.strip()
    for cell in header_cells
]

# 找到数据行
tbody = soup.find("tbody")
data_rows = tbody.find_all("tr")

# 提取数据
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
