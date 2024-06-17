import pyodbc
import pandas

cnx = pyodbc.connect(
        'Driver=IBM i Access ODBC Driver; '
        'System=172.16.14.61; '
        'UserID=ibmecs; '
        'Password=ibmecsusr;'
        )
# 建立新的Library
SCHEMA="ddscinfo2"
# 建立新的cursor
cursor = cnx.cursor()
# 建立SQL語句
sql = "create schema {}".format(SCHEMA)
cursor.execute(sql)
cursor.commit()

sql = "set schema {}".format(SCHEMA)
cursor.execute(sql)
cursor.commit()

sql = "CREATE TABLE {}.tmp(col1 INT, col2 INT, PRIMARY KEY(col1))".format(SCHEMA)
cursor.execute(sql)
cursor.commit()

sql = "INSERT INTO {}.tmp (col1, col2) VALUES ( 1, 2)".format(SCHEMA)
cursor.execute(sql)
cursor.commit()

sql = "INSERT INTO {}.tmp (col1, col2) VALUES ( 9, 2)".format(SCHEMA)
cursor.execute(sql)
cursor.commit()

