#
# 功能: 建立QGPL/CUSTOMER。初始新增1000筆隨機紀錄。刪除500筆紀錄後新增500筆紀錄，重複5次。
# 

import jaydebeapi
import random
import string

# 使用jt400.jar連接到IBM i
conn = jaydebeapi.connect(
    "com.ibm.as400.access.AS400JDBCDriver",
    "jdbc:as400://172.16.14.61",
    ["QSECOFR", "password"],
    "/root/SourceDoc/jt400-20.0.7.jar"
)
cursor = conn.cursor()

# 創建表格
create_table_sql = """
CREATE TABLE QGPL.CUSTOMER (
    NAME VARCHAR(50),
    RANDOM_ID CHAR(6),
    EMAIL VARCHAR(100)
)
"""
cursor.execute(create_table_sql)

# 生成隨機數據並插入記錄
def generate_random_email():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(10)) + '@example.com'

def generate_unique_random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def insert_records(cursor, count):
    insert_sql = "INSERT INTO QGPL.CUSTOMER (NAME, RANDOM_ID, EMAIL) VALUES (?, ?, ?)"
    used_ids = set()
    for i in range(count):
        name = f'Customer{i+1}'
        while True:
            random_id = generate_unique_random_id()
            if random_id not in used_ids:
                used_ids.add(random_id)
                break
        email = generate_random_email()
        cursor.execute(insert_sql, (name, random_id, email))

def delete_random_records(cursor, count):
    delete_sql = "DELETE FROM QGPL.CUSTOMER WHERE RANDOM_ID = ?"
    cursor.execute("SELECT RANDOM_ID FROM QGPL.CUSTOMER")
    all_ids = [row[0] for row in cursor.fetchall()]
    ids_to_delete = random.sample(all_ids, min(count, len(all_ids)))
    for id_to_delete in ids_to_delete:
        cursor.execute(delete_sql, (id_to_delete,))

def get_record_count_and_size(cursor):
    cursor.execute("CALL QSYS2.QCMDEXC('DSPFD FILE(QGPL/CUSTOMER) TYPE(*MBR) OUTPUT(*OUTFILE) OUTFILE(QTEMP/FDINFO)')")
    cursor.execute("select mbnrcd, mbdssz, mbndtr from qtemp.fdinfo")
    result = cursor.fetchone()
    return result[0], result[1] / (1024 * 1024), result[2] if result else (0, 0, 0)

# 初始插入2000條記錄
insert_records(cursor, 2000)
conn.commit()
record_count, file_size, deleted_records = get_record_count_and_size(cursor)
print(f"表格創建完成，並已插入2000條記錄。")
print(f"當前記錄數：{record_count}，檔案大小：{file_size:.2f} MB，刪除筆數：{deleted_records}")

# 等待用戶按下任意鍵
input("初始2000筆紀錄新增完畢，請按下任意鍵繼續...")

# 重複刪除和新增各5次
for i in range(5):
    delete_random_records(cursor, 500)
    conn.commit()
    record_count, file_size, deleted_records = get_record_count_and_size(cursor)
    print(f"第{i+1}次：已隨機刪除500筆記錄。當前記錄數：{record_count}，檔案大小：{file_size:.2f} MB，刪除筆數：{deleted_records}")
    
    insert_records(cursor, 500)
    conn.commit()
    record_count, file_size, deleted_records = get_record_count_and_size(cursor)
    print(f"第{i+1}次：已新增500筆記錄。當前記錄數：{record_count}，檔案大小：{file_size:.2f} MB，刪除筆數：{deleted_records}")

# 關閉連接
cursor.close()
conn.close()

print("所有操作已完成。")
