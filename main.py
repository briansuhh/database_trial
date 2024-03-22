import tkinter as tk
from tkinter import ttk, messagebox
from mysql_connection import Bookdb
import mysql.connector as mysql
from mysql_config import dbConfig

# Create an instance of the Bookdb class
db = Bookdb()

def get_selected_row(event):
    global selected_tuple
    index = list_box.curselection()[0]
    selected_tuple = list_box.get(index)
    print(selected_tuple)
    title_entry.delete(0, 'end')
    title_entry.insert('end', selected_tuple[1])
    author_entry.delete(0, 'end')
    author_entry.insert('end', selected_tuple[2])
    isbn_entry.delete(0, 'end')
    isbn_entry.insert('end', selected_tuple[3])

def view_records():
    list_box.delete(0, 'end')
    for row in db.view():
        list_box.insert('end', row)

def add_book():
    db.insert(title_entry.get(), author_entry.get(), isbn_entry.get())
    list_box.delete(0, 'end')
    list_box.insert('end', (title_entry.get(), author_entry.get(), isbn_entry.get()))
    title_entry.delete(0, "end") # Clears input after inserting
    author_entry.delete(0, "end")
    isbn_entry.delete(0, "end")

def delete_records():
    db.delete(selected_tuple[0])

def update_records():
    db.update(selected_tuple[0], title_entry.get(), author_entry.get(), isbn_entry.get())
    title_entry.delete(0, "end") # Clears input after inserting
    author_entry.delete(0, "end")
    isbn_entry.delete(0, "end")

def clear_screen():
    list_box.delete(0,'end')
    title_entry.delete(0,'end')
    author_entry.delete(0,'end')
    isbn_entry.delete(0,'end')

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

window = tk.Tk()

window.title("Tkinter App with Mysql Database")
window.configure(background="light blue")
window.geometry("850x600")
window.resizable(0, 0)

title_label = ttk.Label(window, text="Title", background="light blue", font=("TkDefaultFont", 20))  
title_label.grid(row=0, column=0, sticky="NEWS", padx=5, pady=5)
title_entry = ttk.Entry(window, width=24)
title_entry.grid(row=0, column=1, sticky="W", padx=5, pady=5)

author_label = ttk.Label(window, text="Author", background="light blue", font=("TkDefaultFont", 20))  
author_label.grid(row=0, column=2, sticky="W", padx=5, pady=5)
author_entry = ttk.Entry(window, width=24)
author_entry.grid(row=0, column=3, sticky="W", padx=5, pady=5)

isbn_label = ttk.Label(window, text="ISBN", background="light blue", font=("TkDefaultFont", 20))  
isbn_label.grid(row=0, column=4, sticky="W", padx=5, pady=5)
isbn_entry = ttk.Entry(window, width=24)
isbn_entry.grid(row=0, column=5, sticky="W", padx=5, pady=5)

add_btn = tk.Button(window, text="Add Book", bg="green", fg="white", font="helvetica 10 bold", command=add_book)
add_btn.grid(row=0, column=6, sticky="W", padx=5, pady=5)

list_box = tk.Listbox(window, height=16, width=40, font="helvetica 13", bg="light yellow")
list_box.grid(row=3, column=0, columnspan=14, padx=15, pady=40, sticky=tk.W + tk.E)
list_box.bind('<<ListboxSelect>>', get_selected_row)

scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=1, column=0, rowspan=14, sticky="W")

# Attach listbox to scrollbar
list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)

# Buttons for operations
view_btn = tk.Button(window, text="View All", bg="green", fg="white", font="helvetica 10 bold", command=view_records)
view_btn.grid(row=15, column=1, padx=5, pady=5)

clear_btn = tk.Button(window, text="Clear Screen", bg="green", fg="white", font="helvetica 10 bold", command=clear_screen)
clear_btn.grid(row=15, column=2, padx=5, pady=5)

exit_btn = tk.Button(window, text="Exit", bg="green", fg="white", font="helvetica 10 bold", command=on_closing)
exit_btn.grid(row=15, column=3, padx=5, pady=5)

modify_btn = tk.Button(window, text="Modify Record", bg="green", fg="white", font="helvetica 10 bold", command=update_records)
modify_btn.grid(row=15, column=4, padx=5, pady=5)

delete_btn = tk.Button(window, text="Delete Record", bg="green", fg="white", font="helvetica 10 bold", command=delete_records)
delete_btn.grid(row=15, column=5, padx=5, pady=5)


window.mainloop()