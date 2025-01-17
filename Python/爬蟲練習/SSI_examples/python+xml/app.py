import requests
from flask import Flask, jsonify, render_template
import xml.etree.ElementTree as ET
import xmlschema

def extract_data_from_xml(root):
    # 提取 HWTitleRecord 和 SWTitleRecord
    hw_records = root.findall('.//HWTitleRecord')  # 查找所有 HWTitleRecord
    sw_records = root.findall('.//SWTitleRecord')  # 查找所有 SWTitleRecord

    # 将提取的数据转换为字典列表
    hw_data = [{'HWTitle': hw.find('HWTitle').text, 'Version': hw.find('Version').text} for hw in hw_records]
    sw_data = [{'SWTitle': sw.find('SWTitle').text, 'Version': sw.find('Version').text} for sw in sw_records]

    return hw_data, sw_data  # 返回硬件和软件数据

def index():
    # 獲取 XML 數據
    response = requests.get('https://www.ibm.com/support/pages/lifecycleapp/api/feeds?days=14&event=ALL&type=download&format=xml')  # 下載 XML 檔案    
    # 加載 XSD
    schema = xmlschema.XMLSchema('https://www.ibm.com/support/pages/lifecycle/ibmPlcDownload_v3.xsd')  # 加載 XSD
    xml_data = response.content  # 獲取原始 XML 數據
    root = ET.fromstring(xml_data)  # 解析 XML 數據

    # 移除 'endalldate' 屬性
    for plc_info in root.findall('.//PLCInfo'):
        if 'endalldate' in plc_info.attrib:
            del plc_info.attrib['endalldate']  # 移除不必要的屬性

    validated_data = schema.to_dict(ET.tostring(root))  # 將 XML 轉換為字典

    # 確保 validated_data 是一個列表
    if isinstance(validated_data, dict) and 'PLCInfo' in validated_data:
        validated_data = validated_data['PLCInfo']  # 提取 PLCInfo 列表
    else:
        validated_data = []  # 如果沒有 PLCInfo，設置為空列表

    # 將 XML 數據顯示在控制台
    print(validated_data)  # 在控制台輸出解析後的數據

    # 提取數據
    hw_data, sw_data = extract_data_from_xml(root)  # 提取硬件和軟件數據

    # 將數據顯示在控制台
    print("硬件數據:", hw_data)  # 在控制台輸出硬件數據
    print("軟件數據:", sw_data)  # 在控制台輸出軟件數據

    # 渲染模板並顯示數據
    return render_template('index.html', hw_data=hw_data, sw_data=sw_data)  # 渲染 HTML 模板

if __name__ == '__main__':
    # 直接調用 index 函數
    index()  # 直接調用 index 函數以執行程式