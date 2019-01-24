from tkinter import *
from tkinter import ttk
master = Tk()

# w = Label(master, text="Hello, world!")
# w.pack()


ttk.Label(master, text='Heading Here').grid(row=1, column=1)
# ttk.Separator(master,orient=HORIZONTAL).grid(row=2, columnspan=5,sticky="sw")
ttk.Separator(master).place(x=0, y=26, relwidth=5)

mainloop()