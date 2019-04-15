import sqlite3

def create_table():
    sqlConnection=sqlite3.connect("lite.db")
    cursorObject=sqlConnection.cursor()
    cursorObject.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    cursorObject.execute("INSERT INTO store VALUES ('iPhone',100,800)")
    sqlConnection.commit()
    sqlConnection.close()

def insert(item,quantity,price):
    sqlConnection=sqlite3.connect("lite.db")
    cursorObject=sqlConnection.cursor()
    cursorObject.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    sqlConnection.commit()
    sqlConnection.close()

def delete(item):
    sqlConnection=sqlite3.connect("lite.db")
    cursorObject=sqlConnection.cursor()
    cursorObject.execute("DELETE FROM store WHERE item=?",(item,))
    sqlConnection.commit()
    sqlConnection.close()

def update(quantity,price,item):
    sqlConnection=sqlite3.connect("lite.db")
    cursorObject=sqlConnection.cursor()
    cursorObject.execute("UPDATE store SET quantity=?, price=? WHERE item =?",(quantity,price,item))
    sqlConnection.commit()
    sqlConnection.close()



def view():
    sqlConnection=sqlite3.connect("lite.db")
    cursorObject=sqlConnection.cursor()
    cursorObject.execute("SELECT * FROM store")
    rows=cursorObject.fetchall()
    sqlConnection.close()
    return rows

print("previous Price")
print(view())
update(85,450,"iPhone")
#delete("Samsung S8")
print("New Price")
print(view())
# insert("Samsung S8",100,450)