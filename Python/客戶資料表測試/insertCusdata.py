from operator import index
import pyodbc
import pandas as pd
import sqlalchemy as sa
import random
from faker import Faker
import time

# 創建假資料生成器
fake = Faker()

# 連接到IBMi
engine = sa.create_engine("ibmi://ibmecs:ibmecsusr@172.16.14.61/tsddssrc", echo=True)

conn = engine.connect()
metadata = sa.MetaData()
table = sa.Table('customers', metadata, autoload=True, autoload_with=engine)

query = sa.select([table])

result = conn.execute(query)
result = result.fetchall()

print(result[0])
# try:
#     conn = pyodbc.connect(
#         driver='{IBM i Access ODBC Driver}',
#         system='172.16.14.61',
#         uid='QSECOFR',
#         pwd='PASSWORD')
#     print("Connected to the database")
# except:
#     print("Not connect to the database")

    # 生成10萬筆測試資料

customer_name = fake.unique.name()
customer_age = random.randint(18, 90)
customer_birth = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=90)
customer_liveAddress = fake.address()
customer_regAddress = fake.address()
customer_emailAddress = fake.unique.email()
customer_bloodType = random.choice(['A', 'B', 'AB', 'O'])
customer_companyName = fake.company()

sql = "select * from ddscinfo.customers where (customer_id >= 10000 and customer_id <= 10010)"
data = pd.read_sql(sql=sql, con=conn)
print(data)