import json

import aiohttp
import asyncio
import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_data(web_model1, web_model2):
    async with aiohttp.ClientSession() as session:
        if web_model1:
            query_url = (
                "https://www.ibm.com/docs/api/v1/search/announcements?query="
                + web_model1
                + "&type=salesManual&start=0&limit=1&region=AP"
            )
            query_content = await fetch(session, query_url)
            query_data = json.loads(query_content)
            web_model2 = query_data["topics"][0]["product"]["key"]
        if web_model2:
            url = (
                "https://www.ibm.com/docs/api/v1/content/"
                + web_model2
                + "?announcement="
                + web_model2
                + "&parsebody=true&lang=en&role=&region=AP"
            )
            rsp = await fetch(session, url)
            soup = BeautifulSoup(rsp, "html.parser")
            device_name = soup.h1.get_text()
            table_content = pd.read_html(url)
    return device_name, table_content


def main_func():
    cache = {}
    option = st.selectbox("選擇任一格式輸入.", ["1. 格式 XXXX-XXX", "2. 格式 XXXX-XX"], key=0)
    if option == "1. 格式 XXXX-XXX":
        model1_func(cache)
    elif option == "2. 格式 XXXX-XX":
        model2_func(cache)
    else:
        st.text("輸入錯誤")


def model1_func(cache):
    web_model1 = st.text_input('輸入機型 ( XXXX-XXX ) : ', key=1)
    if web_model1 != '':
        if web_model1 in cache:
            device_name, table_content = cache[web_model1]
        else:
            device_name, table_content = asyncio.run(get_data(web_model1, None))
            cache[web_model1] = (device_name, table_content)
        date_table_func(device_name, table_content)


def model2_func(cache):
    web_model2 = st.text_input('輸入機型 ( XXXX-XX ) : ', key=2)
    web_model2 = "M" + web_model2
    if web_model2 != 'M':
        if web_model2 in cache:
            device_name, table_content = cache[web_model2]
        else:
            device_name, table_content = asyncio.run(get_data(None, web_model2))
            cache[web_model2] = (device_name, table_content)
        date_table_func(device_name, table_content)


def date_table_func(device_name, table_content):
    st.text(device_name)
    st.table(table_content[0])


# ST標題
st.title("查詢IBM設備相關日期")
main_func()
