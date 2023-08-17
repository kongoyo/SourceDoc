import json

import pandas as pd
import requests
import streamlit as st
from bs4 import BeautifulSoup


def main_func():
    option = st.selectbox("選擇任一格式輸入.", ["1. 格式 XXXX-XXX", "2. 格式 XXXX-XX"], key=0)
    if option == "1. 格式 XXXX-XXX":
        model1_func()
    elif option == "2. 格式 XXXX-XX":
        model2_func()
    else:
        st.text("輸入錯誤")


def model1_func():
    web_model1 = st.text_input('輸入機型 ( XXXX-XXX ) : ', key=1)
    # 查詢第二種機型代碼
    query_url = (
            "https://www.ibm.com/docs/api/v1/search/announcements?query="
            + web_model1
            + "&type=salesManual&start=0&limit=1"
    )
    if web_model1 != '':
        query_content = requests.get(query_url)
        query_data = json.loads(query_content.text)
        web_model2 = query_data["topics"][0]["product"]["key"]
    # 查詢公告日期、銷售日期、EOM日期和EOS日期
        url = (
            "https://www.ibm.com/docs/api/v1/content/"
            + web_model2
            + "?announcement="
            + web_model2
            + "&parsebody=true&lang=en&role="
        )
        if web_model2 != '':
            rsp = requests.get(url)
            soup = BeautifulSoup(rsp.text, "html.parser")
            # 取得設備完整名稱
            device_name = soup.h1.get_text()
            date_table_func(device_name, url)


def model2_func():
    web_model2 = st.text_input('輸入機型 ( XXXX-XX ) : ', key=2)
    web_model2 = "M" + web_model2
    # 查詢公告日期、銷售日期、EOM日期和EOS日期
    url = (
            "https://www.ibm.com/docs/api/v1/content/"
            + web_model2
            + "?announcement="
            + web_model2
            + "&parsebody=true&lang=en&role="
    )
    if web_model2 != 'M':
        rsp = requests.get(url)
        soup = BeautifulSoup(rsp.text, "html.parser")
        # 取得設備完整名稱
        device_name = soup.h1.get_text()
        date_table_func(device_name, url)


def date_table_func(device_name, url):
    st.text(device_name)
    table_content = pd.read_html(url)
    st.table(table_content[0])


# ST標題
st.title("查詢IBM設備相關日期")
main_func()
