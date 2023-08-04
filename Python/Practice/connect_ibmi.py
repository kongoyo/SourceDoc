import pyodbc

connection = pyodbc.connect(
    driver='{IBM i Access ODBC Driver}',
    system='172.16.13.68',
    uid='spring',
    pwd='password')
c1 = connection.cursor()

c1.execute('select * from qiws.QCUSTCDT order by cusnum desc')
for row in c1:
    print (row)