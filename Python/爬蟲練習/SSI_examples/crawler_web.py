from flask import Flask, request, render_template
import requests
import pandas as pd
import datetime
import os
from jinja2 import TemplateNotFound

def fetch_csv(url, filename):
    response = requests.get(url)
    open(filename, 'wb').write(response.content)

def parse_dates(date_list, label, product_name):
    results = []  # 用於存儲解析結果
    if not date_list:
        print(f"此型號尚未{label}資料!")  # 顯示錯誤訊息
        return results
    for date_str in date_list:
        if isinstance(date_str, str):  # 確保 date_str 是字串
            try:
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                results.append(f"{product_name}的{label}日期是: {date}")  # 收集結果，添加 product_name
            except ValueError:
                results.append(f"無法解析{label}日期: {date_str}")
        else:
            results.append(f"無效的{label}日期格式: {date_str}")  # 處理非字串類型的日期
    return results  # 返回解析結果

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            product_code = request.form['product_code'].upper()  # 將輸入轉換為大寫
            
            # 確保 data 目錄存在
            os.makedirs('data', exist_ok=True)  # 如果不存在則創建 data 目錄
            
            # 下載 CSV 檔案
            url = "https://www.ibm.com/support/pages/sites/default/files/product-lifecycle/ibm_product_lifecycle_list.csv"
            fetch_csv(url, 'data/ibm_product_lifecycle.csv')  # 修改為下載到 data 目錄

            # 讀取 CSV 檔案
            df = pd.read_csv('data/ibm_product_lifecycle.csv')  # 修改為從 data 目錄讀取

            # 篩選包含用戶輸入的產品代碼的記錄
            filtered_df = df[df['IBM Product'].str.contains(product_code)]

            # 提取產品名稱
            product_name = filtered_df['IBM Product'].iloc[0] if not filtered_df.empty else product_code  # 獲取第一個匹配的產品名稱
            
            # 提取 EOS 和 GA 資料
            eos_dates = filtered_df['EOS'].tolist()
            ga_dates = filtered_df['GA'].tolist()

            # 解析日期並收集結果
            eos_dates = parse_dates(eos_dates, "EOS", product_name)  # 修改為傳遞 product_name
            ga_dates = parse_dates(ga_dates, "GA", product_name)      # 修改為傳遞 product_name

            # 檢查是否有資料，並設置錯誤訊息
            eos_error = "此型號尚未EOS資料!" if not eos_dates else None
            ga_error = "此型號尚未GA資料!" if not ga_dates else None

            # 清除暫存的 CSV 檔案
            #os.remove('ibm_product_lifecycle.csv')

            # 返回結果到/result
            return render_template('result.html', product_code=product_name, eos_dates=eos_dates, ga_dates=ga_dates, eos_error=eos_error, ga_error=ga_error)
        else:
            # 在GET請求時顯示index.html
            return render_template('index.html')
    except TemplateNotFound:
        return "Template not found. Please check your template files."  # 錯誤處理

# 新增一個新的路由來顯示結果
@app.route('/result')
def result():
    return render_template('result.html')  # 這裡可以根據需要進行調整

@app.route('/all_products', methods=['GET'])
def all_products():
    try:
        # 讀取 CSV 檔案
        df = pd.read_csv('data/ibm_product_lifecycle.csv')  # 修改為從 data 目錄讀取
        
        # 提取需要顯示的欄位
        all_data = df[['IBM Product', 'EOS', 'GA']].to_dict(orient='records')  # 轉換為字典格式以便於渲染

        # 返回結果到all_products.html
        return render_template('all_products.html', all_data=all_data)
    except Exception as e:
        return str(e)  # 錯誤處理

if __name__ == '__main__':
    app.run(debug=True)