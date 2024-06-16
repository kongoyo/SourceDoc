import ibm_db
import random
from faker import Faker
import time

# 創建假資料生成器
fake = Faker()

# 連接到IBMi
conn_str = "DATABASE=YOUR_DATABASE;HOSTNAME=YOUR_HOST;PORT=50000;PROTOCOL=TCPIP;UID=YOUR_USER;PWD=YOUR_PASSWORD;"
conn = ibm_db.connect(conn_str, "", "")

if conn:
    print("Connected to the database")

    # 生成10萬筆測試資料
    for _ in range(100000):
        cus_name = fake.unique.name()
        cus_age = random.randint(18, 90)
        cus_birth = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=90)
        cus_liveAddress = fake.address()
        cus_regAddress = fake.address()
        cus_emailAddress = fake.unique.email()
        cus_bloodType = random.choice(['A', 'B', 'AB', 'O'])
        cus_companyName = fake.company()

        insert_query = f"""
        INSERT INTO Customer (cus_name, cus_age, cus_birth, cus_liveAddress, cus_regAddress, cus_emailAddress, cus_bloodType, cus_companyName)
        VALUES ('{cus_name}', {cus_age}, '{cus_birth}', '{cus_liveAddress}', '{cus_regAddress}', '{cus_emailAddress}', '{cus_bloodType}', '{cus_companyName}')
        """

        try:
            ibm_db.exec_immediate(conn, insert_query)
        except Exception as e:
            print(f"Error inserting data: {e}")
else:
    print("Failed to connect to the database")
