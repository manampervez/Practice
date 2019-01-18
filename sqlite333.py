import sqlite3

sqlConnection=sqlite3.connect("lite.db")
cursorObject=sqlConnection.cursor()
cursorObject.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
sqlConnection.commit()
sqlConnection.close()