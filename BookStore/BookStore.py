"""
This Program will Stores the Books Information

What user can do :
- can Add/Remove/Update the entry
- Search
- Close

"""

from tkinter import *
#from backend import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=listbox.curselection()[0]
        selected_tuple=listbox.get(index)
        #listbox.delete(0, END)
        entry1.delete(0,END)
        entry1.insert(END, selected_tuple[1])
        entry2.delete(0,END)
        entry2.insert(END, selected_tuple[2])
        entry3.delete(0,END)
        entry3.insert(END, selected_tuple[3])
        entry4.delete(0,END)
        entry4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def delete_command():
    backend.delete(selected_tuple[0])
    entry1.delete(0,END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    listbox.delete(0, END)

def update_command():
    backend.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    #print(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def view_command():
    listbox.delete(0,END)
    for row in backend.view():
        listbox.insert(END,row)

def search_command():
    listbox.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        listbox.insert(END,row)

def addentry_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    listbox.delete(0, END)
    listbox.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

window=Tk()
window.wm_title("Manam's BookStore")


lable1=Label(window, text="Title")
lable1.grid(row=0,column=0)

lable2=Label(window, text="Author")
lable2.grid(row=0,column=2)

lable3=Label(window, text="Year")
lable3.grid(row=1,column=0)

lable4=Label(window, text="ISBN")
lable4.grid(row=1,column=2)

title_text=StringVar()
entry1=Entry(window, textvariable=title_text)
entry1.grid(row=0,column=1)

author_text=StringVar()
entry2=Entry(window, textvariable=author_text)
entry2.grid(row=0,column=3)

year_text=StringVar()
entry3=Entry(window, textvariable=year_text)
entry3.grid(row=1,column=1)

isbn_text=StringVar()
entry4=Entry(window, textvariable=isbn_text)
entry4.grid(row=1,column=3)

listbox =Listbox(window, height=6, width=35)
listbox.grid(row=2,column=0, rowspan=6, columnspan=2)

scrollbar= Scrollbar(window)
scrollbar.grid(row=2,column=2,rowspan=6)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

# This will select item to Delete
listbox.bind('<<ListboxSelect>>',get_selected_row)

button1=Button(window,text="View all", width=10,command=view_command)
button1.grid(row=2,column=3)

button2=Button(window,text="Search Entry", width=10,command=search_command)
button2.grid(row=3,column=3)

button3=Button(window,text="Add entry", width=10,command=addentry_command)
button3.grid(row=4,column=3)

button4=Button(window,text="Update", width=10,command=update_command)
button4.grid(row=5,column=3)

button5=Button(window,text="Delete", width=10,command=delete_command)
button5.grid(row=6,column=3)

button6=Button(window,text="Close", width=10,command=window.destroy)
button6.grid(row=7,column=3)





window.mainloop()