"""
This Program will Stores the Books Information

What user can do :
- can Add/Remove/Update the entry
- Search
- Close

"""

from tkinter import *
import backend.py

window=Tk()


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

button1=Button(window,text="View all", width=10)
button1.grid(row=2,column=3)

button2=Button(window,text="Search entry", width=10)
button2.grid(row=3,column=3)

button3=Button(window,text="Add entry", width=10)
button3.grid(row=4,column=3)

button4=Button(window,text="Update", width=10)
button4.grid(row=5,column=3)

button5=Button(window,text="Delete", width=10)
button5.grid(row=6,column=3)

button6=Button(window,text="Close", width=10)
button6.grid(row=7,column=3)





window.mainloop()