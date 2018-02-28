import sqlite3 # Local database library

# Set up initial database
def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

# Insert command button
def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

# For testing purposes to see if backend code is editing database correctly
def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

# Search command button, an OR search, return all rows according to search parameter
def search(title = "", author = "", year = "", isbn = ""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

# Delete command button, user selects from listbox and deletes that item using ID
def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()

# Update command button, user selects from listbox and updates whichever parameter is entered, reference using ID
def update(id, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()
#insert("The Moon", "Ryan Mike", 1944, 9133434223193)
print(view())
#delete(3)
update(2, "The moon", "John Smooth", 1917, 99999999)
print(view())
print(search(author = "John Smith"))
