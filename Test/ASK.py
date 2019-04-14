
from tkinter import *
from tkinter import messagebox
window= Tk()


def wifiOnscript():
    messagebox.showinfo("Information!!", "This process may take up to 2 min. Please try after 2min...")

wifiOnButton=Button(window,text="WiFi-ON",command=wifiOnscript, height=1, width=22)
wifiOnButton.grid(row=2,column=0,padx=40, pady=10)


window.mainloop()

