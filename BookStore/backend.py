import sqlite3

def connect():
        connection1=sqlite3.connect("bookstore.db")
        cursorr=connection1.cursor()
        cursorr.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        connection1.commit()
        connection1.close()


def insert(title,author,year,isbn):
    connection1=sqlite3.connect("bookstore.db")
    cursorr = connection1.cursor()
    cursorr.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    connection1.commit()
    connection1.close()

def view():
    connection1=sqlite3.connect("bookstore.db")
    cursorr = connection1.cursor()
    cursorr.execute("SELECT * FROM book")
    rows=cursorr.fetchall()
    connection1.close()
    return rows

def search(title="",author="",year="",isbn=""):
    connection1=sqlite3.connect("bookstore.db")
    cursorr = connection1.cursor()
    cursorr.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?, (title,author,year,isbn))
    rows=cursorr.fetchall()
    connection1.close()
    return rows

connect()
insert("The Sea","John Tablet",1918,1932168976)
print(view())
