# 取得IBM Group PTF Info
# 網址
# https://www.ibm.com/support/pages/ibm-i-group-ptfs-level
# Attached is the list of IBM i PSPs in XML format
# https://www.ibm.com/support/pages/sites/default/files/inline-files/xmldoc.xml


import pandas as pd
import requests as rq
import streamlit as st
from bs4 import BeautifulSoup

# 變數
url = "https://www.ibm.com/support/pages/ibm-i-group-ptfs-level"
rsp = rq.get(url)

# 標題
st.title("IBM i Group PTFs with level")
st.markdown("A list of the IBM i Group PTF documents with level")

# 內容
rsp_soup = BeautifulSoup(rsp.text, 'html.parser')
rsp_table = rsp_soup.find('table', class_='bx--data-table bx--data-table--compact')
if rsp_table:
    table_rows = rsp_table.find_all('tr')
    if len(table_rows) > 1:
        headers = [header.text.strip() for header in table_rows[0].find_all('th')]
        data = []
        for row in table_rows[1:]:
            row_data = [cell.text.strip() for cell in row.find_all('td')]
            # 保留第一、第二、第三和第五欄的資料
            data.append([row_data[0], row_data[1], row_data[2], row_data[4]])

        if data:  # 如果還有資料，則建立 DataFrame
            rsp_pdtable = pd.DataFrame(data, columns=headers[:3] + [headers[4]])
            st.table(rsp_pdtable)
        else:
            st.error("No data to display.")
    else:
        st.error("Table does not contain enough data.")
else:
    st.error("Table data not found.")
