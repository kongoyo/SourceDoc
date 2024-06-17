from operator import index
import pyodbc
import pandas as pd
import random
from faker import Faker
import time

# 創建假資料生成器
fake = Faker()

# 連接到IBMi
conn = pyodbc.connect(
    driver='{IBM i Access ODBC Driver}',
    system='172.16.14.61',
    uid='QSECOFR',
    pwd='PASSWORD')

if conn:
    print("Connected to the database")

    # 生成10萬筆測試資料
cus_name = fake.unique.name()
cus_age = random.randint(18, 90)
cus_birth = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=90)
cus_liveAddress = fake.address()
cus_regAddress = fake.address()
cus_emailAddress = fake.unique.email()
cus_bloodType = random.choice(['A', 'B', 'AB', 'O'])
cus_companyName = fake.company()
cursor = conn.cursor()
sql = str("select * from ddscinfo.customers")
data = pd.read_sql_query(sql=sql, con=conn, index_col='CUSTOMER_ID')
print(data)