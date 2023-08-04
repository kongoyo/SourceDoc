from pyiaccess.engine import create_db

engine = create_db(
    hostname='V7R3N', dsn='odbc', username='IBMECS', password='IBMECSUSR'
)
engine.connect()
