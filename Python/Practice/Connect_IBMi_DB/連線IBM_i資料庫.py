import ibm_db_dbi as db2
from prettytable import from_db_cursor

conn = db2.connect()
cur = conn.cursor()
cur.execute("select * from qiws.qcustcdt")
print(from_db_cursor(cur))