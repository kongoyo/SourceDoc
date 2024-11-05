import jaydebeapi  # 確保已安裝此庫
import jpype

def connect_to_ibm_i():
    # 設定連線參數
    jdbc_url = "jdbc:as400://172.16.14.61"
    driver = "com.ibm.as400.access.AS400JDBCDriver"
    jar_path = "./libs/jt400.jar"  # 替換為jt400.jar的實際路徑
    username = "qsecofr"
    password = "password"

    # 啟動JVM
    jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path={}".format(jar_path))

    try:
        # 建立連線
        connection = jaydebeapi.connect(driver, jdbc_url, [username, password])
        print("主機連線成功!")  # 新增成功連線的訊息
        return connection
    except Exception as e:
        print("連線失敗:", e)  # 新增失敗的訊息
        exit()  # 程式結束

def main_menu():
    connection = connect_to_ibm_i()  # 在主選單之前連線到IBM i主機
    while True:
        print("選擇操作:")
        print("1. 建立測試表格")
        print("2. 亂數新增1000筆紀錄")
        print("3. 隨機更新500筆紀錄")
        print("4. 隨機刪除500筆紀錄")
        print("5. 退出")

        choice = input("請輸入選擇 (1-5): ")

        if choice == '1':
            create_test_table(connection)
        elif choice == '2':
            insert_random_records(connection)
        elif choice == '3':
            update_random_records(connection)
        elif choice == '4':
            delete_random_records(connection)
        elif choice == '5':
            break
        else:
            print("無效的選擇，請重試。")

# 其他函數的定義
def create_test_table(connection):
    # 實現建立測試表格的邏輯
    create_table_sql = """
    CREATE TABLE ddscinfo.cdctbl (
        Name VARCHAR(50),
        Age INT,
        Height DECIMAL(5, 2),
        Weight DECIMAL(5, 2)
    )
    """
    cursor = connection.cursor()
    cursor.execute(create_table_sql)
    connection.commit()  # 提交變更
    print("表格 ddscinfo.cdctbl 建立成功!")  # 新增表格建立成功的訊息

def insert_random_records(connection):
    import random
    import faker

    fake = faker.Faker()
    cursor = connection.cursor()

    for _ in range(1000):
        name = fake.name()
        age = random.randint(18, 65)  # 隨機年齡範圍
        height = round(random.uniform(150.0, 200.0), 2)  # 隨機身高範圍
        weight = round(random.uniform(50.0, 100.0), 2)  # 隨機體重範圍

        insert_sql = "INSERT INTO ddscinfo.cdctbl (Name, Age, Height, Weight) VALUES (?, ?, ?, ?)"
        cursor.execute(insert_sql, (name, age, height, weight))

    connection.commit()  # 提交變更
    print("已新增 1000 筆隨機紀錄到 ddscinfo.cdctbl 表格!")  # 新增紀錄成功的訊息

def update_random_records(connection):
    import random

    cursor = connection.cursor()
    updated_records = []  # 用於儲存更新的紀錄內容
    failed_updates = []  # 用於儲存更新失敗的紀錄內容

    # 隨機選擇500筆紀錄進行更新
    for _ in range(500):
        # 隨機選擇一筆紀錄的ID（假設有一個ID欄位）
        random_id = random.randint(1, 1000)  # 假設ID範圍是1到1000
        new_age = random.randint(18, 65)  # 隨機新年齡
        new_weight = round(random.uniform(50.0, 100.0), 2)  # 隨機新體重

        update_sql = "UPDATE ddscinfo.cdctbl SET age = ?, weight = ? WHERE RRN(ddscinfo.cdctbl) = ?"
        try:
            cursor.execute(update_sql, (new_age, new_weight, random_id))
            updated_records.append((random_id, new_age, new_weight))  # 儲存成功更新的紀錄
        except Exception as e:
            failed_updates.append((random_id, new_age, new_weight, str(e)))  # 儲存失敗的紀錄及錯誤訊息

    connection.commit()  # 提交變更
    print("已隨機更新 500 筆紀錄的年齡和體重!")  # 更新成功的訊息

    # 列出更新失敗的紀錄內容
    if failed_updates:
        print("更新失敗的紀錄:")
        for record in failed_updates:
            print(f"ID: {record[0]}, 新年齡: {record[1]}, 新體重: {record[2]}, 錯誤訊息: {record[3]}")
    else:
        print("所有紀錄更新成功!")

def delete_random_records(connection):
    import random

    cursor = connection.cursor()

    # 隨機刪除500筆紀錄，確保ID不重複
    deleted_ids = set()  # 用於儲存已刪除的ID
    while len(deleted_ids) < 500:
        # 隨機選擇一筆紀錄的ID（假設有一個ID欄位）
        random_id = random.randint(1, 1000)  # 假設ID範圍是1到1000
        if random_id not in deleted_ids:  # 確保ID不重複
            delete_sql = "DELETE FROM ddscinfo.cdctbl WHERE RRN(ddscinfo.cdctbl) = ?"
            cursor.execute(delete_sql, (random_id,))
            deleted_ids.add(random_id)  # 將已刪除的ID加入集合

    connection.commit()  # 提交變更
    print("已隨機刪除 500 筆紀錄!")  # 刪除成功的訊息

    # 列出刪除的紀錄內容
    for deleted_id in deleted_ids:
        print(f"已刪除的ID: {deleted_id}")

if __name__ == "__main__":
    main_menu()
