import random
import string
import xlwt

# 建立 Excel 工作簿
workbook = xlwt.Workbook()

# 建立 Excel 工作表
sheet = workbook.add_sheet("autocrtuid")

# 寫入表頭
sheet.write(0, 0, "ID Number")
sheet.write(0, 1, "Name")

# 生成十萬組身分證字號和英文姓名
for i in range(1, 100001):
    # 生成身分證字號
    id_number = random.choice(string.ascii_uppercase)  # 隨機選擇一個英文字母作為首碼
    id_number += str(random.randint(1, 2))  # 隨機選擇一個性別碼，1代表男性，2代表女性
    id_number += str(random.randint(1000000, 9999999))  # 生成後面七個數字
    
    # 計算檢查碼
    check_code = (10 - sum(int(digit) * weight for digit, weight in zip(id_number, [1, 9, 8, 7, 6, 5, 4, 3, 2, 1])) % 10) % 10
    id_number += str(check_code)
    
    # 生成英文姓名
    name = random.choice(string.ascii_uppercase)  # 隨機選擇一個英文字母作為姓氏的首字母
    name += ''.join(random.choice(string.ascii_lowercase) for _ in range(9))  # 隨機生成一個英文名字
    
    # 寫入 Excel 工作表
    sheet.write(i, 0, id_number)
    sheet.write(i, 1, name)

# 儲存 Excel 檔案
workbook.save("autocrtuid.xls")
