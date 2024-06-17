import pyodbc
import pandas

cnx = pyodbc.connect(
        'Driver=IBM i Access ODBC Driver; '
        'System=172.16.14.61; '
        'UserID=ibmecs; '
        'Password=ibmecsusr;'
        )
SCHEMA="ddscinfo2"
sql = "Select * from {}.tmp".format(SCHEMA)
data = pandas.read_sql(sql, cnx)
print(data)