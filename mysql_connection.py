from mysql_config import dbConfig
import mysql.connector as mysql
from tkinter import messagebox

class Bookdb:
    def __init__(self):
        self.con = mysql.connect(**dbConfig)
        self.cursor = self.con.cursor()
        print("You have connected to the  database")
        print(self.con)

    # to ensure that the connection is always closed when the program is terminated
    def __del__(self): 
        self.con.close()

    def view(self):
        self.cursor.execute("SELECT * FROM books")
        rows = self.cursor.fetchall()
        self.con.commit()
        return rows

    def insert(self, title, author, isbn):
        query=("INSERT INTO books(title,author,isbn)VALUES (%s, %s, %s)")
        values = [title, author, isbn]
        self.cursor.execute(query,values)
        self.con.commit()
        messagebox.showinfo(title="Book Database",message="New book added to database")

    def update(self, id, title, author, isbn):
        query = 'UPDATE books SET  title = %s, author = %s, isbn = %s WHERE id= %s'
        values = [title, author, isbn, id]
        self.cursor.execute(query, values)
        self.con.commit()
        messagebox.showinfo(title="Book Database",message="Book Updated")

    def delete(self, id):
        query ='DELETE FROM books WHERE id = %s'
        values = [id]
        self.cursor.execute(query, values)
        self.con.commit()
        messagebox.showinfo(title="Book Database",message="Book Deleted")